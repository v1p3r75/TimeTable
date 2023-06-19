document.addEventListener('DOMContentLoaded', (e) => {
    document.querySelector('.preloader').style.display = 'none';
})
        // Données factices pour l'exemple
        var data = {
            labels: ['L1', 'L2', 'L3', 'M1', 'M2', 'ISI'],
            datasets: [
                {
                    label: 'Enseignants',
                    data: [20, 25, 30, 35, 28, 22],
                    borderColor: '#18aefa', // Couleur de la ligne
                    backgroundColor: '#18aefa', // Couleur de fond
                    fill: false, // Pas de remplissage sous la ligne
                },
                {
                    label: 'Étudiants',
                    data: [50, 45, 60, 55, 58, 62],
                    borderColor: '#3D5EE1', // Couleur de la ligne
                    backgroundColor: '#3D5EE1', // Couleur de fond
                    fill: false, // Pas de remplissage sous la ligne
                }
            ]
        };

        // Configuration du graphique
        var options = {
            responsive: true,
            title: {
                display: true,
                text: "Comparaison du nombre d'enseignants et d'étudiants"
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        };

        // Création du graphique
        var ctx = document.getElementById('graph-viewer').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: data,
            options: options
        });