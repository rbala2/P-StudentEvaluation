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

    $.ajax({
        url: $("#myExamsResults").attr("data-url"),
        success: function (result) {
        new Chart($("#myExamsResults"), {
            type: 'bar',
            data: {
                labels: result.subjects,
                datasets: [
                    {
                        label: "Marks Obtained",
                        backgroundColor: 'rgba(0, 0, 255, 0.5)',
                        borderWidth: 1,
                        data: result.obtained_marks,
                        xAxisID: "bar-x-axis1",
                        stack: "background"
                    },
                    {
                        label: "Total Marks",
                        backgroundColor: 'rgba(0, 0, 0, 0.2)',
                        borderWidth: 1,
                        data: result.total_marks,
                        xAxisID: "bar-x-axis2"
                    }
                ]
            },
            options:{
                scales: {
                    xAxes: [
                        {
                            id: "bar-x-axis2",
                            stacked: true,
                            categoryPercentage: 0.5,
                            barPercentage: 0.5,
                            gridLines: { display: false }
                        },
                        {
                            display: false,
                            stacked: true,
                            id: "bar-x-axis1",
                            type: 'category',
                            categoryPercentage: 0.5,
                            barPercentage: 0.5,
                            gridLines: { offsetGridLines: false},
                            offset: true
                        }
                    ],
                    yAxes: [{
                        id: "bar-y-axis1",
                        stacked: false,
                        ticks: { beginAtZero: true },
                        gridLines:{ display: true },
                        maxTicksLimit: 5
                    }]
                }
            }
        });
    }});
}

$(document).ready(onReady);


