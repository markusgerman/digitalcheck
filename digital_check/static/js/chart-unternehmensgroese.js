
var ctx = document.getElementById('myChart').getContext('2d');

var value = document.getElementById('myChart').getAttribute('value');

var array = JSON.parse("[" + value + "]");

var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['myconsult', 'IHK-KU', 'IHK-KMU'],
        datasets: [{
            label: '# Umfrageteilnehmer nach Institution',
            data: array,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
            ],
            borderWidth: 1
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        title: {
            display: true,
            text: 'Umfrageteilnehmer nach Institution',
        }
    }
});

