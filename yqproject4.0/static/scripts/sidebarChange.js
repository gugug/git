function change(){
			var sidebar=document.getElementById('sidebar');
			var content=document.getElementById('content');
			var container=document.getElementById('siderbar-container');
			width_sidebar=sidebar.style.width ||sidebar.offsetWidth || sidebar.clientWidth;
			if(width_sidebar!='0px'){
			//container.style.display='none';
			sidebar.style.width='0';
			content.style.width='100%';
			}
			else{
				//container.style.display='block';
			sidebar.style.width='20%';
			content.style.width='80%';

			}
		};