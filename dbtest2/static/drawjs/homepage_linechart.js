
         $(document).ready(function()
            {
              var chart =
              {
                      backgroundColor: 'rgba(0,0,0,0)',
                      type: 'line',
              };


              var title =
                {
                  text: ''  ,
                  x: -20
                  };

              var subtitle =
                {
                  // text: 'Source:广外舆情项目组',
                  x: -20,//确定了显示位置，例如-200，标题就会更加偏左
                  style:{
                     color:"#ffffff",
                  }

                };

              var plotOptions=
              {
                  series: {
                      marker: {
                            radius: 4,  //曲线点半径，默认是4
                            symbol: 'circle'//曲线点类型："circle", "square", "diamond", "triangle","triangle-down"，默认是"circle"
                      }
                  }
              };

              var xAxis =
                {
                  lineColor:'rgba(0,0,0,0)',
                  categories: ['1月', '2月', '3月', '4月', '5月','6月','7月','8月','9月','10月','11月','12月'],
                  tickWidth:0,//好像是控制贴近x轴的那条线的长度
                  plotLines:
                    [{value: 0,
                    width: 0,
                    color: '#ffffff'
                  }],
                  labels: {
                    style: {
                      color: '#ffffff',//颜色
                      fontSize:'12px'  //字体
                    }
                  },

                };
              var yAxis =
              {
                gridLineWidth:0,//平行于x轴的几条线
                title:
                  {
                    text: '社区数： (个)',
                    style:{
                    color:"#ffffff",
                  }
              },

                plotLines:
                [{
                    value: 0,
                    width: 0,
                    color: '#ffffff'//绘制主线 灰色

                }],
                labels: {
                    y: 20, //x轴刻度往下移动20px
                    style: {
                      color: '#ffffff',//颜色
                      fontSize:'12px'  //字体
                    }
                },
            };

            var tooltip =
            {
                valueSuffix: '个'
            }

            var legend = {
                  layout: 'vertical',  //【图例】显示的样式：水平（horizontal）/垂直（vertical）
                  align: 'right',
                  verticalAlign: 'middle', //让图例在中间显示，不会偏上或偏下
                  borderWidth: 2,
                  borderRadius:5,
                  borderColor:'#ffffff',
                  itemStyle : {
                     'color': '#ffffff'
                  },
               }

             var series = [
            {
               type:'spline',
               name: '开心',
               data: [1, 1, 1, 1, 12, 9, 7, 9, 11, 25, 22, 13]
            },

            {
               type:'spline',
               name: '快乐',
               data: [16, 22, 18, 12, 11, 8, 6, 8, 22, 11, 23, 26]
            },

            {
               type:'spline',
               name: '满意',
               data: [13, 18, 26, 22, 17, 11, 16, 22, 18, 12, 11, 8]
            },

            {
               type:'spline',
               name: '惊讶',
               data: [6, 11, 18, 24, 15, 12, 26, 22, 17, 11, 16, 22]
            },

            {
               type:'spline',
               name: '无奈',
               data: [2, 4.0, 7.9, 13.8, 11, 18, 24, 15, 12, 26, 17.2, 14.8]
            },

            {
               type:'spline',
               name: '不满',
               data: [-1.4, 2.5, 5.8, 2, 4.0, 7.9, 13.8, 11, 9.2, 15.9, 22.7, 22]
            },

            {
               type:'spline',
               name: '难过',
               data: [-3.7, -0.8, 2.9, -1.4, 2.5, 5.8, 2, 4.0, 7.6, 14.8, 22.3, 11]
            },

            {
               type:'spline',
               name: '痛恨',
               data: [0.6, 2.2, -3.7, -0.8, 2.9, -1.4, 2.5, 5.8, 5.9, 9.7, 15.8, 17.7]
            }];

            Highcharts.setOptions({
               credits: { enabled: false }
            })
            Highcharts.setOptions({
                colors: ['#F7846B','#F79C9C', '#FFBDA5', '#FFE6DE', '#FFFFEF', '#FFEFBD',
               '#D6E6B5', '#CEE6E6']
              // colors: ['#ffffff','#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
              // '#ffffff', '#ffffff']
            });
             var json = {};
             json.chart=chart;
             json.title = title;
             json.subtitle = subtitle;
             json.plotOptions = plotOptions;
             json.xAxis = xAxis;
             json.yAxis = yAxis;
             json.tooltip = tooltip;
             json.legend = legend;
             json.series = series;

             $('#right').highcharts(json);
         });
        