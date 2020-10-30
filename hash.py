

def double_hash(h1,h2, arreglo):
    aa = h1
    b=1
    while arreglo[aa] != -1:
        aa = (h1 + b* h2)%10
        print(aa)
        b=b+1
        
    return aa

def hashing(arreglo_ingresado, arreglo_nuevo):
    
    for x in range (0,5,1):
        elemento = arreglo_ingresado[x]
        indice_elemento = int(elemento)%10
        print("El indice es: ", indice_elemento," del elemento: ", elemento)
        a=1
        while arreglo_nuevo[indice_elemento]!= -1 and a==1:
            print("OCURRIO UNA COLISIÓN EN EL INDICE")
            calcu = int(elemento%7)
            h2 = 7-calcu
            
            
            indice_elemento = double_hash(indice_elemento,h2,arreglo_nuevo)
            print("El indice real es:",indice_elemento, "del elemento:",elemento)
            
            a=9
        arreglo_nuevo[indice_elemento] = elemento

    return arreglo_nuevo

arreglo = [5,25,15,35,95]    
arreglo1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


arreglo3 = hashing(arreglo, arreglo1)





