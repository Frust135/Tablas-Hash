from tkinter import *
from hash import *
#-------------------------------------------------------------------
#          Creación de funciones
#------------------------------------------------------------------
def update_table(tabla_hash):
    altura=110
    for tabla_indice in range(0,10):
        valor=Label(bg='white', width="20", height="1", text=tabla_hash[tabla_indice], font=("Cambria",12), fg="#22061A")
        valor.place(x=510, y=altura)
        altura+=30
    return NONE

def insertar_dato(clave, valor, tabla_hash):
    arreglo_retorno = hashing(clave, valor, tabla_hash)
    tabla_hash=arreglo_retorno[0]
    if arreglo_retorno[2] == ("Ocurrió una colisión en el índice"):
        consola=Label(bg='lightgray', width="30", height="5", text=arreglo_retorno[2]+'\n'+arreglo_retorno[3], font=("Segoe UI Bold",12), fg="#22061A")
        consola.place(x=750, y=200)
    else:
        consola=Label(bg='lightgray', width="30", height="5", text=arreglo_retorno[1], font=("Segoe UI Bold",12), fg="#22061A")
        consola.place(x=750, y=200)
    update_table(tabla_hash)
    return NONE

def obtener_dato(clave,valor):
    indice = busqueda(clave, valor,tabla_hash)
    if (tabla_hash[indice]==-1):
        dato_retorno=("El color " +str(clave)+" no se encuentra"+ '\n' + "almacenado en la tabla HASH")
    else:
        dato_retorno=("El color "+str(clave)+" se encuentra en el índice: "+str(indice)+'\n'+ " Su código HEX es: "+ str(tabla_hash[indice]))
    consola=Label(bg='lightgray', width="32", height="5", text=dato_retorno, font=("Segoe UI Bold",12), fg="#22061A")
    consola.place(x=750, y=200)
    return NONE

#-------------------------------------------------------------------
#          Creación de ventana
#------------------------------------------------------------------
ventana = Tk()
ventana.geometry("1110x450")
ventana['bg'] = '#6B0621'
tabla_hash = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

Titulo=Label(text="Tablas hash para colores HEX" ,font=("Segoe UI Bold",16),fg="#CE7A6C" , bg="#330530", width="893", height="3")

Titulo.pack()
#-------------------------------------------------------------------
#          Creación de box 1
#------------------------------------------------------------------
box_1=Label(bg="#AD3D66", width="45", height="21")
box_1.place(x=25, y=100)

#---------------------Inserción--------------------

titulo_nombre_color = Label(text="Nombre de color", bg="#AD3D66", font=("Segoe UI Bold",14), fg="#22061A")
titulo_nombre_color.place(x=110, y=110)

Entrada_nombre_color = Entry(width="40", bg="#F3CCCD")
Entrada_nombre_color.place(x=64, y=140)

titulo_codigo_hex = Label(text="Código HEX", bg="#AD3D66", font=("Segoe UI Bold",14), fg="#22061A")
titulo_codigo_hex.place(x=130, y=170)

Entrada_codigo_hex = Entry(width="40", bg="#F3CCCD")
Entrada_codigo_hex.place(x=64, y=200)

btn_almacenar = Button(ventana, text="Almacenar", bg="#F3CCCD", command=lambda: insertar_dato(Entrada_nombre_color.get(),Entrada_codigo_hex.get(), tabla_hash))
btn_almacenar.place(x=145, y=250)
#---------------------Busqueda--------------------
titulo_busqueda_color = Label(text="Buscar color", bg="#AD3D66", font=("Segoe UI Bold",14), fg="#22061A")
titulo_busqueda_color.place(x=128, y=300)

Entrada_busqueda_color = Entry(width="40", bg='#F3CCCD')
Entrada_busqueda_color.place(x=64, y=330)

Entrada_busqueda_hex = Entry(width="40", bg='#F3CCCD')
Entrada_busqueda_hex.place(x=64, y=357)

btn_buscar = Button(ventana, text="Buscar", bg="#F3CCCD", command=lambda:obtener_dato(Entrada_busqueda_color.get(),Entrada_codigo_hex.get()))
btn_buscar.place(x=153, y=390)
#-------------------------------------------------------------------
#          Creación de box 2
#------------------------------------------------------------------
box_2=Label(bg="#AD3D66", width="100", height="21")
box_2.place(x=375, y=100)

#---------------------Tablas--------------------
altura = 110
for creador_tabla_indice in range(0,10):
    index=Label(bg='white', width="3", height="1", text=creador_tabla_indice, font=("CaSegoe UI Boldmbria",12), fg="#22061A")
    index.place(x=430, y=altura)
    altura+=30
update_table(tabla_hash)
consola=Label(bg='lightgray', width="30", height="5")
consola.place(x=750, y=200)

ventana.mainloop()
