var ctx6 = document.getElementById('dogChart2').getContext('2d');

var mbarChart = new Chart(ctx6, {
    type: 'doughnut',
    data: {
        labels: ['bis 19 Mitarbeiter', '20-49 Mitarbeiter', '50-249 Mitarbeiter', 'ab 250 Mitarbeiter'],
        datasets: [{
            label: '# Umfrageteilnehmer produzierendes Gewerbe',
            data: [12 ,23 , 23],
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
            text: 'Umfrageteilnehmer produzierendes Gewerbe',
        },
        legend: {
        display: false,
    },
    }
});