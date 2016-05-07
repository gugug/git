function change(){
			var sidebar=document.getElementById('sidebar');
			var content=document.getElementById('content');
			width_sidebar=sidebar.style.width ||sidebar.offsetWidth || sidebar.clientWidth;
			if(width_sidebar!='0px'){
			sidebar.style.width='0';
			content.style.width='100%';
			}
			else{
			sidebar.style.width='20%';
			content.style.width='80%';	
			}
		};