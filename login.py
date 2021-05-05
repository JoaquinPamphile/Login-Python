import os
import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector

#INTERFAZ GRAFICA
def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenido!")
    #icono: pantalla.iconbitmap("url") tiene que ser extension .ico
    image=PhotoImage(file="usuario2.gif")
    image=image.subsample(1,1)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sistema", bg="slateblue1", fg="white", width="250", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", bg="deep sky blue", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Registrarse", bg="light grey", height="3", width="30", command=registrarse).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla) #sale despues de la pantalla de menu
    pantalla1.geometry("350x250")
    pantalla1.title("Inicio de Sesión")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña a continuación", width="250", bg="slateblue1", fg="white").pack()
    Label(pantalla1, text="")

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = StringVar()
    contrasenausuario_verify = StringVar()

    global nombre_usuario_entry
    global contrasenia_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenia_usuario_entry = Entry(pantalla1, show="*",textvariable=contrasenausuario_verify)
    contrasenia_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", bg="deep sky blue", command=validar_inicio_sesion_mysql).pack()


def registrarse():
    global pantalla2
    pantalla2 = Toplevel(pantalla) #sale despues de la pantalla de menu
    pantalla2.geometry("300x350")
    pantalla2.title("Registrarse")

    Label(pantalla2, text="Por favor complete la siguiente información", width="250", bg="slateblue1", fg="white").pack()
    Label(pantalla2, text="")

    global nombreusuario_entry
    global contrasena_entry
    global emailusuario_entry
    global contrasenarepe_entry

    emailusuario_entry = StringVar()
    contrasenarepe_entry = StringVar()
    nombreusuario_entry = StringVar()
    contrasena_entry = StringVar()

    Label(pantalla2, text="Email").pack()
    emailusuario_entry = Entry(pantalla2)
    emailusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Nombre de usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Repita contraseña").pack()
    contrasenarepe_entry = Entry(pantalla2, show="*")
    contrasenarepe_entry.pack()
    Label(pantalla2).pack()


    Button(pantalla2, text="Registrase", bg="deep sky blue",command=insertar_datos_mysql).pack()

def insertar_datos_mysql():
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='login'
    )
    cursor=conexion.cursor()
    sql= 'insert into Users (email, username, passwd) values (%s, %s, %s)'
    values=(emailusuario_entry.get(), nombreusuario_entry.get(), contrasena_entry.get())
    try:
        cursor.execute("select username from Users where username='"+nombreusuario_entry.get()+"'")
        if cursor.fetchall():
            messagebox.showinfo(message="El usuario ya está registrado en el sistema.", title="Aviso")
        else:
            if contrasena_entry.get() == contrasenarepe_entry.get():
                cursor.execute(sql, values)
                conexion.commit()
                messagebox.showinfo(message="Registro exitoso!", title="Aviso")
            else:
                messagebox.showinfo(message="Las contraseñas no coinciden", title="Aviso")

    except:
        conexion.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")
    conexion.close()

def validar_inicio_sesion_mysql():
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='login'
    )
    cursor=conexion.cursor()
    cursor.execute("select passwd from Users where username='"+nombreusuario_verify.get()+"' and passwd='"+contrasenausuario_verify.get()+"'")
    if cursor.fetchall():
        messagebox.showinfo(title="Inicio de sesión correcto", message="Usuario y Contraseña correctos")
    else:
        messagebox.showinfo(title="Inicio de sesión incorrecto", message="Usuario y Contraseña incorrectos")
    conexion.close()


menu_pantalla()
