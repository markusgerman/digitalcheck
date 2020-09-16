
var ctx10 = document.getElementById('reifegradkmu').getContext('2d');

var value = document.getElementById('reifegradkmu').getAttribute('value');

var array = JSON.parse("[" + value + "]");

var mbarChart = new Chart(ctx10, {
    type: 'pie',
    data: {
        labels: ["Digitaler Beginner", "Digital Mithaltender", "Digitaler Vorreiter"],
        datasets: [{
            label: '# Umfrageteilnehmer nach Digitalisierungsgrad KMU',
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
            text: 'Umfrageteilnehmer nach Digitalisierungsgrad (KMU)',
        },
        legend: {
        display: false,
    },
    }
});
