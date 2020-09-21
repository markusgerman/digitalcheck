
var ctx20 = document.getElementById('handelChart').getContext('2d');

var value = document.getElementById('handelChart').getAttribute('value');

x = JSON.parse(value)

delete x.null;
delete x.Total;

var values = Object.values(x)

var keys = Object.keys(x)

var mbarChart = new Chart(ctx20, {
    type: 'bar',
    data: {
      labels: keys,
      datasets: [
        {
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: values,
        }
      ]
    },
    
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
            xAxes:[{
                ticks:{
                    display: false
                }
            }]
        },
        responsive: true,
        maintainAspectRatio: false,
        title: {
            display: true,
            text: 'Umfrageteilnehmer Handel',
        },
        legend: {
        display: false,
    },
    }
});

