import sqlite3

conn = sqlite3.connect('web.db')
cursor = conn.cursor()


def crear_tablas():
    query = """
    CREATE TABLE  (
        id,
        nombre TEXT, 
        apellido TEXT, 
        telefono INT, 
        email TEXT,
        paquetes INT,
        logs TEXT,
        pagos TEXT);
    """
    cursor.execute(query)

def listar_paquetes():
    query = """
    SELECT id, nombre, apellido, telefono, email, logs, pagos FROM paquete;
    """
    cursor.execute(query)
    paquetes = cursor.fetchall()

def listar_logs():
    query = """
    SELECT id, nombre, apellido, telefono, email, paquetes, pagos FROM log;
    """
    cursor.execute(query)
    logs = cursor.fetchall()

def listar_pagos():
    query = """
    SELECT id, nombre, apellido, telefono, email, paquetes, logs FROM pago;
    """
    cursor.execute(query)
    pagos = cursor.fetchall()

def crear_paquete(nombre, apellido, telefono, email, pagos):
    query = """
    INSERT INTO paquete (nombre, apellido, telefono, email, pagos) value (?, ?, ?)
    """
    cursor.execute(query, (nombre, apellido, telefono, email, pagos))
    guardar_cambios()
    
def crear_paquete(id):
    query = """
    DELETE from paquete where id = ?
    """
    cursor.execute(query, (id,))
    guardar_cambios()


    
def guardar_cambios():
    conn.commit()


cursor.close()
conn.close()



