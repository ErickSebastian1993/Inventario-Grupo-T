import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Inventario.db')
        #flash('Me conecté!',con)
        return con
    except Error:
        print(Error)

def consultar_producto(nombre):
    query = "SELECT * FROM Producto WHERE nombre = '"+nombre+"';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    producto = cursorObj.fetchall()
    con.close()
    return producto

def get_productos():
    query = "SELECT * FROM Producto;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    productos = cursorObj.fetchall()
    con.close()
    return productos

def insertar_producto(referencia,nombre,precio,cantidad,estado,imagen):
    query = "INSERT INTO Producto (referencia,nombre,precio,cantidad,estado,imagen) values('"+referencia+"','"+nombre+"','"+str(precio)+"', '"+str(cantidad)+"','"+estado+"','"+imagen+"');"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    con.close()

def actualizar_producto(referencia,nombre,precio,cantidad,imagen):
    query = "UPDATE Producto SET referencia = '"+referencia+"', nombre = '"+nombre+"', precio = '"+str(precio)+"', cantidad = '"+str(cantidad)+"', imagen = '"+imagen+"' WHERE referencia = '"+referencia+"';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    con.close()    

#def inactivar_producto(referencia):

def insertar_usuario(nombre,correo,usuario,password,rol):
    query = "INSERT INTO USUARIO (nombre,correo,usuario,password,rol) values('"+nombre+"', '"+correo+"','"+usuario+"','"+password+"','"+rol+"');"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    con.close()

def validar_sesion(usuario,contraseña):
    query = "SELECT usuario,contraseña FROM Usuario WHERE usuario = "+usuario+" AND password = "+password+";"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    usuario = cursorObj.fetchall()
    con.close()
    return usuario