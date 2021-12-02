/* Function to create plot */
function plotData() {

    let graph_data = [];
    let graph_times = [];
    var sensorToLook = getSelectedSensor();
    {% for dataEntry in timeData %}
    if ('{{dataEntry.id_tag}}' == sensorToLook) {
        graph_data.push(Number('{{dataEntry.masl}}'));
        graph_times.push('{{dataEntry.time}}');
    }
    {% endfor %}

    const ctx = document.getElementById('Chart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: graph_times,
            datasets: [{
                label: 'Data for sensor ' + sensorToLook,
                data: graph_data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)'

                ],
                borderWidth: 1
            }]
        },
        options: {
            elements: {
                point: {
                    radius: 0
                }
            },
            plugins: {
              zoom: {
                zoom: {
                  mode: 'x',
                  overScaleMode: 'x',
                  drag: {
                    enabled: true
                  }
                },
                pan: {
                  enabled:true,
                  modifierKey: 'shift',
                  mode: 'y'
                }

              }
            }
        }
    });

    return myChart
}

/* Function to update plot given a change in sensor dropdown */
function updatePlot(){
    let graph_data = [];
    let graph_times = [];
    var sensorToLook = getSelectedSensor();
    {% for dataEntry in timeData %}
        if ('{{dataEntry.id_tag}}' == sensorToLook) {
            graph_data.push(Number('{{dataEntry.masl}}'));
            graph_times.push('{{dataEntry.time}}');
        }
    {% endfor %}
    myChart.data.datasets[0].data = graph_data;
    myChart.data.datasets[0].label = 'Data for sensor ' + sensorToLook;
    myChart.data.labels = graph_times;
    myChart.update();
    console.log('Updated the plot')
}
