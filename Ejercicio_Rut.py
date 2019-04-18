#Ejercicio 1 de Guia Lab
#Mauricio troncoso
print("Bienvenido")
def rut():
    Q = [2,3,4,5,6,7,2,3,4,5,6,7]
    W = input("Ingrese su RUT sin puntuaciones ni digito verificador: ")
    W = W[::-1]
    E = 0
    D = 0
    Dv = 12
    S = 0
    
    while E < len(W):
        D = int(W[E])*int(Q[E])
        S = S + D
        E= E + 1
    print (S)
    v = 11 - (S % 11)
    
    if 0 < v < 10:
        Dv = v
    elif v == 11:
        Dv = 0
    elif v == 10:
        str(Dv)
        Dv = "K"
        
    print ("Su digito verificador es: ", Dv)
    
rut()
    
