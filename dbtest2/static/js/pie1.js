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
         allowPointSelect: true,
         size:94,
         innerSize:76,
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
         ['快乐',45.0],
         ['喜悦',26.8],
         // {
         //    name: 'Chrome',
         //    y: 12.8,
         //    sliced: false,
         //    selected: false
         // },
         ['惊讶',12.7],
         ['一般',8.5],
         ['无奈',5.3],
         ['难过',5.3],
         ['愤怒',2.1],
         ['恶心',1.7]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie1').highcharts(json);  
});
