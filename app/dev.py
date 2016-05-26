# Set the path
import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'doorboard')))

from flask.ext.script import Manager, Server
from doorboard import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=False,
    use_reloader=False,
    host='0.0.0.0')
)

if __name__ == "__main__":
    manager.run()
