var $ = django.jQuery;
$(document).ready(function() {		
	/* chequear que la url sea add o edit */
	var estado = checkURL();
	if(estado == 'add'){
		$('#id_mes, #id_anio').attr('disabled', true);
		$('#id_anio').change(function(){
			if($(this).val() != ''){
				loadOptions('', $('#id_proyecto').val(), $(this).val());
			}
		});
	}else if(estado == 'edit'){
		var selecto = $('#id_mes').val();
		loadOptions('&load='+selecto, $('#id_proyecto').val(), $('#id_anio').val());		
	}
	
	$('#id_proyecto').change(function(){
		if(estado == 'add'){
			if($(this).val() != ''){
				$("#id_anio").val($("#id_anio option:first").val());
				$('#id_anio').removeAttr('disabled');				
				$('#id_mes').attr('disabled', true);
			}else{
				$('#id_anio').attr('disabled', true);
				$('#id_mes').attr('disabled', true);
			}
		}		
	});
});

function checkURL(){
	var url = window.location.href.split('/');
	if((url[url.length-2]=="add") && (url.length == 8)){
		return 'add';
	}else if(url.length == 8){
		return 'edit';
	}
}
function loadOptions(url, proy_id, year){
	$.getJSON('/ajax/meses/?id='+proy_id+'&year='+year+url, function(data){
        $('#id_mes').html('');
        $('#id_mes').removeAttr('disabled');
        $('<option></option>').val('').html('-------').appendTo($('#id_mes'));
        if(data){
            $.each(data, function(i, item){
                $('<option></option>').val(item.id).html(item.nombre).appendTo($('#id_mes'));
            });
            if(url != ''){
            	$("#id_mes").val(url.split('=')[1]);
            }            
        }
    });
}