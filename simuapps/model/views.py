# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response	
from simuapps.gva.views import gvexponencial2, gvuniforme2 #, gvnormal2
import json
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
	return HttpResponse(json.dumps(response_data), mimetype="application/json")

def process(request):
	response_data = {}
	arreglo =[]
	res = []
	if request.method == 'GET':
		alet1=float(request.GET['aleat1'])
		alet2=float(request.GET['aleat2'])
		alet3=float(request.GET['aleat3'])
		arreglo.append(alet1)
		arreglo.append(alet2)
		arreglo.append(alet3)
		#add db of aleat vals

		gva=int(request.GET['got'])

		if gva== 1:
			prom=int(request.GET['prom'])
			res = gvexponencial2(prom,arreglo)

		elif gva == 2:
			minim=int(request.GET['min'])
			maxim=int(request.GET['max'])
			res= gvuniforme2(minim,maxim,arreglo)
		elif gva == 3:
			prom=int(request.GET['prom'])
			desv=int(request.GET['desv'])

		response_data['res'] = res

	return HttpResponse(json.dumps(response_data), mimetype="application/json")

def arrib(request):
	response_data = {}
	if request.method == 'GET':
		choice=request.GET['aleat1']
		choice=request.GET['send_resul']
		choice=request.GET['send_resul']
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")