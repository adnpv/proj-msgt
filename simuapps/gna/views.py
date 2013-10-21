# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response	

#resolv multiple choice
def home(request):
	print "llamado home"
	return "non"
# def home(request):
# 	response_data = {}
# 	if request.method == 'GET': 
# 		choice=request.GET['send_resul']
# 		question_id=request.GET['quest']
# 		#q = Quest.objects.get(id=question_id)
# 		n= choice.split('-', 1 );
# 		chu= n[1]
# 		print chu
# 		valcheck = Choice.objects.filter(id=chu)
# 		if valcheck.count() > 0:
# 			response_data=almacenar(chu)
# 		else:
# 			loadnewdata()
# 			#ingresar valor 
# 	return HttpResponse(json2.dumps(response_data), mimetype="application/json")


def operation(a,x,c):
	return str((a*x)+c)

def operacion(a,x,c,m=0):
	if m == 0:
		return str((a*x)+c)
	else:
		return str((((a * x) + c) % m))

def aValidate(vala):
	mod = (vala - 1) % 4
	if mod == 0:
		return True
	else:
		return False

def pesiValidate(m,c):
	res = m % c
	if c == 1:
		return True
	elif c==0:
		return False
	elif res !=0:
		return True
	else:
		False

def mValidate(p,val):
	#res = m % c
	if val <= p:
		#print "fall 1"
		return False
	else:
		res=0
		for i in range(30):
			res= 2**i
			#print res,val,"hi!!!"
			if res == val:
				#print "fall 2"
				return True
		#print "fall 3",res
		return False

def calcnums(x,m,a,c,filas,p):
	resulta = []
	x_var = x
	vals = []
	periodo = ""
	limit =0
	datus=""
	randomi=""
	try:
		if aValidate(a):
			if mValidate(p, m):
				if pesiValidate(m, c):
					for i in range(filas):
						row=[]
						roundn=[]
						roundn.append(str(i))
						roundn.append(str(x_var))
						roundn.append(operacion(a, x_var, c))
						rvalue=operacion(a, x_var, c, m)
						roundn.append(rvalue)
						#vals.append(rvalue)
						#row.append(roundn)
						resulta.append(roundn)
						x_var = int(operacion(a, x_var, c, m))
						#print i
						#print repr(row)
						#print "valor m",m
						if (x_var == x) and (m != filas+1):
							periodo=str(m)
							limit =1
						else:
							if limit == 0:
								vals.append(rvalue)						
				else:
					resulta = "NO CUMPLE --> 'C y M SON PESI'"
			else:
				resulta = "NO CUMPLE --> 'P > M' o 'M Potencia De Un Cuadrado'"
		else:
			resulta ="NO CUMPLE --> 'A = 4*K + 1'"
		#print repr(resulta)
		datus = repr(resulta)
		randomi = repr(vals)
	except ZeroDivisionError, e:#division por 0
		print e
		resulta ="C no puede ser 0"		
	except Exception, e:#division por 0
		print e
		print "hi!a"
		resulta ="NO DEJE ESPACIOS EN BLANCO"

	return {'result':resulta,
			'periodu':periodo,
			'data': datus,
			'random_vals':randomi,
			'arreg':vals,}

def generar_gna(request):
	#try:
	datoscalc={}
	resulta = []
	vals = []
	periodo = ""
	datus=""
	randomi=""
	limit =0
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
			resulta= datoscalc['result']
			periodo= datoscalc['periodu']
			datus= datoscalc['data']
			randomi= datoscalc['random_vals']

		except Exception, e:#division por 0
			print e
			resulta ="NO DEJE ESPACIOS EN BLANCO"
	return render_to_response('numbers.html', {'result':resulta,
												'periodu':periodo,
												'data': datus,
												'random_vals':randomi,}) 


	#else:
		#pass
	#finally:
		#pass

# private String operacion(int a, int x, int c)
#         {
#             return ((a * x) + c).ToString();
#         }

# private void btnCalcular_Click(object sender, EventArgs e)
#         {
#             dgvResult.Rows.Clear();
#             txtPeriodo.Clear();
#             try
#             {
#                 int x = Convert.ToInt32(txtX.Text);
#                 int x_var = Convert.ToInt32(txtX.Text);
#                 int m = Convert.ToInt32(txtM.Text);
#                 int a = Convert.ToInt32(txtA.Text);
#                 int c = Convert.ToInt32(txtC.Text);
#                 int filas = Convert.ToInt32(txtFilas.Text);
#                 int p = Convert.ToInt32(txtP.Text);

#                 if (aValidate(a))
#                 {
#                     if (mValidate(p, m))
#                     {
#                         if (pesiValidate(m, c))
#                         {
#                             for (int i = 0; i <= filas; i++)
#                             {
#                                 String[] row = new String[] { i.ToString(), x_var.ToString(), operacion(a, x_var, c), operacion(a, x_var, c, m) };
#                                 dgvResult.Rows.Add(row);
#                                 x_var = Convert.ToInt32(operacion(a, x_var, c, m));
#                                 if (x_var == x && m != filas+1)
#                                 {
#                                     txtPeriodo.Text = m.ToString();
#                                 }
#                             }
#                         }
#                         else
#                         {
#                             MessageBox.Show(this, "NO CUMPLE --> 'C y M SON PESI'");
#                         }
#                     }
#                     else
#                     {
#                         MessageBox.Show(this, "NO CUMPLE --> 'P > M' o 'M Potencia De Un Cuadrado'");
#                     }
#                 }
#                 else
#                 {
#                     MessageBox.Show(this, "NO CUMPLE --> 'A = 4*K + 1'");
#                 }
#             }
#             catch (DivideByZeroException dbz)
#             {
#                 Console.WriteLine(dbz);
#                 MessageBox.Show(this, "C no puede ser 0");
#             }
#             catch (Exception ex)
#             {
#                 Console.WriteLine(ex);
#                 MessageBox.Show(this, "NO DEJE ESPACIOS EN BLANCO");
#             }
#         }


#         private String operacion(int a, int x, int c)
#         {
#             return ((a * x) + c).ToString();
#         }

#         private String operacion(int a, int x, int c, int m)
#         {
#             return (((a * x) + c) % m).ToString();
#         }



#         private Boolean aValidate(int val)
#         {
#             double mod = (val - 1) % 4;
#             if (mod != 0)
#             {
#                 return false;
#             }
#             else
#             {
#                 return true;
#             }
#         }


#         private Boolean pesiValidate(int m, int c)
#         {
#             double res = m % c;
#             if (c == 1)
#             {
#                 return true;
#             }
#             else if (c == 0)
#             {
#                 return false;
#             }
#             else if (res != 0)
#             {
#                 return true;
#             }
#             else
#             {
#                 return false;
#             }
#         }


#         private Boolean mValidate(int p, int val)
#         {
#             if (val <= p)
#             {
#                 return false;
#             }
#             else
#             {
#                 double res = 0;
#                 for (int i = 0; i <= 30; i++)
#                 {
#                     res = Math.Pow(2, i);
#                     if (res == val)
#                     {
#                         return true;
#                     }
#                 }
#                 return false;
#             }
#         }