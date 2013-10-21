$(document).ready(function(){
$("input[name=fde]").click(function(){
    var rad_val = $('input:radio[name=fde]:checked').val();
    //alert(rad_val);
    switch (rad_val)
	{
	   case '1': 
	   		$(".gvas").css('display','none');
	        $("#uniforme").css('display','block');
	       break;
	   case '2': 
	   		$(".gvas").css('display','none');
	        $("#exponencial").css('display','block');
	       break;
	   case '3': 
	   		$(".gvas").css('display','none');
	        $("#normal").css('display','block');
	       break;
	}
});
$("input[name=fde2]").click(function(){
    var rad_val = $('input:radio[name=fde2]:checked').val();
    //alert(rad_val);
    switch (rad_val)
	{
	   case '1': 
	   		$(".gvas2").css('display','none');
	        $("#uniforme2").css('display','block');
	       break;
	   case '2': 
	   		$(".gvas2").css('display','none');
	        $("#exponencial2").css('display','block');
	       break;
	   case '3': 
	   		$(".gvas2").css('display','none');
	        $("#normal2").css('display','block');
	       break;
	}
});
});