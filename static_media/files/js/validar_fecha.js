var $ = django.jQuery;
$(document).ready(function() {		
	/* chequear que la url sea add o edit */
	var estado = checkURL();
	if(estado == 'add'){
		$('#id_mes, #id_anio').attr('disabled', true);
		$('#id_anio').change(function(){
			if($(this).val() != ''){
				loadOptions('', $('#id_proyecto').val());
			}
		});
	}else{
		
	}
	
	$('#id_proyecto').change(function(){
		if(estado == 'add'){
			if($(this).val() != ''){
				$('#id_anio').removeAttr('disabled');
			}else{
				$('#id_anio').attr('disabled', true);
			}
		}		
	});
});

function checkURL(){
	var url = window.location.href.split('/');
	if(url[url.length-2]=="add"){
		return 'add';
	}else{
		return 'edit';
	}
}
function loadOptions(url, proy_id){
	$.getJSON('/ajax/meses/id='+proy_id+url, function(data){
        $('#id_organizacion').html('');
        if(data){
            $.each(data, function(i, item){
                $('<option></option>').val(item.id).html(item.nombre_corto).appendTo(orgs)
            });
            orgs.multiselect('refresh');
            orgs.multiselect("enable");
        }
    });
}
/*validar que los dos campos tengan valor*/
function validarSeleccion() {	
	if (($("#id_mes").val() != "") && ($("#id_mes").val() != "")) {
		return true;
	} else {
		return false;
	}
}

