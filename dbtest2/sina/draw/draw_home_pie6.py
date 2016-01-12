# coding=utf-8
__author__ = 'gu'
from sina.exercise import *
def draw_pie6(file_name):
    infile = open('/home/gu/PycharmProjects/dbtest2/sina/draw/home_pie_common.txt','r')
    outfile = open(file_name,'w+')
    outfile.write(infile.read()+'\n'+
                  """
                  var series= [{
      type: 'pie',
      name: '占比',
      data: [
         ['快乐',"""+home_pie6()[0]+"""],
         ['喜悦',"""+home_pie6()[1]+"""],
         ['惊讶',"""+home_pie6()[2]+"""],
         ['一般',"""+home_pie6()[3]+"""],
         ['无奈',"""+home_pie6()[4]+"""],
         ['难过',"""+home_pie6()[5]+"""],
         ['愤怒',"""+home_pie6()[6]+"""],
         ['恶心',"""+home_pie6()[7]+"""]
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

                  """


                  )

    infile.close()
    outfile.close()
    print 'Done home_pie6'

# draw_pie6()