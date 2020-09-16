
var ctx5 = document.getElementById('dogChart').getContext('2d');

var value = document.getElementById('dogChart').getAttribute('value');

var array = JSON.parse("[" + value + "]");

var mbarChart = new Chart(ctx5, {
    type: 'doughnut',
    data: {
        labels: ["Dienstleistung" , "prod", "handel"],
        datasets: [{
            label: '# Umfrageteilnehmer nach Branche',
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
            text: 'Umfrageteilnehmer nach Branche',
        },
        legend: {
        display: false,
    },
    }
});

