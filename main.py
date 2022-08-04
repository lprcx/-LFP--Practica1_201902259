
import tkinter as tk
from tkinter import Label, Button, Entry
from tkinter import ttk
from tkinter.messagebox import NO

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


principal = None
def main():
    global principal

    principal = tk.Tk()
    principal.title("Menú Principal")
    principal.geometry("600x500")
    principal.config(bg="gray")
    principal.resizable(0,0)

    #label
    tit1 = Label(principal, text="Nombre del curso: Lab. Lenguajes Formales y Programación", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=20,y=20)
    tit2 = Label(principal, text="Nombre del estudiante: Lourdes Patricia Reyes Castillo", font="Arial 12 bold", fg="black", bg="gray")
    tit2.place(x=20,y=60)
    tit3 = Label(principal, text="Carnet del estudiante: 201902259", font="Arial 12 bold", fg="black", bg="gray")
    tit3.place(x=20,y=100)

    

    #botones
    bot1 = Button(principal, text="Cargar Archivo", font="Arial 12", bg="#B4A9B5", command=cargar)
    bot1.place(x=100, y= 150)
    bot2 = Button(principal, text="Gestionar Cursos", font="Arial 12", bg="#B4A9B5", command=gestionarr)
    bot2.place(x=100, y= 200)
    bot3 = Button(principal, text="Conteo de Créditos", font="Arial 12", bg="#B4A9B5", command=conteoc)
    bot3.place(x=100, y= 250)
    bot4 = Button(principal, text="Salir", font="Arial 12", bg="#B4A9B5", command=salir)
    bot4.place(x=100, y= 300)


    principal.mainloop()


selecar=None
def regresar():
    global selecar
    selecar.destroy()
    main()


def selectar():
    global selecar
    selecar = tk.Tk()
    selecar.title("Seleccionar Archivo")
    selecar.geometry("500x200")
    selecar.config(bg="gray")
    selecar.resizable(0,0)

    #label
    tit1 = Label(selecar, text="Ruta:", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=50,y=60)

    #textbook
    cuad = Entry(selecar)
    cuad.place(x=100, y=60, width=300, height=20)

    #botones

    bot1 = Button(selecar, text="Seleccionar", font="Arial 12", bg="#B4A9B5")
    bot1.place(x=100, y= 140)
    bot2 = Button(selecar, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar)
    bot2.place(x=300, y= 140)



    selecar.mainloop()

listarc=None

def regresar1():
    global listarc
    listarc.destroy()
    gestion()


def listar():
    global listarc
    listarc = tk.Tk()
    listarc.title("Listar Cursos")
    listarc.geometry("800x600")
    listarc.config(bg="gray")
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
    for i in range(1,5):
        lista.append((i,i,i,i,i,i,i))
    for num in lista:
        tabla.insert("", tk.END, values=num)
    tabla.grid(row=0, column=0, sticky="nsnew")
    scroll = ttk.Scrollbar(listarc, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scroll.set)
    scroll.grid(row=0, column=1, sticky="ns", pady=8)
    tabla.place(x=20, y=20)
    scroll.place(x=0,y=20)
    
    

    #botones

    bot1 = Button(listarc, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar1)
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
    gestionar.geometry("600x500")
    gestionar.config(bg="gray")
    gestionar.resizable(0,0)
    

    #botones
    bot1 = Button(gestionar, text="Listar Cursos", font="Arial 12", bg="#B4A9B5", command=lc)
    bot1.place(x=100, y= 150)
    bot2 = Button(gestionar, text="Agregar Curso", font="Arial 12", bg="#B4A9B5", command=agregarc)
    bot2.place(x=100, y= 200)
    bot3 = Button(gestionar, text="Editar Curso", font="Arial 12", bg="#B4A9B5", command=ec)
    bot3.place(x=100, y= 250)
    bot4 = Button(gestionar, text="Eliminar Curso", font="Arial 12", bg="#B4A9B5", command=elic)
    bot4.place(x=100, y= 300)
    bot5 = Button(gestionar, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar2)
    bot5.place(x=100, y= 350)


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
    agcurso.config(bg="gray")
    agcurso.resizable(0,0)

    #label
    tit1 = Label(agcurso, text="Código", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=50,y=60)
    tit2 = Label(agcurso, text="Nombre", font="Arial 12 bold", fg="black", bg="gray")
    tit2.place(x=50,y=110)
    tit3 = Label(agcurso, text="Pre Requisito", font="Arial 12 bold", fg="black", bg="gray")
    tit3.place(x=50,y=160)
    tit4 = Label(agcurso, text="Semestre", font="Arial 12 bold", fg="black", bg="gray")
    tit4.place(x=50,y=210)
    tit5 = Label(agcurso, text="Opcionalidad", font="Arial 12 bold", fg="black", bg="gray")
    tit5.place(x=50,y=260)
    tit6 = Label(agcurso, text="Créditos", font="Arial 12 bold", fg="black", bg="gray")
    tit6.place(x=50,y=310)
    tit7 = Label(agcurso, text="Estado", font="Arial 12 bold", fg="black", bg="gray")
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

    bot1 = Button(agcurso, text="Agregar", font="Arial 12", bg="#B4A9B5")
    bot1.place(x=100, y= 460)
    bot2 = Button(agcurso, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar3)
    bot2.place(x=300, y= 460)



    agcurso.mainloop()

