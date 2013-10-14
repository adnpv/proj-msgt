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

def generar_gna(request):
	response_data = {}
	datok = 1
	resultk=[]
	
	if request.method == 'GET':
		x=request.GET.get('x')
		x_val=request.GET.get('x')
		m =request.GET.get('m')
		a =request.GET.get('a')
		c =request.GET.get('c')
		filas =request.GET.get('filas')
		p =request.GET.get('p')

		
			r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
			data2 = r.json()
			data3 =json2.loads(r.content)
			datok= data3[0]['nombre']
			#datok= data2[0]['nombre']
			#datok = len(data2)
			for i in range(len(data2)):
				if i == 0:
					print 'no'
				else:
					opc1.append(data2[i]['nombre'])
			 		#opc1[i]=data2[i]['nombre']

		jsonString = json2.dumps(data2,sort_keys='nice',indent=4)
		#datok = jsonString
	return render_to_response('numbers.html', {'result':resultk,}) 