



$(document).ready(function(){




$('.procesos').click(function() {

  	var id=$(this).attr('id');
  	var valu;
  	var alet1 = $('input[name=al1]').val();
	var alet2 = $('input[name=al2]').val();
	var alet3 = $('input[name=al3]').val();
  	switch (id)
	{
	   case 'exp': 
			var prom = $('input[name=promed]').val();
			valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 1,
				'prom': prom};
	       break;
	   case 'unif': 
	   		var min = $('input[name=min]').val();
	   		var max = $('input[name=max]').val();
	   		valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 2,
				'min': min,
				'max':max};
	       break;
	   case 'norm': 
	   		var prom = $('input[name=promnorm]').val();
	   		var desv = $('input[name=desvest]').val();
	   		valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 3,
				'prom': prom,
				'desv': desv};
	       break;
	}

	$.ajax({
	    type: "GET",
	    dataType: "json",
	    url: "/model/valores_procesos",
	    data: valu,
	    success: function(response){
	        //alert('thanks');
	        $.each(response, function(key,val) {
	        	for ( i=0; i < val.length; i++)
				{
					$('#proc').append(val[i]+"<br>");
				}
                      
            });

	    },
	    error: function (xhr, ajaxOptions, thrownError) {
	        alert(xhr.responseText);
	        alert(thrownError);
	        alert('error');
	    }
	});


});







$('.procesos2').click(function() {

  	var id=$(this).attr('id');
  	var valu;
  	var alet1 = $('input[name=al12]').val();
	var alet2 = $('input[name=al22]').val();
	var alet3 = $('input[name=al32]').val();
  	switch (id)
	{
	   case 'exp2': 
			var prom = $('input[name=promed2]').val();
			valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 1,
				'prom': prom};
	       break;
	   case 'unif2': 
	   		var min = $('input[name=min2]').val();
	   		var max = $('input[name=max2]').val();
	   		valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 2,
				'min': min,
				'max':max};
	       break;
	   case 'norm2': 
	   		var prom = $('input[name=promnorm2]').val();
	   		var desv = $('input[name=desvest2]').val();
	   		valu={ 'aleat1': alet1,
				'aleat2': alet2,
				'aleat3': alet3,
				'got': 3,
				'prom': prom,
				'desv': desv};
	       break;
	}

	$.ajax({
	    type: "GET",
	    dataType: "json",
	    url: "/model/valores_procesos",
	    data: valu,
	    success: function(response){
	        //alert('thanks');
	        $.each(response, function(key,val) {
	        	for ( i=0; i < val.length; i++)
				{
					$('#arrib').append(val[i]+"<br>");
				}
                      
            });

	    },
	    error: function (xhr, ajaxOptions, thrownError) {
	        alert(xhr.responseText);
	        alert(thrownError);
	        alert('error');
	    }
	});


});




$("#next1").click(function(){
    //revision si 

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

});