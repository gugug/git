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
            data : xaxis
        }
    ],
    yAxis : [
        {
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
            name:'搜索热度',
            type:'line',
            data: seris_data,
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