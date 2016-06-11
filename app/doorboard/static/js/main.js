var options = {
    scaleShowLabels: false,

    ///Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines : false,

    //String - Colour of the grid lines
    scaleGridLineColor : "rgba(1,1,1,.05)",

    //Number - Width of the grid lines
    scaleGridLineWidth : 1,

    //Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: false,

    //Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: false,

    //Boolean - Whether the line is curved between points
    bezierCurve : true,

    //Number - Tension of the bezier curve between points
    bezierCurveTension : 0.4,

    //Boolean - Whether to show a dot for each point
    pointDot : false,

    //Boolean - Whether to show a stroke for datasets
    datasetStroke : false,

    //Number - Pixel width of dataset stroke
    datasetStrokeWidth : 4,

    //Boolean - Whether to fill the dataset with a colour
    datasetFill : true,

    scaleFontColor: 'white'
};

var data = {
    labels: [
        "Now",    "", "", "", "", "", "", "", "", "",
        "10 min", "", "", "", "", "", "", "", "", "",
        "20 min", "", "", "", "", "", "", "", "", "",
        "30 min", "", "", "", "", "", "", "", "", "",
        "40 min", "", "", "", "", "", "", "", "", "",
        "50 min", "", "", "", "", "", "", "", "", "", "1 hour"],
    datasets: [
        {
            fillColor: "rgba(30,144,255,0.5)",
            data: rainProb
        }
    ]
};

$(document).ready(function() {
    setInterval(function() {
        location.reload(true);
        console.log('Reloading');
    }, 30000);

    var ctx = document.getElementById("rain-probability").getContext("2d");
    var rainProbability = new Chart(ctx).Line(data, options);
});

