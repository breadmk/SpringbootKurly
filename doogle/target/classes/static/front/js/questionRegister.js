$(function(){
	$("#type1").change(function(){
		if($("#type1").is(":checked")){
			$("#type").val("y");
		}else{
			$("#type").val("n");
		}
	});
initEdit();
});