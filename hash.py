def double_hash(h1 ,h2 ,arreglo):
    indice = h1
    aumentador = 1
    while arreglo[indice] != -1:
        indice = (h1 + aumentador* h2)%10
        aumentador = aumentador+1       
    return indice

def esPrimo(numero):
    contador = 0
    for iteracion_numero in range(1,numero+1,1):
        resto = numero % iteracion_numero
        if resto == 0:
            contador = contador+1

    if contador == 2:
        return 1
    else:
        return 0

def NumeroPrimoMasCercano(numero):
    ##recorrido menor a menor 
    for valor in range(numero,0,-1):
        primo = esPrimo(valor)
        if primo == 1:
            return valor

def hashing(arreglo_ingresado, arreglo_nuevo):
    largo_arreglo_ingresado = len(arreglo_ingresado)
    for x in range (0,largo_arreglo_ingresado,1):
        elemento = arreglo_ingresado[x]
        largo_arreglo_nuevo = len(arreglo_nuevo)
        indice_elemento = int(elemento)%largo_arreglo_nuevo
        print("El indice es: ", indice_elemento," del elemento: ", elemento)
        
        while arreglo_nuevo[indice_elemento]!= -1:
            print("OCURRIO UNA COLISIÓN EN EL INDICE")
            numero_primo = NumeroPrimoMasCercano(largo_arreglo_nuevo)
            calculo = int(elemento%numero_primo)
            ecuacion_2 = numero_primo-calculo
            indice_elemento = double_hash(indice_elemento,ecuacion_2,arreglo_nuevo)
            print("El indice real es:",indice_elemento, "del elemento:",elemento)      
           
        arreglo_nuevo[indice_elemento] = elemento
    return arreglo_nuevo

arregloIngresado = [5,25,15,35,95]    
arreglo1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


arreglo3 = hashing(arregloIngresado, arreglo1)





