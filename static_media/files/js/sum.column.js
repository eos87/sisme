function sumAndputHere(tablaID, classToSum, elem_id, decimal){
	$('#'+elem_id).html(sumarColumnas(tablaID, classToSum, decimal));
}

function sumarColumnas(tablaID, classToSum, decimal){
	var tot = 0;
	console.log($("#" + tablaID + " ." + classToSum));
	$("#" + tablaID + " ." + classToSum).each(function(){		
		tot += parseFloat($(this).html());
	});		
	if(decimal==1){
		return tot.toFixed(2);
	}else{
		return tot.toFixed(0);
	}
	
}