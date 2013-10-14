# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response	

#resolv multiple choice
def home(request):
	response_data = {}
	if request.method == 'GET':
		choice=request.GET['send_resul']
		question_id=request.GET['quest']
		#q = Quest.objects.get(id=question_id)
		n= choice.split('-', 1 );
		chu= n[1]
		print chu
		valcheck = Choice.objects.filter(id=chu)
		if valcheck.count() > 0:
			response_data=almacenar(chu)
		else:
			loadnewdata()
			#ingresar valor 
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")