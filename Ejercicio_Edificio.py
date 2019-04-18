#Ejercicio 2
#Mauricio Troncoso

x=(input("ingrese un numero: "))
num=x
piso= num[:2]
t=num[2:]
Z=int(piso)
if Z==20:
  print("El valor del piso es de: 400")
  t=int(input("ingrese los ultimos 2 digitos: "))
  if t== (0,4):
      print("Departamento con vista al cerro")
      print("Aplicando descuento")
      print("El valor total es de:320" )
  elif t== 7:
     print("Departamento con vista al mar")
     print("Aplicando aumento por vista")
     print("El valor total es de:460" ) 
  elif t== 3:
      print("Departamento con vista al mar")
      print("Aplicando aumento por vista")
      print("El valor total es de:460" ) 
  else:
     print("El valor del departamento es:400")
if Z ==1:
   print("El valor del piso es de 100") 
   t=int(input("ingrese los ultimos 2 digitos: "))
   if t== (0,4):
     print("Departamento con vista al cerro")
     print("Aplicando descuento")
     print("El valor total es de:80" )
   elif t== 7 or 3:
    print("Departamento con vista al mar")
    print("Aplicando aumento por vista")
    print("El valor total es de:115" )    
   else:
    print("El valor del departamento es:100")
   
elif Z>20:
    print("Piso no valido")
elif Z<20: 
    print("valor del departamento es 250") 
    t=(input("ingrese una opcion: "))
    a=0 or 4
    if t== (a): 
     print("Departamento con vista al cerro")
     print("Aplicando descuento")
     print("El valor total es de:200" )
     
    b= 7 or 3
    if t== (b):
     print("Departamento con vista al mar")
     print("Aplicando aumento por vista")
     print("El valor total es de:287,5" )   
    c=[2,19] 
    if t==(c):
     print("El valor del departamento es:250")
print("gracias por su visita")     