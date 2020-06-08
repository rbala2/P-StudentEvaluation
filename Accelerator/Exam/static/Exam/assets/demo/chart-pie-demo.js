// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
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

var ctx = document.getElementById("ResultsPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [70, 30],
      backgroundColor: ['#87CEEB', '#FFFF00'],
    }],
  }
});
