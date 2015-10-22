function checkUser(){
   username=document.form1.username.value; 
   pwd1=document.form1.pwd1.value; 
   if(username.length<6||username.length>15){ 
//检查用户名是否在指定的范围之内 
alert("用户名长度必须在6-15位之间！"); 
return false; 
} 
if(pwd1.length<6||pwd1.length>20){ 
//检查密码是否在指定范围之内 
alert("密码必须在6-20位之间!"); 
return false; 
}
}
function checkUser1(){
   username1=document.form2.username1.value; 
   pwd2=document.form2.pwd2.value; 
   pwd3=document.form2.pwd3.value; 
   if(username1.length<1||username1.length>15){
//检查用户名是否在指定的范围之内 
alert("用户名长度必须在2-15位之间！");
return false; 
} 
if(pwd2.length<6||pwd2.length>20){ 
//检查密码是否在指定范围之内 
alert("密码必须在6-20位之间!"); 
return false; 
} 
if(pwd2!=pwd3){ 
//检查密码是否一致 
alert("密码不匹配!") 
return false; 
} 
}
function openNew1(){
   //获取页面的高度和宽度
   var sWidth=document.body.scrollWidth;
   var sHeight=document.body.scrollHeight;
   //获取页面的可视区域高度和宽度
   var wHeight=document.documentElement.clientHeight;
   var oMask=document.createElement("div");
      oMask.id="mask";
      oMask.style.height=sHeight+"px";
      oMask.style.width=sWidth+"px";
      document.body.appendChild(oMask);
   var oLogin=document.createElement("div");
      oLogin.id="login";
      oLogin.innerHTML="<div class='loginCon'> " +
          "<div id='close'>点击关闭</div><form name='form1' action='/login/'  method='post' ' onsubmit = 'return checkUser();'>" +
          "<ul><li><input type='text' name='username' placeholder='用户名/长度6-15位之间' id='userid'></li>" +
          "<li><input type='password' name='password' placeholder='密码/长度在6-20之间' id='userpassid'></li>" +
          "<li><input type='submit' value='登录'></li><li><p>忘记密码？<a href=''>找回</a></p></li></ul></form></div>";
      document.body.appendChild(oLogin);
   
   //获取登陆框的宽和高
   var dHeight=oLogin.offsetHeight;
   var dWidth=oLogin.offsetWidth;
      //设置登陆框的left和top
      oLogin.style.left=sWidth/2-dWidth/2+"px";
      oLogin.style.top=wHeight/2-dHeight/2+"px";
   //点击关闭按钮
   var oClose=document.getElementById("close");
   
      //点击登陆框以外的区域也可以关闭登陆框
      oClose.onclick=oMask.onclick=function(){
               document.body.removeChild(oLogin);
               document.body.removeChild(oMask);
               };
               };

function openNew2(){
   //获取页面的高度和宽度
   var sWidth=document.body.scrollWidth;
   var sHeight=document.body.scrollHeight;
   //获取页面的可视区域高度和宽度
   var wHeight=document.documentElement.clientHeight;
   var oMask1=document.createElement("div");
      oMask1.id="mask1";
      oMask1.style.height=sHeight+"px";
      oMask1.style.width=sWidth+"px";
      document.body.appendChild(oMask1);
   var osigin=document.createElement("div");
      osigin.id="sigin";
      osigin.innerHTML="<div class='siginCon'><div id='close1'>点击关闭</div><form name='form2' action='/register/'  method='post'  onsubmit = 'return checkUser1();'>" +
          "<ul><li><input type='text' name='username1' placeholder='用户名/长度在6-15位之间' " +
          "id='userid1'></li><li><input type='password' name='pwd3' placeholder='密码/长度在6-20之间'" +
          " id='userpassid1'></li><li><input type='password' name='pwd2' placeholder='请再输入一次密码'id='userpassid2'>" +
          "</li><li><input type='submit' value='注册'></li></ul></form></div>";
      document.body.appendChild(osigin);
   
   //获取登陆框的宽和高
   var dHeight=osigin.offsetHeight;
   var dWidth=osigin.offsetWidth;
      //设置登陆框的left和top
      osigin.style.left=sWidth/2-dWidth/2+"px";
      osigin.style.top=wHeight/2-dHeight/2+"px";
   //点击关闭按钮
   var oClose1=document.getElementById("close1");
   
      //点击登陆框以外的区域也可以关闭登陆框
      oClose1.onclick=oMask1.onclick=function(){
               document.body.removeChild(osigin);
               document.body.removeChild(oMask1);
               };
               };               
   window.onload=function(){
         var oBtn=document.getElementById("btnLogin");
            //点击登录按钮
         var oBtn1=document.getElementById("btnsigin");
            //点击登录按钮
            oBtn.onclick=function(){
               openNew1();
               return false;
               }
            oBtn1.onclick=function(){
               openNew2();
               return false;
               }   
      } 


$(document).ready(function() {  
   var chart = {
     backgroundColor: 'rgba(0,0,0,0.15)',
            type: 'line'
      
   }; 
   var title = {
       text: '舆情监测系统'   
   };
   var subtitle = {
        text: 'Source:广外舆情项目组'
   };
   var xAxis = {
       categories: ['2011年', '2012年', '2013年', '2014年', '2015年']
   };
   var yAxis = {
      title: {
         text: '社区数： (个)'
      },
      plotLines: [{
         value: 0,
         width: 1,
         color: '#808080'
      }]
   };   

   var tooltip = {
      valueSuffix: '个'
   }

   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
   };

   var series =  [
      {
         name: '快乐',
         data: [7.0, 19.0, 21.0, 22.0,22.0]
        
      }, 
      {
         name: '悲伤',
         data: [3.0, 9.0, 5.0, 7.0, 12.0]
        
      }, 
      {
         name: '气愤',
         data: [18.0, 19.0, 14.0, 10.0, 13.0]
         
      }, 
      {
         name: '兴奋',
         data: [13.0, 9.0, 5.0, 8.0, 11.0]
        
      },
      {
      name: '惊奇',
         data: [8.0, 4.0, 5.0, 8.0, 13.0]
      },
      {
      name: '信任',
         data: [24.0, 20.0, 15.0, 7.0, 11.0]
      },
      {
      name: '内疚',
         data: [15.0, 11.0, 5.0, 8.0, 3.0]
      },
      {
      name: '厌恶',
         data: [11.0, 8.0, 5.0, 8.0, 3.0]
      }
   ];
Highcharts.setOptions({
credits: { enabled: false }
})
Highcharts.setOptions({
    colors: ['#ee82ee','#ff0000', '#90ee90', '#87cefa', '#ffb6c1', '#FF9655',
'#FFF263', '#6AF9C4']
});
   var json = {};
   json.chart=chart;
   json.title = title;
   json.subtitle = subtitle;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.tooltip = tooltip;
   json.legend = legend;
   json.series = series;

   $('#spline1').highcharts(json);
});            