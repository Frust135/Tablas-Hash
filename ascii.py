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

print(get_ascii('Hola'))