function MainFunction(attendance_list) {
    google.load('visualization', '1', {packages: ['controls', 'charteditor']});
    google.setOnLoadCallback(drawChart);
    function drawChart(){
        var data = new google.visualization.DataTable();
        data.addColumn('date', 'X');
        data.addColumn('number', 'Expected time');
        data.addColumn('number', 'Real time');
        attendance_list.forEach(function (item) {
            data.addRow([new Date(item[0], item[1]-1, item[2]), 8, item[3]]);
        });
        var dash = new google.visualization.Dashboard(document.getElementById('dashboard'));

        var control = new google.visualization.ControlWrapper({
            controlType: 'ChartRangeFilter',
            containerId: 'control_div',
            options: {
                filterColumnIndex: 0,
                ui: {
                    chartOptions: {
                        height: 50,
                        width: 600,
                        chartArea: {
                            width: '80%'
                        }
                    }
                }
            }
        });

        var chart = new google.visualization.ChartWrapper({
            chartType: 'LineChart',
            containerId: 'chart_div'
        });

        function setOptions(wrapper) {

            wrapper.setOption('width', 620);
            wrapper.setOption('chartArea.width', '80%');

        }

        setOptions(chart);


        dash.bind([control], [chart]);
        dash.draw(data);
        google.visualization.events.addListener(control, 'statechange', function () {
            const controlState = control.getState();
            const filteredResults = data.getFilteredRows([{
              column: 0,
              minValue: controlState.range.start,
              maxValue: controlState.range.end
            }]);

            let totalValue = 0;
            for (let i  = 0; i < filteredResults.length; i++) {
              totalValue += data.getValue(filteredResults[i], 1);
            }

            document.getElementById('total_work_amount').textContent = totalValue;
            document.getElementById('dbgchart').innerHTML = controlState.range.start+ ' to ' +controlState.range.end;
            return 0;
        });
    }
}