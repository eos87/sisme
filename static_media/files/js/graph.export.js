var options = {
	'width' : 970,
	'height' : 500,
	'autoScale' : false,
	'type' : 'iframe'
}
var link = $('<a></a>').attr('href', '/view-graph/');
var img = $('<img>').attr('src', '/files/img/spin.gif');

function exportGraph(data, title, id){	
	$('#'+id).html(img);
	
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
			$('#'+id).html('');
			console.log(id);
			$(link).fancybox(options).trigger('click');	
		}		
	});	
}