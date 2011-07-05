function sumAndputHere(tablaID, uniqueClass, elem_id, decimal){
	$('#'+elem_id).html(sumarColumnas(tablaID, uniqueClass, decimal));
}

function sumarColumnas(tablaID, uniqueClass, decimal){
	var tot = 0;
	$("#" + tablaID + " ." + uniqueClass).each(function(){
		tot += parseFloat($(this).html());
	});		
	if(decimal==1){
		return tot.toFixed(2);
	}else{
		return tot.toFixed(0);
	}
	
}