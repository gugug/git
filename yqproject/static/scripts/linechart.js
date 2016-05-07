option = {
    title : {
    },
    tooltip : {
        trigger: 'axis',
        axisPointer:{
            type : 'line',
            lineStyle : {
                  color: '#999',
                  width: 2,
                  type: 'solid'
            },
        }
    },
    grid:{
            borderWidth:0,
            borderColor:'#fff'
            },
    xAxis : [
        {
            name:'时间',
            splitLine:{
                show:false,
            },
            axisTick:{
                show:false,
            },
            axisLine:{
                lineStyle:{
                    color:'#999999',
                }
                
            },
            axisLabel: {
                show: true,
                textStyle: {
                    color: '#333'
                }
            },
            type : 'category',
            boundaryGap : false,
            data : ['6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00','1:00','2:00','3:00','4:00']
        }
    ],
    yAxis : [
        {
            name:'事件规模量(万/每小时)',
            splitLine:{
                show:false,
            },
            axisLine:{
                lineStyle:{
                    color:'#999',
                }  
            },
            axisLabel: {
                show: true,
                textStyle: {
                    color: '#333'
                }
            },
            type : 'value',
            axisLabel : {
                formatter: '{value} '
            },

        }
    ],
    series : [
        {
            smooth:true,
            name:'事件规模量(万/每小时)',
            type:'line',
            data: [1,3,7,6,10,18,25,30,19,15,18,20,22,32,21,19,20,16,7,5,2,0,0],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            itemStyle:{
                normal:{
                    // color:'#F89C0D',
                    lineStyle:{
                        color:'#5CC595',
                    }
                }
            }

        },

    ]
};