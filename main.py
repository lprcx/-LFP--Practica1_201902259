from cgitb import text
from faulthandler import disable
from glob import glob
from operator import truediv
import os
from pyexpat.errors import messages
from sre_parse import State
import tkinter as tk
from tkinter import Label, Button, Entry
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import NO
from logging import root
from tkinter import filedialog
from curso import Curso
from PIL import ImageTk, Image

cursos = []

def gestionarr():
    principal.destroy()
    gestion()

def cargar():
    principal.destroy()
    selectar()

def salir():
    principal.destroy() 

def agregarc():
    gestionar.destroy()
    agregarcurso()

def elic():
    gestionar.destroy()
    eliminar()

def conteoc():
    principal.destroy()
    cc()

def mosc():
    gestionar.destroy()
    mostrarcurso()


principal = None
def main():
    global principal

    principal = tk.Tk()
    principal.title("Menú Principal")
    principal.geometry("600x500")
    principal.config(bg="#D4E6FF")
    principal.resizable(0,0)

    #label
    tit1 = Label(principal, text="Nombre del curso: Lab. Lenguajes Formales y Programación A-", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=20,y=40)
    tit2 = Label(principal, text="Nombre del estudiante: Lourdes Patricia Reyes Castillo", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit2.place(x=20,y=80)
    tit3 = Label(principal, text="Carnet del estudiante: 201902259", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit3.place(x=20,y=120)


    #botones
    bot1 = Button(principal, text="Cargar Archivo", font="Arial 12", bg="#FFD8D4", command=cargar)
    bot1.place(x=230, y= 200)
    bot2 = Button(principal, text="Gestionar Cursos", font="Arial 12", bg="#FFD4E6", command=gestionarr)
    bot2.place(x=220, y= 250)
    bot3 = Button(principal, text="Conteo de Créditos", font="Arial 12", bg="#FFD8D4", command=conteoc)
    bot3.place(x=213, y= 300)
    bot4 = Button(principal, text="Salir", font="Arial 12", bg="#FFD4E6", command=salir)
    bot4.place(x=255, y= 350)


    principal.mainloop()


selecar=None
def regresar():
    global selecar
    selecar.destroy()
    main()
#leer archivo
def leerarchivo(contenido):
    global cursos
    contenido1=contenido.split('\n')
    for linea in contenido1:
        if linea != "":
            contenido2=linea.split(",")
            if verificarcurso(contenido2[0])==False:
                nuevo = Curso(contenido2[0], contenido2[1], contenido2[2], contenido2[3], contenido2[4], contenido2[5], contenido2[6])
                cursos.append(nuevo)
    messagebox.showinfo("Cargado!", "Cargado con exito")

def verificarcurso(codigo):
    global cursos
    for c in cursos:
        if c.codigo==codigo:
            return True
    return False




#función para cargar un archivo
def Carga():
    root = tk.Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title="Carga de", filetypes=(("Text files", "*.lfp*"), ("all files", "*.*")))
    if ruta!= "":
        archivo = open(ruta, 'r', encoding='utf-8')
        contenido = archivo.read()
        leerarchivo(contenido)
    else:
        messagebox.showinfo("Error", "Seleccione un archivo")




def selectar():
    global selecar
    selecar = tk.Tk()
    selecar.title("Seleccionar Archivo")
    selecar.geometry("500x200")
    selecar.config(bg="#D4E6FF")
    selecar.resizable(0,0)

    #label
    tit1 = Label(selecar, text="Ruta:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=50,y=60)

    #textbook
    cuad = Entry(selecar)
    cuad.place(x=100, y=60, width=300, height=20)

    #botones

    bot1 = Button(selecar, text="Seleccionar", font="Arial 12", bg="#FFD8D4", command=Carga)
    bot1.place(x=100, y= 140)
    bot2 = Button(selecar, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar)
    bot2.place(x=300, y= 140)



    selecar.mainloop()

listarc=None

#función para agregar un curso
def agregar_curso(codigo, nombre, prerrequisitos, semestre, opcionalidad, creditos, estado):
    global cursos
    if codigo != "" and nombre!= "" and semestre!="" and opcionalidad!="" and creditos!="" and estado!="":
        if (verificarcurso(codigo)==False):
            nuevo = Curso(codigo, nombre, prerrequisitos, opcionalidad, semestre, creditos, estado)
            cursos.append(nuevo)
            messagebox.showinfo("Agregado!", "Curso agregado con éxito")
        else:
            messagebox.showinfo("Error", "El curso ya existe en la lista")
    else:
        messagebox.showinfo("Error", "Llene todos los campos requeridos")


def editar_curso(codigo, nombre, prerrequisitos, semestre, opcionalidad, creditos, estado):
    global cursos
    if codigo != "" and nombre!= "" and semestre!="" and opcionalidad!="" and creditos!="" and estado!="":
        if (verificarcurso(codigo)==True):
            for c in cursos:
                if c.codigo==codigo:
                    c.nombre=nombre
                    c.prerrequisistos=prerrequisitos
                    c.semestre=semestre
                    c.opcionalidad=opcionalidad
                    c.creditos=creditos
                    c.estado=estado
            messagebox.showinfo("Actualizado!", "Curso actualizado con éxito")
        else:
            messagebox.showinfo("Error", "El curso no se encuentra en la lista")
    else:
        messagebox.showinfo("Error", "Llene todos los campos requeridos")


def eliminar_curso(codigo):
    global cursos
    if codigo != "":
        if verificarcurso(codigo)==True:
            for i in range(len(cursos)):
                if codigo == cursos[i].codigo:
                    cursos.remove(cursos[i])
                    messagebox.showinfo("Eliminado!", "Curso eliminado con éxito")
        else:
            messagebox.showinfo("Error", "El curso no se encuentra en la lista")
    else:
        messagebox.showinfo("Error", "Llene todos los campos requeridos")






def regresar1():
    global listarc
    listarc.destroy()
    gestion()


def listar():
    global listarc
    global cursos
    listarc = tk.Tk()
    listarc.title("Listar Cursos")
    listarc.geometry("800x600")
    listarc.config(bg="#D4E6FF")
    listarc.resizable(0,0)
    
    #tabla
    tabla = ttk.Treeview(listarc, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show="headings")
    tabla.heading("#1", text="Codigo")
    tabla.heading("#2", text="Nombre")
    tabla.heading("#3", text="Pre Requisito")
    tabla.heading("#4", text="Opcionalidad")
    tabla.heading("#5", text="Semestre")
    tabla.heading("#6", text="Créditos")
    tabla.heading("#7", text="Estado")
    tabla.column("#1", width=50)
    tabla.column("#2", width=200)
    tabla.column("#3", width=90)
    tabla.column("#4", width=90)
    tabla.column("#5", width=90)
    tabla.column("#6", width=90)
    tabla.column("#7", width=90)
    lista = []
    for c in cursos:
        lista.append((c.codigo,c.nombre,c.prerrequisitos,c.opcionalidad,c.semestre,c.creditos,c.estado))
    for num in lista:
        tabla.insert("", tk.END, values=num)
    tabla.grid(row=0, column=0, sticky="nsnew")
    scroll = ttk.Scrollbar(listarc, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scroll.set)
    scroll.grid(row=0, column=1, sticky="ns", pady=8)
    tabla.place(x=20, y=20)
    scroll.place(x=0,y=20)
    
    

    #botones

    bot1 = Button(listarc, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar1)
    bot1.place(x=450, y= 500)


    listarc.mainloop()



gestionar = None

def regresar2():
    global gestionar
    gestionar.destroy()
    main()

def lc():
    global gestionar
    gestionar.destroy()
    listar()

def ec():
    global gestionar
    gestionar.destroy()
    editarcurso()

def gestion():
    global gestionar

    gestionar = tk.Tk()
    gestionar.title("Menú Principal")
    gestionar.geometry("400x450")
    gestionar.config(bg="#D4E6FF")
    gestionar.resizable(0,0)
    

    #botones
    bot1 = Button(gestionar, text="Listar Cursos", font="Arial 12", bg="#FFD8D4", command=lc)
    bot1.place(x=150, y= 100)
    bot2 = Button(gestionar, text="Agregar Curso", font="Arial 12", bg="#FFD4E6", command=agregarc)
    bot2.place(x=150, y= 150)
    bot3 = Button(gestionar, text="Editar Curso", font="Arial 12", bg="#FFD8D4", command=ec)
    bot3.place(x=150, y= 200)
    bot4 = Button(gestionar, text="Eliminar Curso", font="Arial 12", bg="#FFD4E6", command=elic)
    bot4.place(x=150, y= 250)
    bot5 = Button(gestionar, text="Mostrar Curso", font="Arial 12", bg="#FFD8D4", command=mosc)
    bot5.place(x=150, y= 300)
    bot6 = Button(gestionar, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar2)
    bot6.place(x=150, y= 350)


    gestionar.mainloop()


agcurso = None

def regresar3():
    global agcurso
    agcurso.destroy()
    gestion()

def agregarcurso():
    global agcurso
    agcurso = tk.Tk()
    agcurso.title("Seleccionar Archivo")
    agcurso.geometry("500x550")
    agcurso.config(bg="#D4E6FF")
    agcurso.resizable(0,0)

    #label
    tit1 = Label(agcurso, text="Código", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=50,y=60)
    tit2 = Label(agcurso, text="Nombre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit2.place(x=50,y=110)
    tit3 = Label(agcurso, text="Pre Requisito", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit3.place(x=50,y=160)
    tit4 = Label(agcurso, text="Semestre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit4.place(x=50,y=210)
    tit5 = Label(agcurso, text="Opcionalidad", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit5.place(x=50,y=260)
    tit6 = Label(agcurso, text="Créditos", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit6.place(x=50,y=310)
    tit7 = Label(agcurso, text="Estado", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit7.place(x=50,y=360)

    #textbox
    cuad1 = Entry(agcurso)
    cuad1.place(x=200, y=60, width=200, height=20)
    cuad2 = Entry(agcurso)
    cuad2.place(x=200, y=110, width=200, height=20)
    cuad3 = Entry(agcurso)
    cuad3.place(x=200, y=160, width=200, height=20)
    cuad4 = Entry(agcurso)
    cuad4.place(x=200, y=210, width=200, height=20)
    cuad5 = Entry(agcurso)
    cuad5.place(x=200, y=260, width=200, height=20)
    cuad6 = Entry(agcurso)
    cuad6.place(x=200, y=310, width=200, height=20)
    cuad7 = Entry(agcurso)
    cuad7.place(x=200, y=360, width=200, height=20)

    #botones

    bot1 = Button(agcurso, text="Agregar", font="Arial 12", bg="#FFD8D4", command=lambda:agregar_curso(cuad1.get(), cuad2.get(), cuad3.get(), cuad4.get(), cuad5.get(), cuad6.get(), cuad7.get()))
    bot1.place(x=100, y= 460)
    bot2 = Button(agcurso, text="Regresar", font="Arial 12", bg="#FFD4E6", command=regresar3)
    bot2.place(x=300, y= 460)



    agcurso.mainloop()

editcurso = None


moscurso=None

def mostrarcurso():
    global moscurso
    moscurso = tk.Tk()
    moscurso.title("Mostrar Curso")
    moscurso.geometry("500x550")
    moscurso.config(bg="#D4E6FF")
    moscurso.resizable(0,0)

    #label
    tit1 = Label(moscurso, text="Código", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=50,y=60)
    tit2 = Label(moscurso, text="Nombre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit2.place(x=50,y=110)
    tit3 = Label(moscurso, text="Pre Requisito", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit3.place(x=50,y=160)
    tit4 = Label(moscurso, text="Semestre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit4.place(x=50,y=210)
    tit5 = Label(moscurso, text="Opcionalidad", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit5.place(x=50,y=260)
    tit6 = Label(moscurso, text="Créditos", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit6.place(x=50,y=310)
    tit7 = Label(moscurso, text="Estado", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit7.place(x=50,y=360)

    #textbox
    cuad1 = Entry(moscurso)
    cuad1.place(x=200, y=60, width=200, height=20)
    cuad2 = Entry(moscurso, state="disable")
    cuad2.place(x=200, y=110, width=200, height=20)
    cuad3 = Entry(moscurso, state="disable")
    cuad3.place(x=200, y=160, width=200, height=20)
    cuad4 = Entry(moscurso, state="disable")
    cuad4.place(x=200, y=210, width=200, height=20)
    cuad5 = Entry(moscurso, state="disable")
    cuad5.place(x=200, y=260, width=200, height=20)
    cuad6 = Entry(moscurso, state="disable")
    cuad6.place(x=200, y=310, width=200, height=20)
    cuad7 = Entry(moscurso, state="disable")
    cuad7.place(x=200, y=360, width=200, height=20)

    #botones

    bot1 = Button(moscurso, text="Mostrar", font="Arial 12", bg="#FFD8D4", command=lambda:mostrar_curso(cuad1.get(), cuad2, cuad3, cuad4, cuad5, cuad6, cuad7))
    bot1.place(x=100, y= 460)
    bot2 = Button(moscurso, text="Regresar", font="Arial 12", bg="#FFD4E6", command=regresar7)
    bot2.place(x=300, y= 460)



    moscurso.mainloop()

#función para mostrar cursos
def mostrar_curso(codigo, nombre, prerrequisitos, semestre, opcionalidad, creditos, estado):
    global cursos
    if codigo != "":
        if verificarcurso(codigo)==True:
            for c in cursos:
                if codigo == c.codigo:
                    nombre["state"]="normal"
                    nombre.delete(0,"end")
                    nombre.insert(0, c.nombre)
                    nombre["state"]="disable"
                    
                    prerrequisitos["state"]="normal"
                    prerrequisitos.delete(0,"end")
                    prerrequisitos.insert(0, c.prerrequisitos)
                    prerrequisitos["state"]="disable"

                    semestre["state"]="normal"
                    semestre.delete(0,"end")
                    semestre.insert(0, c.semestre)
                    semestre["state"]="disable"

                    opcionalidad["state"]="normal"
                    opcionalidad.delete(0,"end")
                    opcionalidad.insert(0, c.opcionalidad)
                    opcionalidad["state"]="disable"

                    creditos["state"]="normal"
                    creditos.delete(0,"end")
                    creditos.insert(0, c.creditos)
                    creditos["state"]="disable"

                    estado["state"]="normal"
                    estado.delete(0,"end")
                    estado.insert(0, c.estado)
                    estado["state"]="disable"
        else:
            messagebox.showinfo("Error", "El curso no se encuentra en la lista")
    else:
        messagebox.showinfo("Error", "Llene todos los campos requeridos")

    
def regresar7():
    global moscurso
    moscurso.destroy()
    gestion()



def regresar4():
    global editcurso
    editcurso.destroy()
    gestion()

def editarcurso():
    global editcurso
    editcurso = tk.Tk()
    editcurso.title("Editar Curso")
    editcurso.geometry("500x550")
    editcurso.config(bg="#D4E6FF")
    editcurso.resizable(0,0)

    #label
    tit1 = Label(editcurso, text="Código", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=50,y=60)
    tit2 = Label(editcurso, text="Nombre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit2.place(x=50,y=110)
    tit3 = Label(editcurso, text="Pre Requisito", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit3.place(x=50,y=160)
    tit4 = Label(editcurso, text="Semestre", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit4.place(x=50,y=210)
    tit5 = Label(editcurso, text="Opcionalidad", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit5.place(x=50,y=260)
    tit6 = Label(editcurso, text="Créditos", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit6.place(x=50,y=310)
    tit7 = Label(editcurso, text="Estado", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit7.place(x=50,y=360)

    #textbox
    cuad1 = Entry(agcurso)
    cuad1.place(x=200, y=60, width=200, height=20)
    cuad2 = Entry(agcurso)
    cuad2.place(x=200, y=110, width=200, height=20)
    cuad3 = Entry(agcurso)
    cuad3.place(x=200, y=160, width=200, height=20)
    cuad4 = Entry(agcurso)
    cuad4.place(x=200, y=210, width=200, height=20)
    cuad5 = Entry(agcurso)
    cuad5.place(x=200, y=260, width=200, height=20)
    cuad6 = Entry(agcurso)
    cuad6.place(x=200, y=310, width=200, height=20)
    cuad7 = Entry(agcurso)
    cuad7.place(x=200, y=360, width=200, height=20)

    #botones

    bot1 = Button(agcurso, text="Actualizar", font="Arial 12", bg="#FFD8D4", command=lambda:editar_curso(cuad1.get(), cuad2.get(), cuad3.get(), cuad4.get(), cuad5.get(), cuad6.get(), cuad7.get()))
    bot1.place(x=100, y= 460)
    bot2 = Button(agcurso, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar4)
    bot2.place(x=300, y= 460)



    agcurso.mainloop()

eliminarc = None

def regresar5():
    global eliminarc
    eliminarc.destroy()
    gestion()


def eliminar():
    global eliminarc
    eliminarc = tk.Tk()
    eliminarc.title("Seleccionar Archivo")
    eliminarc.geometry("500x200")
    eliminarc.config(bg="#D4E6FF")
    eliminarc.resizable(0,0)

    #label
    tit1 = Label(eliminarc, text="Codigo del Curso:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=30,y=60)

    #textbox
    cuad = Entry(eliminarc)
    cuad.place(x=180, y=60, width=250, height=20)

    #botones

    bot1 = Button(eliminarc, text="Eliminar", font="Arial 12", bg="#FFD8D4", command=lambda: eliminar_curso(cuad.get()))
    bot1.place(x=100, y= 140)
    bot2 = Button(eliminarc, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar5)
    bot2.place(x=300, y= 140)



    eliminarc.mainloop()

conteo = None

def regresar6():
    global conteo
    conteo.destroy()
    main()

def cc():
    global conteo

    conteo = tk.Tk()
    conteo.title("Menú Principal")
    conteo.geometry("600x500")
    conteo.config(bg="#D4E6FF")
    conteo.resizable(0,0)

    #label
    tit1 = Label(conteo, text="Créditos aprobados: ", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit1.place(x=20,y=20)
    tit2 = Label(conteo, text="Créditos cursando: ", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit2.place(x=20,y=60)
    tit3 = Label(conteo, text="Créditos pendientes: ", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit3.place(x=20,y=100)
    tit4 = Label(conteo, text="Créditos obligatorios hasta semestre N:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit4.place(x=20,y=140)
    tit5 = Label(conteo, text="Semestre:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit5.place(x=20,y=180)
    tit6 = Label(conteo, text="Créditos del Semestre:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit6.place(x=20,y=220)
    tit7 = Label(conteo, text="Semestre:", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit7.place(x=20,y=260)
    tit8 = Label(conteo, text="0", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit8.place(x=200,y=20)
    tit9 = Label(conteo, text="0", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit9.place(x=200,y=60)
    tit10 = Label(conteo, text="0", font="Arial 12 bold", fg="black", bg="#D4E6FF")
    tit10.place(x=200,y=100)
    tit11 = Label(conteo, text="Créditos aprobados: ", font="Arial 12", fg="black", bg="#D4E6FF")
    tit11.place(x=20,y=300)
    tit12 = Label(conteo, text="Créditos cursando: ", font="Arial 12", fg="black", bg="#D4E6FF")
    tit12.place(x=20,y=350)
    tit13 = Label(conteo, text="Créditos pendientes: ", font="Arial 12", fg="black", bg="#D4E6FF")
    tit13.place(x=20,y=400)

    contarcreditos(tit8,tit9,tit10)
    

    #textbox
    cuad = Entry(conteo, state="disable")
    cuad.place(x=350, y=140, width=50, height=20)

    cuad1 = ttk.Spinbox(conteo, from_= 1, to=10)
    cuad1.place(x=100, y=180, width=50)

    cuad3 = ttk.Spinbox(conteo, from_= 1, to=10)
    cuad3.place(x=100, y=260, width=50)

    

    #botones
    bot1 = Button(conteo, text="Contar", font="Arial 12", bg="#FFD8D4", command=lambda:contarcred_semestre(cuad1.get(), cuad))
    bot1.place(x=200, y= 180)
    bot2 = Button(conteo, text="Contar", font="Arial 12", bg="#FFD4E6", command=lambda: contar_semestre(cuad3.get(), tit11, tit12, tit13))
    bot2.place(x=200, y= 260)
    bot3 = Button(conteo, text="Regresar", font="Arial 12", bg="#FFD8D4", command=regresar6)
    bot3.place(x=300, y=450)


    conteo.mainloop()



def contarcreditos(label1, label2, label3):
    global cursos
    contador_aprobados = 0
    contador_pendientes = 0
    contador_cursando = 0
    for c in cursos:
        if c.estado == "0":
            contador_aprobados+=int(c.creditos)
        elif c.estado == "1":
            contador_cursando+=int(c.creditos)
        elif c.estado == "-1":
            contador_pendientes+=int(c.creditos)
    label1.config(text=str(contador_aprobados))
    label2.config(text=str(contador_cursando))
    label3.config(text=str(contador_pendientes))


#contar creditos hasta semestre N
def contarcred_semestre(semestre, textbox):
    global cursos
    if semestre!="":
        contador_creditos = 0
        for c in cursos:
            contador_semestre = 1
            if c.opcionalidad == "1":
                for i in range(contador_semestre, int(semestre)+1):
                    if int(c.semestre)== i:
                        contador_creditos+=int(c.creditos)

        textbox["state"]="normal"
        textbox.delete(0,"end")
        textbox.insert(0, str(contador_creditos))
        textbox["state"]="disable"
    else:
        messagebox.showinfo("Error", "Seleccione el número de semestre")

#contar creditos del semestre seleccionado
def contar_semestre(semestre, label1, label2, label3):
    contador_aprobados = 0
    contador_pendientes = 0
    contador_cursando = 0
    global cursos
    if semestre!="":
        for c in cursos:
            if c.estado == "0" and c.semestre==semestre:
                contador_aprobados+=int(c.creditos)
            elif c.estado == "1" and c.semestre==semestre:
                contador_cursando+=int(c.creditos)
            elif c.estado == "-1" and c.semestre==semestre:
                contador_pendientes+=int(c.creditos)
        label1.config(text="Creditos aprobados: "+str(contador_aprobados))
        label2.config(text="Creditos cursando: "+str(contador_cursando))
        label3.config(text="Creditos pendientes: "+str(contador_pendientes))
    else:
        messagebox.showinfo("Error", "Seleccione el número de semestre")


main()
