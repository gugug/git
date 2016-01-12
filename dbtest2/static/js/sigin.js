function openNew2(){
   	//获取页面的高度和宽度
   	var sWidth=document.body.scrollWidth;
      var sHeight=document.body.scrollHeight;
      //获取页面的可视区域高度和宽度
      var wHeight=document.documentElement.clientHeight;
      var oMask=document.createElement("div");
      oMask.id="mask1";
      oMask.style.height=sHeight+"px";
      oMask.style.width=sWidth+"px";
      document.body.appendChild(oMask);
      var oSigin=document.createElement("div");
      oSigin.id="sigin";
      oSigin.innerHTML="<div class='siginCon'><div id='close1'></div><form ><ul><li><input type='text' placeholder='用户名'></li><li><input type='password' placeholder='密码'></li><li><input type='submit' value='注册'></li></ul></form></div>";
      document.body.appendChild(oSigin);
   
      //获取登陆框的宽和高
      var dHeight=oSigin.offsetHeight;
      var dWidth=oSigin.offsetWidth;
      //设置登陆框的left和top
      oSigin.style.left=sWidth/2-dWidth/2+"px";
      oSigin.style.top=wHeight/2-dHeight/2+"px";
      //点击关闭按钮
      var oClose=document.getElementById("close1");
   
      //点击登陆框以外的区域也可以关闭登陆框
      oClose.onclick=oMask.onclick=function(){
            document.body.removeChild(oSigin);
            document.body.removeChild(oMask);
      };
};
window.onload=function(){
      var oBtn1=document.getElementById("btnSigin");
      oBtn1.onclick=function(){
            openNew2();
            return false;
      }   
} 