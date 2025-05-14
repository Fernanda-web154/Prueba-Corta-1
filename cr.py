import mysql.connector

def conectar(consulta_sql):
    config = {
        'user': 'u48dywqrelwifgf9',
        'password': 'KDsoCkCk4HTREpiYG9t4',
        'host': 'blwkycdvpcuymls399fh-mysql.services.clever-cloud.com',
        'database': 'blwkycdvpcuymls399fh',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.:)")

        cursor = conexion.cursor()
        cursor.execute(consulta_sql)
        resultado = cursor.fetchall()

        conexion.close()
        return resultado

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return []

