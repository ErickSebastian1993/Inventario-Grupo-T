import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Inventario.db')
        return con
    except Error:
        print(Error)

def consultar_producto(nombre):
    query = "SELECT * FROM Producto WHERE nombre = ?;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(query,(nombre))
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
    tprecio=str(precio)
    tcantidad=str(cantidad)
    if imagen.filename=='':
        query = "UPDATE Producto SET referencia = ?, nombre = ?, precio = ?, cantidad = ? WHERE referencia = ?;"  
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(query,(referencia,nombre,tprecio,tcantidad,referencia))
        con.commit()
        con.close()   
    else:
        resimagen='../static/img/'+imagen.filename
        query = "UPDATE Producto SET referencia = ?, nombre = ?, precio = ?, cantidad = ?, imagen = ? WHERE referencia = ?;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(query,(referencia,nombre,tprecio,tcantidad,resimagen,referencia))
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