var ctx2 = document.getElementById('barChart').getContext('2d');

var value = document.getElementById('barChart').getAttribute('value');

var array = JSON.parse("[" + value + "]");


var mbarChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['bis 19 Mitarbeiter', '20-49 Mitarbeiter', '50-249 Mitarbeiter', 'ab 250 Mitarbeiter'],
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
            text: 'Umfrageteilnehmer nach Unternehmensgröße',
        },
        legend: {
        display: false,
    },
    }
});