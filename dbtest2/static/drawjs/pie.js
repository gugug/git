
        $(document).ready(function() {
   var chart = {
      backgroundColor: 'rgba(0,0,0,0)',
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,

   };
   var title = {
      style:{
                     color:"#b8b8b8",},
      text: ''
   };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: false
         },
         showInLegend: false//下面图例是否出现
      }
   };
    // var InLegend = {
    //               itemStyle : {
    //                  'color': '#b8b8b8'
    //               },
    //            }
   Highcharts.setOptions({
credits: { enabled: false }
})
   var series= [{
      type: 'pie',
      name: '情绪',


      data: [
         ['快乐',1],
         ['喜悦',2],
         ['惊讶',3],
         {
            name: '一般',
            y: 4,
            sliced: false,
            selected: false
         },
         ['无奈',5],
         ['难过',6],
         ['愤怒',7],
         ['恶心',8]
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#pie_chart').highcharts(json);
});

        