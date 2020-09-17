// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

colorMapping = function (label) {
    switch (label.toLowerCase()) {
        case "pass": return "#32CD32";
        case "fail": return "#DC3545";
        default: return "#e5e5e5";
    }
}
onReady = function () {
    $.ajax({
        url: $("#myResults").attr("data-url"),
        success: function (result) {
            new Chart($("#myResults"), {
                type: 'pie',
                data: {
                    labels: result.labels,
                    datasets: [{
                        data: result.data,
                        backgroundColor: result.labels.map(colorMapping),
                    }],
                }
            });
        }
    });

    // TODO: What needs to be shown? Its hardcoded needs to be adjusted
    new Chart($("#myAttendance"), {
        type: 'doughnut',
        data: {
            labels: ['passed', 'failed'],
            datasets: [{
                data: [70, 30],
                backgroundColor: ['#32CD32', '#FFA500'],
            }],
        },
        options: {
            rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            cutoutPercentage: 50
        }
    });
}

$(document).ready(onReady);


