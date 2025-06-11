from collections import deque
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

"""
    Agregar scrollbar
    agrear ventana de palabra aceptada
    agregar label paso 3
    intentar eliminar transiciones de a una
"""


def recoger_entrada():
    global transiciones
    if (not entry1.get().strip() or not entry2.get().strip() or
        not entry3.get().strip() or not entry4.get().strip() or
        not entry5.get().strip()):
        messagebox.showwarning("Campos vacios", "Por favor, complete todos los campos.")
        return
    
    transicion = (entry1.get(), entry2.get(), entry3.get(),
                  entry4.get(), entry5.get())
    transiciones.append(transicion)
    print(transiciones)

    lista_transiciones.config(state="normal")
    lista_transiciones.insert(tk.END, f"δ(q{entry1.get()},{entry2.get()},{entry3.get()}) = (q{entry4.get()},") #simbolo
    if (entry5.get() == "-"):
        lista_transiciones.insert(tk.END, f"ε)\n") #simbolo
    else:
        lista_transiciones.insert(tk.END, f"{entry5.get()})\n")
    lista_transiciones.config(state="disabled")
        
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)


def borrar():
    global transiciones

    transiciones = []

    lista_transiciones.config(state="normal")
    lista_transiciones.delete("1.0", tk.END)
    lista_transiciones.config(state="disabled")

    print(transiciones)


