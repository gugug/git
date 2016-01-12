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
		      	oLogin.innerHTML="<div class='loginCon'><div id='close'></div><form name='login' action='/login/' method='post'><ul><li>" +
					"<input type='text' placeholder='用户名' name='username'></li><li><input type='password'" +
					" placeholder='密码',name='password'></li><li>" +
					"<input type='submit' value='登录'></li></ul></form></div>";
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
window.onload=function(){
         var oBtn=document.getElementById("btnLogin");
        oBtn.onclick=function(){
              	openNew1();
               	return false;
        }
}