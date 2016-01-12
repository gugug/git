

$(document).ready(function() {
   var chart = {
    backgroundColor: 'rgba(0,0,0,0)',
    type: 'column'
 };
   var title = {
     style:{
                     color:"#fff",},
      text: ''
   };
   var subtitle = {
    style:{
                     color:"#fff",},
      text: ''
   };

var credits = {
      enabled: false
   };
   var xAxis = {
      categories:['开心','快乐','满意','惊讶','不满','无奈','难过','痛恨'],
      labels: {
         rotation: -45,
         style: {
            fontSize: '13px',
            fontFamily: 'Verdana, sans-serif',
            color:"#FFFFFF",
         }
      }
   };
   var yAxis ={
      min: 0,
      title: {
        text: 'Percent (%)',
          style:{color:"#fff"}
      },
      gridLineColor: '#197F07',//控制图后面平行于x轴的几条线的颜色
    gridLineWidth: 0,//控制图后面平行于x轴的几条线的宽度
     labels: {
         rotation: -45,
         style: {
            fontSize: '13px',
            fontFamily: 'Verdana, sans-serif',
            color:"#FFFFFF",
         }
      }
   };
   var tooltip = {
      pointFormat: '情绪: <b>{point.y:.1f} %</b>'
   };

   var plotOptions = {
      column: {

        showInLegend:false
      }

   };
   var series= [{
            name: ' ',

                        data: [{y:7.8,color:"#F7846B"},
                {y:3.1,color:"#F79C9C"},
                {y:2.5,color:"#FFBDA5"},
                               {y:8.9,color:"#FFE6DE"},
                               {y:19.1,color:"#FFFFEF"},
                {y:18.5,color:"#FFEFBD"},
                               {y:27.2,color:"#D6E6B5"},
                {y:27.2,color:"#CEE6E6"}]



           /* dataLabels: {
                enabled: true,
                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y:.1f}', // one decimal
                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '15px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }*/  //控制显示在柱状图上的数字的一系列的形态，包括显示与否，角度，样式等
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.subtitle = subtitle;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.plotOptions = plotOptions;
   json.tooltip = tooltip;
   json.credits = credits;
   json.series = series;
   $('#bar_chart').highcharts(json);

});
