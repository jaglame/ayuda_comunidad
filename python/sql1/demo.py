
import sqlite3
sqlite3.paramstyle = "named"  # Para pasar los parámetros como diccionario.

def get_connection():
    """ """
    conn = sqlite3.connect("cliente.db")
    conn.set_trace_callback(print)  # Para ver por pantalla los queries.
    return conn

def crear_tabla():
    """ """

    sql1 = "DROP TABLE IF EXISTS clientes"
    sql2 = "CREATE TABLE IF NOT EXISTS clientes (id PRIMARY KEY, direccion, password)"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()


def insert(cursor, datos):
    """ """
    sql = "INSERT INTO clientes VALUES (:id, :direccion, :password)"
    cursor.execute(sql, datos);


def update(cursor, datos):
    """ """
    sql = "UPDATE clientes SET password=:password, direccion=:direccion WHERE ID=:id"
    cursor.execute(sql, datos);
 

def run_ejemplo():

    conn = get_connection()
    cursor = conn.cursor()


    # INSERT
    datos = {"id": 1,
             "password": "123456789",
             "direccion": "Mi dirección 1"}
    insert(cursor, datos)

    datos = {"id": 2,
             "password": "123456789",
             "direccion": "Mi dirección 2"}
    insert(cursor, datos)
    conn.commit()


    # UPDATE
    datos = {"id": 1,
             "password": "sadsadasas",
             "direccion": "Mi dirección 1 Actualizada"}
    update(cursor, datos)

    conn.commit()


if __name__ == "__main__":
    """ """

    crear_tabla()
    run_ejemplo()





