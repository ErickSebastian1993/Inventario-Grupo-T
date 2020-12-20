import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Inventario.db')
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
    resimagen='../static/img/'+imagen.filename
    query = "INSERT INTO Producto (referencia,nombre,precio,cantidad,estado,imagen) values(?,?,?,?,?,?)" 
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query,(referencia,nombre,precio,cantidad,estado,resimagen))
    con.commit()
    con.close()

def actualizar_producto(referencia,nombre,precio,cantidad,imagen):
    query = "UPDATE Producto SET referencia = '"+referencia+"', nombre = '"+nombre+"', precio = '"+str(precio)+"', cantidad = '"+str(cantidad)+"', imagen = '"+imagen+"' WHERE referencia = '"+referencia+"';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query)
    con.commit()
    con.close()    

def insertar_usuario(nombre,correo,usuario,password,rol):
    query = "INSERT INTO USUARIO (nombre,correo,usuario,password,rol) values(?,?,?,?,?);"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query,(nombre,correo,usuario,password,rol))
    con.commit()
    con.close()

def validar_sesion(usuario,password):
    query = "SELECT * FROM Usuario WHERE usuario = ? AND password = ?;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query,(usuario,password))
    con.commit()
    usuario = cursorObj.fetchall()
    con.close()
    return usuario