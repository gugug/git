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
         allowPointSelect: false,
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
         ['快乐',18.0],
         ['喜悦',22.8],
         // {
         //    name: 'Chrome',
         //    y: 12.8,
         //    sliced: false,
         //    selected: false
         // },
         ['惊讶',11.7],
         ['一般',10.5],
         ['无奈',8.3],
         ['难过',8.3],
         ['愤怒',6.1],
         ['恶心',5.7]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#oPie6').highcharts(json);  
});