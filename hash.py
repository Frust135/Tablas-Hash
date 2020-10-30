def double_hash(h1,h2, arreglo):
    aa = h1
    b=1
    while arreglo[aa] != -1:
        aa = (h1 + b* h2)%10
        b=b+1       
    return aa

def esPrimo(x):
    contador = 0
    for f in range(1,x+1,1):
        div = x % f
        if div == 0:
            contador = contador+1

    if contador == 2:
        return 1
    else:
        return 0

def NumeroPrimoMasCercano(x):
    for s in range(x,0,-1):
        primo = esPrimo(s)
        if primo == 1:
            return s

def hashing(arreglo_ingresado, arreglo_nuevo):
    largoAI = len(arreglo_ingresado)
    for x in range (0,largoAI,1):
        elemento = arreglo_ingresado[x]
        largoAN = len(arreglo_nuevo)
        indice_elemento = int(elemento)%largoAN
        print("El indice es: ", indice_elemento," del elemento: ", elemento)
        
        while arreglo_nuevo[indice_elemento]!= -1:
            print("OCURRIO UNA COLISIÓN EN EL INDICE")
            Nprimo = NumeroPrimoMasCercano(largoAN)
            calcu = int(elemento%Nprimo)
            h2 = Nprimo-calcu
            indice_elemento = double_hash(indice_elemento,h2,arreglo_nuevo)
            print("El indice real es:",indice_elemento, "del elemento:",elemento)      
           
        arreglo_nuevo[indice_elemento] = elemento

    return arreglo_nuevo

arregloIngresado = [5,25,15,35,95]    
arreglo1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


arreglo3 = hashing(arregloIngresado, arreglo1)





