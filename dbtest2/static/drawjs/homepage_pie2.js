$(document).ready(function(){
   var chart = {
       // plotBackgroundColor: null,
       // plotBorderWidth: null,
       // plotShadow: false
      backgroundColor: 'rgba(255, 255, 255, 0)',
      plotBorderColor : null,
      plotBackgroundColor: null,
      plotBackgroundImage:null,
      plotBorderWidth: null,
      plotShadow: false,

   };
   var title = {
      text: ''
   };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: false,//控制圆环图是否裂开
         size:94,
         innerSize:72,
         cursor: 'pointer',
         dataLabels: {
            enabled: false,
            format: '<b>{point.name}%</b>: {point.percentage:.1f} %',
            style: {
               color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
            }
         }
      }
   };

                  var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['快乐',12],
         ['喜悦',22],
         ['惊讶',32],
         ['一般',42],
         ['无奈',52],
         ['难过',62],
         ['愤怒',72],
         ['恶心',82]
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie2').highcharts(json);
});

                  