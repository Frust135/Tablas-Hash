from tkinter import *

#-------------------------------------------------------------------
#          Creación de ventana
#------------------------------------------------------------------
ventana = Tk()
ventana.geometry("1110x450")
ventana['bg'] = '#6B0621'

Titulo=Label(text="Tablas hash para colores HEX" ,font=("Cambria",16),fg="#CE7A6C" , bg="#330530", width="893", height="3")

Titulo.pack()
#-------------------------------------------------------------------
#          Creación de box 1
#------------------------------------------------------------------
box_1=Label(bg="#AD3D66", width="45", height="21")
box_1.place(x=25, y=100)

titulo_nombre_color = Label(text="Nombre de color", bg="#AD3D66", font=("Cambria",14), fg="#22061A")
titulo_nombre_color.place(x=110, y=110)

Entrada_nombre_color = Entry(width="40", bg="#F3CCCD")
Entrada_nombre_color.place(x=64, y=140)

titulo_codigo_hex = Label(text="Código HEX", bg="#AD3D66", font=("Cambria",14), fg="#22061A")
titulo_codigo_hex.place(x=130, y=170)

Entrada_codigo_hex = Entry(width="40", bg="#F3CCCD")
Entrada_codigo_hex.place(x=64, y=200)

btn_almacenar = Button(ventana, text="Almacenar", bg="#F3CCCD", command="#")
btn_almacenar.place(x=145, y=250)

#-------------------------------------------------------------------
#          Creación de box 2
#------------------------------------------------------------------
box_2=Label(bg="#AD3D66", width="100", height="21")
box_2.place(x=375, y=100)

ventana.mainloop()
