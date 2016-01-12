# coding=utf-8
__author__ = 'gu'
from sina.exercise import *
def draw_pie(file_name):
    file = open(file_name,'w')
    file.write(
        """
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
         ['快乐',"""+pie_data()[0]+"""],
         ['喜悦',"""+pie_data()[1]+"""],
         ['惊讶',"""+pie_data()[2]+"""],
         {
            name: '一般',
            y: """+pie_data()[3]+""",
            sliced: false,
            selected: false
         },
         ['无奈',"""+pie_data()[4]+"""],
         ['难过',"""+pie_data()[5]+"""],
         ['愤怒',"""+pie_data()[6]+"""],
         ['恶心',"""+pie_data()[7]+"""]
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

        """
    )
    file.close()
    print 'Done kaixin pie'

# draw_pie('/home/gu/PycharmProjects/dbtest2/static/drawjs/pie.js')