def menu_editar():
    global transiciones
    
    def al_cambiar_opcion(*args):
        if seleccion.get() in lineas:
            frame_ocultar2.place_forget()
        else:
            frame_ocultar2.place(x=0, y=80)

    def editar():
        global transiciones
        if (not entry11.get().strip() or not entry12.get().strip() or
            not entry13.get().strip() or not entry14.get().strip() or
            not entry15.get().strip()):
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return
    
        transicion_nueva = (entry11.get(), entry12.get(), entry13.get(),
                      entry14.get(), entry15.get())
        transiciones[lineas.index(seleccion.get())] = transicion_nueva
        print(transiciones)

        lista_transiciones.config(state="normal")
        texto_transicion = f"δ(q{entry11.get()},{entry12.get()},{entry13.get()}) = (q{entry14.get()},"
        if (entry15.get() == "-"):
            texto_transicion += f"ε)"
        else:
            texto_transicion += f"{entry15.get()})"
            
        lista_transiciones.config(state="normal")
        lineas_texto = lista_transiciones.get("1.0", "end-1c").splitlines()
        indice_linea = lineas.index(seleccion.get())
        lineas_texto[indice_linea] = texto_transicion

        lista_transiciones.delete("1.0", tk.END)
        for linea in lineas_texto:
            lista_transiciones.insert(tk.END, linea + "\n")
        lista_transiciones.config(state="disabled")
        
        ventana_emergente.destroy()
            
    lineas = lista_transiciones.get("1.0", tk.END).splitlines()
    lineas = [linea for linea in lineas if linea.strip()]  

    if not lineas:
        return  

    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Editar transiciones")
    ventana_emergente.geometry("500x300")

    fondo = tk.Frame(ventana_emergente, bg="#fcf6d2", height=300, width=500)
    fondo.place(x=0, y=0)

    seleccion = tk.StringVar(ventana_emergente)
    seleccion.set("Seleccione transicion a editar")
    seleccion.trace_add("write", al_cambiar_opcion)

    menu_opciones = tk.OptionMenu(ventana_emergente, seleccion, *lineas)
    menu_opciones.config(bg="#f5cf9f", activebackground="#fcf6d2", font=fuente1, relief=tk.SOLID, borderwidth=2)
    menu_opciones.pack(pady=20, padx=20)

    menu = menu_opciones["menu"]
    for i, linea in enumerate(lineas):
        menu.entryconfig(i, font=fuente1, background="#f5cf9f")
    
    label_inst = tk.Label(fondo, text="(Para ingresar ε, escriba '-')", font=fuente5, bg="#fcf6d2")
    label_inst.place(x=150, y=60)
    
    label11 = tk.Label(fondo, text="Estado actual", font=fuente1, bg="#fcf6d2")
    label11.place(x=10, y=100)
    labelq11 = tk.Label(fondo, text="q", font=fuente4, bg="#fcf6d2")
    labelq11.place(x=133, y=95)
    entry11 = tk.Entry(fondo, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
    entry11.place(x=150, y=100)

    label12 = tk.Label(fondo, text="Simbolo a leer", font=fuente1, bg="#fcf6d2")
    label12.place(x=10, y=140)
    entry12 = tk.Entry(fondo, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
    entry12.place(x=150, y=140)

    label13 = tk.Label(fondo, text="Tope de stack", font=fuente1, bg="#fcf6d2")
    label13.place(x=10, y=180)
    entry13 = tk.Entry(fondo, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
    entry13.place(x=150, y=180)

    imagen1 = tk.PhotoImage(file="flecha.png")
    label_flecha1 = tk.Label(fondo, image=imagen, bg="#fcf6d2")
    label_flecha1.place(x=210, y=125)

    label14 = tk.Label(fondo, text="Nuevo estado", font=fuente1, bg="#fcf6d2")
    label14.place(x=290, y=120)
    labelq12 = tk.Label(fondo, text="q", font=fuente4, bg="#fcf6d2")
    labelq12.place(x=423, y=115)
    entry14 = tk.Entry(fondo, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
    entry14.place(x=440, y=120)

    label15 = tk.Label(fondo, text="Agregar a stack", font=fuente1, bg="#fcf6d2")
    label15.place(x=290, y=160)
    entry15 = tk.Entry(fondo, width=6, font=fuente3, relief=tk.SOLID, borderwidth=2)
    entry15.place(x=440, y=160)

    boton_cambios = tk.Button(fondo, text="Confirmar cambios", command=editar, font=fuente1, relief=tk.SOLID, borderwidth=2, bg="#f5cf9f")
    boton_cambios.place(x=170, y=250)

    frame_ocultar2 = tk.Frame(fondo, bg="#fcf6d2", height=240, width=500)
    frame_ocultar2.place(x=0, y=60)

def ocultar():
    if (opcion_final.get() == "estado"):
        frame_ocultar.place_forget()
    else:
        entry7.delete(0, tk.END)
        frame_ocultar.place(x=8, y=155)

#validar_palabra
def validar_palabra():
    global transiciones
    palabra = entry_palabra.get() + "-"
    estado_inicial = entry6.get()
    estado_actual = estado_inicial
    estado_final = None 

    if (entry7.get()):
        estado_final = entry7.get()

    pila = deque(['R'])
    for i in range(len(palabra)):
        simbolo_actual = palabra[i]
        print("Simbolo actual: ", simbolo_actual)
        print("Estado actual: ", estado_actual)
        print("Tope de pila: ", pila[0])
        
        #Cambio: ahora tambien busca la transicion que coincida con tope de pila
        resultado = next((t for t in transiciones if (t[0] == estado_actual and t[1] == simbolo_actual) and t[2] == pila[0]), None)
        print("Transicion encontrada: ", resultado, "\n")
        if not resultado:
            print(f"Error: No hay transicion '{simbolo_actual}'")
            break
         
        estado_actual = resultado[3]
        if len(resultado[4]) > 1:
            for j in range(len(resultado[4])-2, -1, -1):
                pila.appendleft(resultado[4][j])
        elif resultado[4] == '-':
            pila.popleft()
            
                        
    if str(estado_actual) == estado_final:
        print("Cadena aceptada por estado final")
    elif not estado_final and not pila:
        print("Cadena aceptada por stack vacio")
    

transiciones = []

ventana = tk.Tk()
ventana.title("Simulador APD")
ventana.geometry("800x600")
ventana.resizable(False, False)

frame_sup = tk.Frame(ventana, bg="#fcf6d2", height=400, width=800)
frame_sup.place(x=0, y=0)
frame_inf = tk.Frame(ventana, bg="#f5cf9f", height=200, width=800)
frame_inf.place(x=0, y=400)

fuente1 = tkFont.Font(family="Verdana", size=11)
fuente2 = tkFont.Font(family="Consolas", size=12, weight="bold")
fuente3 = tkFont.Font(family="Consolas", size=12)
fuente4 = tkFont.Font(family="Consolas", size=16, weight="bold")
fuente5 = tkFont.Font(family="Verdana", size=10)

label_paso1 = tk.Label(frame_sup, text="Paso 1", font=fuente4, bg="#fcf6d2")
label_paso1.place(x=10, y=20)
label_paso2 = tk.Label(frame_inf, text="Paso 2", font=fuente4, bg="#f5cf9f")
label_paso2.place(x=10, y=10)

label_inst1 = tk.Label(frame_sup, text="Ingrese las transiciones del APD una por una", font=fuente5, bg="#fcf6d2")
label_inst1.place(x=10, y=45)
label_inst2 = tk.Label(frame_sup, text="(Para ingresar ε, escriba '-')", font=fuente5, bg="#fcf6d2")
label_inst2.place(x=10, y=65)
label_inst3 = tk.Label(frame_inf, text="Indique las siguientes caracteristicas de su APD", font=fuente5, bg="#f5cf9f")
label_inst3.place(x=10, y=35)



label1 = tk.Label(frame_sup, text="Estado actual", font=fuente1, bg="#fcf6d2")
label1.place(x=10, y=140)
labelq1 = tk.Label(frame_sup, text="q", font=fuente4, bg="#fcf6d2")
labelq1.place(x=133, y=135)
entry1 = tk.Entry(frame_sup, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry1.place(x=150, y=140)

label2 = tk.Label(frame_sup, text="Simbolo a leer", font=fuente1, bg="#fcf6d2")
label2.place(x=10, y=180)
entry2 = tk.Entry(frame_sup, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry2.place(x=150, y=180)

label3 = tk.Label(frame_sup, text="Tope de stack", font=fuente1, bg="#fcf6d2")
label3.place(x=10, y=220)
entry3 = tk.Entry(frame_sup, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry3.place(x=150, y=220)

imagen = tk.PhotoImage(file="flecha.png")
label_flecha = tk.Label(ventana, image=imagen, bg="#fcf6d2")
label_flecha.place(x=210, y=165)

label4 = tk.Label(frame_sup, text="Nuevo estado", font=fuente1, bg="#fcf6d2")
label4.place(x=290, y=160)
labelq2 = tk.Label(frame_sup, text="q", font=fuente4, bg="#fcf6d2")
labelq2.place(x=423, y=155)
entry4 = tk.Entry(frame_sup, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry4.place(x=440, y=160)

label5 = tk.Label(frame_sup, text="Actualizar stack", font=fuente1, bg="#fcf6d2")
label5.place(x=290, y=200)
entry5 = tk.Entry(frame_sup, width=6, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry5.place(x=440, y=200)

boton_agregar = tk.Button(frame_sup, text="Agregar transicion", command=recoger_entrada, font=fuente1, relief=tk.SOLID, borderwidth=2, bg="#f5cf9f")
boton_agregar.place(x=180, y=280)

boton_editar = tk.Button(frame_sup, text="Editar transicion", command=menu_editar, font=fuente1, relief=tk.SOLID, borderwidth=2, bg="#f5cf9f")
boton_editar.place(x=520, y=350)

boton_borrar = tk.Button(frame_sup, text="Borrar todo", command=borrar, font=fuente1, relief=tk.SOLID, borderwidth=2, bg="#f5cf9f")
boton_borrar.place(x=675, y=350)

label_transiciones = tk.Label(frame_sup, text="Transiciones ingresadas", font=fuente1, bg="#fcf6d2")
label_transiciones.place(x=510, y=25)
lista_transiciones = tk.Text(frame_sup, height=15, width=28, font=fuente2, relief=tk.SOLID, borderwidth=2)
lista_transiciones.place(x=520, y=50)
lista_transiciones.config(state="disabled")


label6 = tk.Label(frame_inf, text="Estado inicial", font=fuente1, bg="#f5cf9f")
label6.place(x=10, y=80)
labelq6 = tk.Label(frame_inf, text="q", font=fuente4, bg="#f5cf9f")
labelq6.place(x=133, y=75)
entry6 = tk.Entry(frame_inf, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry6.place(x=150, y=80)

label7 = tk.Label(frame_inf, text="Estado final", font=fuente1, bg="#f5cf9f")
label7.place(x=10, y=160)
labelq7 = tk.Label(frame_inf, text="q", font=fuente4, bg="#f5cf9f")
labelq7.place(x=133, y=155)
entry7 = tk.Entry(frame_inf, width=3, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry7.place(x=150, y=160)

label_palabra = tk.Label(frame_inf, text="Ingrese una palabra", font=fuente1, bg="#f5cf9f")
label_palabra.place(x=550, y=40)
entry_palabra = tk.Entry(frame_inf, width=30, font=fuente3, relief=tk.SOLID, borderwidth=2)
entry_palabra.place(x=485, y=80)

label_radio = tk.Label(frame_inf, text="El APD acepta por", font=fuente1, bg="#f5cf9f")
label_radio.place(x=10, y=130)

opcion_final = tk.StringVar(value="stack")
radio1 = tk.Radiobutton(frame_inf, text="Stack vacio", variable=opcion_final, value="stack", font=fuente1, bg="#f5cf9f", command=ocultar)
radio1.place(x=160, y=130)
radio2 = tk.Radiobutton(frame_inf, text="Estado final", variable=opcion_final, value="estado", font=fuente1, bg="#f5cf9f", command=ocultar)
radio2.place(x=280, y=130)

frame_ocultar = tk.Frame(frame_inf, bg="#f5cf9f", height=30, width=200)
frame_ocultar.place(x=8, y=155)

boton_verificar = tk.Button(frame_inf, text="Verificar palabra", font=fuente1, relief=tk.SOLID, borderwidth=2, bg="#fcf6d2", command=validar_palabra)
boton_verificar.place(x=560, y=150)
    
ventana.mainloop()





        
