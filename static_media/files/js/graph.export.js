function exportGraph(data, title, elem){
	var foo = data;
	var titulo = title;
	var csrf_token =  $.cookie('csrftoken');	
	$.post("/graph-params/", {
		data : foo,
		title: titulo,
		csrfmiddlewaretoken : csrf_token
	}, function(data) {		
		if(data=='error'){
			alert('Ha ocurrido un error :(');			
		}else{
			$(elem).html('');					
			$(link).fancybox(options).trigger('click');	
		}		
	});	
}