// function checkUser_1(){
//    username_1=document.form_1.username_1.value; 
//    pwd_1=document.form_1.pwd_1.value; 
//    if(username_1.length<6||username_1.length>15){ 
// //检查用户名是否在指定的范围之内 
// alert("用户名长度必须在6-15位之间！"); 
// return false; 
// } 
// if(pwd_1.length<6||pwd_1.length>20){ 
// //检查密码是否在指定范围之内 
// alert("密码必须在6-20位之间!"); 
// return false; 
// }
// }
// function checkUser_2(){
//    username_2=document.form_2.username_2.value; 
//    pwd_2=document.form_2.pwd_2.value; 
//    if(username_2.length<6||username_2.length>15){ 
// //检查用户名是否在指定的范围之内 
// alert("用户名长度必须在6-15位之间！"); 
// return false; 
// } 
// if(pwd_2.length<6||pwd_2.length>20){ 
// //检查密码是否在指定范围之内 
// alert("密码必须在6-20位之间!"); 
// return false; 
// }
// }
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
          oSigin.innerHTML="<div class='siginCon'><div id='close'></div>" +
                    "<form name='register' action='/register/' method='post'><ul><li><input  type='text' name='name_1" +
              "' placeholder='用户名'></li>" +
                    "<li><input type='password' name='pwd_1' placeholder='密码'></li><li><input type='submit' name='sub_1' value='注册'></li></ul></form></div>";
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
      var oBtn=document.getElementById("btnLogin");
      //点击登录按钮
      var oBtn1=document.getElementById("btnSigin");
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