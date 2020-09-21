
var ctx20 = document.getElementById('dienstChart').getContext('2d');

var value = document.getElementById('dienstChart').getAttribute('value');

x = JSON.parse(value)
var values = Object.values(x)

var keys = Object.keys(x)

for (var i = 0; i < x.length; i++){
    // look for the entry with a matching `code` value
    if (x[i].code == "index"){
       
    }
  }

var mbarChart = new Chart(ctx20, {
    type: 'bar',
    data: {
      labels: keys,
      datasets: [
        {
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data:values,
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
            text: 'Umfrageteilnehmer Dienstleistungsbranche',
        },
        legend: {
        display: false,
    },
    }
});

