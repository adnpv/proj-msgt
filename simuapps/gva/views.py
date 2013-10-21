# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response	
from simuapps.gna.views import calcnums
import math
#resolv multiple choice

aleatory1 = []
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

def generar_gva2(request):
	#try:
	datoscalc={}
	resulta = []
	vals = []
	periodo = ""
	datus=""
	randomi=""
	limit =0
	gvunif=[]
	gvexponenc =[]
	arreglu=[]
	if request.method == 'GET':
		try:
			x=int(request.GET.get('x'))
			x_var=int(request.GET.get('x'))
			m =int(request.GET.get('m'))
			a =int(request.GET.get('a'))
			c =int(request.GET.get('c'))
			filas =int(request.GET.get('filas'))
			p =int(request.GET.get('p'))
			
		
			datoscalc=calcnums(x,m,a,c,filas,p)
			randomi= datoscalc['random_vals']
			vals= datoscalc['arreg']
			for i in range(len(vals)):
				arreglu.append(vals[i])
				#print "arr",arreglu[i]
			#gvunif=gvuniforme(vals)

			gvexponenc=gvexponencial(arreglu)


			#aleatory1=vals
		except Exception, e:#division por 0
			print e
			resulta ="NO DEJE ESPACIOS EN BLANCO"
	return render_to_response('gvas.html', {'random_vals':randomi,
											'arreglu':vals,
											'unifv':gvunif,
											'exponv':gvexponenc,}) 



def gvexponencial(arreglo):
	valores=[] 
	n=float(len(arreglo))
	suma=0.0
	#print arreglo[4],"val3"
	#print type(arreglo[4]),"valuke"
	for i in range(len(arreglo)):
		suma += float(arreglo[i])
		#print arreglo[i]

	prome= suma/n

	print "promedio",prome
	landa= (1.0/prome)
	print landa
	for i in range(len(arreglo)):
		valint=float(arreglo[i])
		#if valint != 0 :
		valint = valint/100
		dat=1.0-valint
		dat2 = math.log(dat)

		resu=(dat2)*(-1)/(landa)
		valores.append(resu)

	return valores






# def gvuniforme(arreglo):
# 	valores=[]
# 	maxim=max(arreglo)
# 	minim=min(arreglo)

# 	for i in range(len(arreglo)):
# 		resu=minim + (arreglo[i] *(maxim-minim))
# 		valores.append(resu)

# 	return valores







# def gvnormal(promedio,desvest,arreglo, aleat12):
# 	valores=[]

# 	for i in range(len(arreglo)):
# 		resu=promedio + desvest*((aleat12)-6)
# 		valores.append(resu)

# 	return valores



def gvexponencial2(prome, arreglo):
	valores=[] 
	print arreglo,"inside"
	for i in range(len(arreglo)):
		valint=arreglo[i]
		#valint = valint/100
		dat =1.0-valint
		#dat2 = math.log(dat)

		resu=(math.log(dat))*(-prome)
		valores.append(resu)

	return valores

def gvuniforme2(minim, maxim, arreglo):
	valores=[]
	for i in range(len(arreglo)):
		resu=minim + (arreglo[i] *(maxim-minim))
		valores.append(resu)

	return valores

# def gvnormal2(promedio,desvest,arreglo, aleat12):
# 	valores=[]

# 	for i in range(len(arreglo)):
# 		resu=promedio + desvest*((aleat12)-6)
# 		valores.append(resu)

# 	return valores

















# def generar_gva(request):
# 	#try:
# 	datoscalc={}
# 	resulta = []
# 	vals = []
# 	periodo = ""
# 	datus=""
# 	randomi=""
# 	limit =0
# 	if request.method == 'GET':
# 		try:
# 			x=int(request.GET.get('x'))
# 			x_var=int(request.GET.get('x'))
# 			m =int(request.GET.get('m'))
# 			a =int(request.GET.get('a'))
# 			c =int(request.GET.get('c'))
# 			filas =int(request.GET.get('filas'))
# 			p =int(request.GET.get('p'))

		
# 			datoscalc=calcnums(x,m,a,c,filas,p)
# 			randomi= datoscalc['random_vals']
# 			vals= datoscalc['arreg']



# 			aleatory1=vals
# 		except Exception, e:#division por 0
# 			print e
# 			resulta ="NO DEJE ESPACIOS EN BLANCO"
# 	return render_to_response('gvas.html', {'random_vals':randomi,
# 											'arreglu':vals,}) 


# def generar_uniforme(request):
# 	arreglo=aleatory1
# 	randomi=repr(arreglo)
# 	if request.method == 'GET':
# 		try:
# 			minima=int(request.GET.get('mini'))
# 			maximo=int(request.GET.get('maxi'))
					
# 			datoscalc=gvuniforme(minima,maximo, arreglo)
# 			randomi= datoscalc['random_vals']
# 			vals= datoscalc['arreg']
# 			aleatory1=vals
# 		except Exception, e:#division por 0
# 			print e
# 			resulta ="NO DEJE ESPACIOS EN BLANCO"
# 	return render_to_response('gvas.html', {'random_vals':randomi,}) 


# def generar_exponencial(request):
# 	arreglo=[]
# 	randomi=repr(arreglo)
# 	datoscalc = []
# 	datoscalcrep =""
# 	if request.method == 'GET':
# 		try:
# 			arreglo = request.GET.get('arreglo')
# 			n=len(arreglo)
# 			suma=0
# 			for i in range(len(arreglo)):
# 				suma += arreglo[i]
# 				print "helloko"
# 			prome= suma/n #int(request.GET.get('x'))
					
# 			datoscalc=gvexponencial(prome,arreglo)
# 			datoscalcrep = repr(datoscalc)
# 			#randomi= datoscalc['random_vals']
# 			#vals= datoscalc['arreg']
# 			#aleatory1=vals
# 		except Exception, e:#division por 0
# 			print e
# 			resulta ="NO DEJE ESPACIOS EN BLANCO"
# 	return render_to_response('gvas.html', {'random_vals':datoscalc,
# 											'reprec':datoscalcrep,}) 

