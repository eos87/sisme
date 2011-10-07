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

(function($) {
	var cache = [];
	// Arguments are image paths relative to the current page.
	$.preLoadImages = function() {
		var args_len = arguments.length;
		for ( var i = args_len; i--;) {
			var cacheImage = document.createElement('img');
			cacheImage.src = arguments[i];
			cache.push(cacheImage);
		}
	}
})(jQuery)

$(document).ready(function(){
	jQuery.preLoadImages("/files/img/spin.gif",);
})