editcurso = None

def regresar4():
    global editcurso
    editcurso.destroy()
    gestion()

def editarcurso():
    global editcurso
    editcurso = tk.Tk()
    editcurso.title("Seleccionar Archivo")
    editcurso.geometry("500x550")
    editcurso.config(bg="gray")
    editcurso.resizable(0,0)

    #label
    tit1 = Label(editcurso, text="Código", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=50,y=60)
    tit2 = Label(editcurso, text="Nombre", font="Arial 12 bold", fg="black", bg="gray")
    tit2.place(x=50,y=110)
    tit3 = Label(editcurso, text="Pre Requisito", font="Arial 12 bold", fg="black", bg="gray")
    tit3.place(x=50,y=160)
    tit4 = Label(editcurso, text="Semestre", font="Arial 12 bold", fg="black", bg="gray")
    tit4.place(x=50,y=210)
    tit5 = Label(editcurso, text="Opcionalidad", font="Arial 12 bold", fg="black", bg="gray")
    tit5.place(x=50,y=260)
    tit6 = Label(editcurso, text="Créditos", font="Arial 12 bold", fg="black", bg="gray")
    tit6.place(x=50,y=310)
    tit7 = Label(editcurso, text="Estado", font="Arial 12 bold", fg="black", bg="gray")
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

    bot1 = Button(agcurso, text="Agregar", font="Arial 12", bg="#B4A9B5")
    bot1.place(x=100, y= 460)
    bot2 = Button(agcurso, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar4)
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
    eliminarc.config(bg="gray")
    eliminarc.resizable(0,0)

    #label
    tit1 = Label(eliminarc, text="Codigo del Curso:", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=30,y=60)

    #textbox
    cuad = Entry(eliminarc)
    cuad.place(x=180, y=60, width=250, height=20)

    #botones

    bot1 = Button(eliminarc, text="Eliminar", font="Arial 12", bg="#B4A9B5")
    bot1.place(x=100, y= 140)
    bot2 = Button(eliminarc, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar5)
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
    conteo.config(bg="gray")
    conteo.resizable(0,0)

    #label
    tit1 = Label(conteo, text="Créditos aprobados: xx", font="Arial 12 bold", fg="black", bg="gray")
    tit1.place(x=20,y=20)
    tit2 = Label(conteo, text="Créditos cursando: xx", font="Arial 12 bold", fg="black", bg="gray")
    tit2.place(x=20,y=60)
    tit3 = Label(conteo, text="Créditos pendientes: xx", font="Arial 12 bold", fg="black", bg="gray")
    tit3.place(x=20,y=100)
    tit4 = Label(conteo, text="Créditos obligatorios hasta semestre N:", font="Arial 12 bold", fg="black", bg="gray")
    tit4.place(x=20,y=140)
    tit5 = Label(conteo, text="Semestre:", font="Arial 12 bold", fg="black", bg="gray")
    tit5.place(x=20,y=180)
    tit6 = Label(conteo, text="Créditos del Semestre:", font="Arial 12 bold", fg="black", bg="gray")
    tit6.place(x=20,y=220)
    tit7 = Label(conteo, text="Semestre:", font="Arial 12 bold", fg="black", bg="gray")
    tit7.place(x=20,y=260)

    #textbox
    cuad = Entry(conteo)
    cuad.place(x=250, y=140, width=50, height=20)

    cuad1 = ttk.Spinbox(conteo, from_= 1, to=10)
    cuad1.place(x=100, y=180, width=50)

    cuad2 = Entry(conteo)
    cuad2.place(x=250, y=220, width=50, height=20)

    cuad3 = ttk.Spinbox(conteo, from_= 1, to=10)
    cuad3.place(x=100, y=260, width=50)

    

    #botones
    bot1 = Button(conteo, text="Contar", font="Arial 12", bg="#B4A9B5", command=cargar)
    bot1.place(x=200, y= 180)
    bot2 = Button(conteo, text="Contar", font="Arial 12", bg="#B4A9B5", command=gestionarr)
    bot2.place(x=200, y= 260)
    bot3 = Button(conteo, text="Regresar", font="Arial 12", bg="#B4A9B5", command=regresar6)
    bot3.place(x=300, y=300)


    conteo.mainloop()


main()
