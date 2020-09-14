var ctx7 = document.getElementById('dogChart3').getContext('2d');

var value = document.getElementById('dogChart3').getAttribute('value');



var mbarChart = new Chart(ctx7, {
    type: 'doughnut',
    data: {
        labels: ["test", "test2", "test3"],
        datasets: [{
            label: '# Umfrageteilnehmer der Handelsbranche',
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
            text: 'Umfrageteilnehmer der Handelsbranche',
        },
        legend: {
        display: false,
    },
    }
});