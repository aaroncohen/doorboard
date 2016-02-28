import calendar
import datetime

import forecastio
import os
from flask import Flask, render_template
from flask.ext.appconfig import AppConfig


def create_app(configfile=None):
    new_app = Flask(__name__)
    AppConfig(new_app, configfile)
    return new_app

# Loads settings from default_config.py, then from a .cfg file specified in DOORBOARD_CONFIG env var,
# then from any environment variables prefixed with DOORBOARD_
app = create_app()

app.secret_key = app.config.get('SECRET_KEY') or os.urandom(24)

api_key = app.config.get('FORECASTIO_API_KEY')
home = app.config.get('HOME')

update_delay = datetime.timedelta(seconds=app.config.get('UPDATE_DELAY'))
last_updated = datetime.datetime.now() - update_delay
last_weather = forecastio.load_forecast(api_key, *home)


def update_weather():
    global last_weather, last_updated

    if last_updated + update_delay <= datetime.datetime.now():
        last_updated = datetime.datetime.now()
        last_weather = forecastio.load_forecast(api_key, *home)


@app.template_filter('dayname')
def dayname(date):
    return calendar.day_name[date.weekday()]


@app.template_filter('tempcolor')
def tempcolor(value):
    if value > 85:
        return 'v-warm'
    elif value > 75:
        return 'warm'
    elif value < 55:
        return 'cold'
    elif value < 45:
        return 'v-cold'
    else:
        return ''


@app.route('/')
def doorboard():
    update_weather()

    currently = last_weather.currently()
    minutely = last_weather.minutely()
    hourly = last_weather.hourly()
    daily = last_weather.daily()
    today = daily.data[0]

    current_icon = currently.d['icon']
    current_temp = int(round(currently.d['temperature']))
    feels_like = int(round(currently.d['apparentTemperature']))
    high_temp = int(round(today.d['apparentTemperatureMax']))
    low_temp = int(round(today.d['apparentTemperatureMin']))

    rain_prob = [minute.d['precipIntensity'] for minute in minutely.data]
    rain_soon = any(rain_prob)

    return render_template('doorboard.html',
                           current_icon=current_icon, current_temp=current_temp,
                           feels_like=feels_like, high=high_temp, low=low_temp,
                           current_text=currently.summary, next_hour_text=minutely.summary, next_day_text=hourly.summary,
                           next_week_text=daily.summary, days=daily.data, rain_soon=rain_soon, rain_prob=rain_prob)


if __name__ == '__main__':
    app.run()
