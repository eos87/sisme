function exportGraph(data, title){
	var foo = data;
	var titulo = title;
	var csrf_token =  $.cookie('csrftoken');	
	$.post("/graph-params/", {
		data : foo,
		title: titulo,
		csrfmiddlewaretoken : csrf_token
	}, function(data) {		
		if(data!='error'){
			var options = {
				'width' : 970,
				'height' : 500,
				'autoScale' : false,
				'type' : 'iframe'
			}
			var link = $('<a></a>').attr('href', '/view-graph/')
			$(link).fancybox(options).trigger('click');
			return;
		}else{
			alert('Ha ocurrido un error :(');
		}
	});	
}