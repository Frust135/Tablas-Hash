# ____________________________________________________________
#
# Función que realiza el Doble Hash
# ____________________________________________________________
def double_hash(h1 ,h2 ,arreglo):
    indice = h1
    aumentador = 1
    while arreglo[indice] != -1:
        indice = (h1 + aumentador* h2)%10
        aumentador = aumentador+1       
    return indice
# ____________________________________________________________
#
# Función que retorna el valor primo
# ____________________________________________________________
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
# ____________________________________________________________
#
# Función que retorna el número primo más cercano
# ____________________________________________________________
def NumeroPrimoMasCercano(numero):
    ##recorrido menor a menor 
    for valor in range(numero,0,-1):
        primo = esPrimo(valor)
        if primo == 1:
            return valor
# ____________________________________________________________
#
# Función Ascii (Retorna la suma del valor ascii de una palabra)
# ____________________________________________________________
def get_ascii(palabra):
    arreglo_palabra=list(palabra)
    acumulador = 0
    for recorrido in range(0, len(arreglo_palabra)):
        acumulador+=ord(arreglo_palabra[recorrido])
    return acumulador

# ____________________________________________________________
#
# Función que realiza el Hashing
# ____________________________________________________________
def hashing(clave, valor, tabla_hash):
    largo_hash = len(tabla_hash)
    indice_elemento=get_ascii(clave)%largo_hash
    print("El indice de: ", clave, "es: ", indice_elemento)
    while tabla_hash[indice_elemento]!=-1:
        print("OCURRIÓ UNA COLISIÓN EN EL ÍNDICE")
        numero_primo = NumeroPrimoMasCercano(largo_hash)
        calculo = int(get_ascii(clave)%numero_primo)
        ecuacion = numero_primo-calculo
        indice_elemento = double_hash(indice_elemento, ecuacion, tabla_hash)
        print("El indice nuevo de: ", clave, "es: ", indice_elemento)
    tabla_hash[indice_elemento] = valor
    return tabla_hash
# def hashing(arreglo_ingresado, arreglo_nuevo):
#     largo_arreglo_ingresado = len(arreglo_ingresado)
#     for x in range (0,largo_arreglo_ingresado,1):
#         elemento = arreglo_ingresado[x]
#         largo_arreglo_nuevo = len(arreglo_nuevo)
#         indice_elemento = int(elemento)%largo_arreglo_nuevo
#         print("El indice es: ", indice_elemento," del elemento: ", elemento)
        
#         while arreglo_nuevo[indice_elemento]!= -1:
#             print("OCURRIO UNA COLISIÓN EN EL INDICE")
#             numero_primo = NumeroPrimoMasCercano(largo_arreglo_nuevo)
#             calculo = int(elemento%numero_primo)
#             ecuacion_2 = numero_primo-calculo
#             indice_elemento = double_hash(indice_elemento,ecuacion_2,arreglo_nuevo)
#             print("El indice real es:",indice_elemento, "del elemento:",elemento)      
           
#         arreglo_nuevo[indice_elemento] = elemento
#     return arreglo_nuevo

tabla_hash = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
clave = 'verde'
valor = '#verde'
clave1 = 'azul'
valor1 = '#azul'
clave2 = 'rojo'
valor2 = '#rojo'
clave3 = 'morado'
valor3 = '#morado'
clave4 = 'purpura'
valor4 = '#purpura'
hashing(clave, valor, tabla_hash)
hashing(clave2, valor2, tabla_hash)
hashing(clave3, valor3, tabla_hash)
hashing(clave4, valor4, tabla_hash)
print(tabla_hash)



