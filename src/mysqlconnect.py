#Ejecutar este script para crear la Base de datos

import mysql.connector

#Coneccion al server de la BD
conn = mysql.connector.connect(host="localhost",
                                user = "root",
                                passwd = "root")
#Crear el cursor
cursor = conn.cursor()

#Crear la base de datos para los usuarios
sql = "CREATE DATABASE login"
cursor.execute(sql)

#Actibar BD para crear la tabla
sql = "USE login"
cursor.execute(sql)

#Crear la tabla que almacenar usuario, mail y password
sql = """CREATE TABLE Users (
                id int(10) PRIMARY KEY AUTO_INCREMENT,
                email varchar(50),
                username varchar(30),
                passwd varchar(30)
    )"""
cursor.execute(sql)