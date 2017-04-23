/*
$(function(){  
	$('#loginButton').click(function(){

		var uid = $("#uid").val();  
		var password = $("#password").val();  

		alert(uid + " " + password);

		$.post('validate',{uid:uid, password:password},function(data){
			alert(data)
			if ("OK" == data)
				window.location.href = "/";
		});
	});  


	$('#registerButton').click(function(){
		window.location.href = "/user/register"
	});  
});
*/
$(document).ready(function(){ 
	$(".form-template-error-div").attr("class", "col-sm-offset-2 col-sm-10");
	$(".form-template-error-span").attr("class", "text-danger small");
	$(".form-template-field-label").attr("class", "control-label col-sm-3");
	$(".form-template-field").attr("class", "col-sm-9 form-box");

});
