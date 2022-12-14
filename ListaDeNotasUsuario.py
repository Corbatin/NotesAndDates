import pymysql
import sys

def Database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='Notes&Dates'
    )

    print("Conexion establecida correctamente")
    sys.stdout.flush()

    mycursor = connection.cursor()
    return mycursor

db = Database()
sql = 'SELECT * FROM Nota,Cuenta WHERE Cuenta.CUE_ID = Nota.NOT_CUENTA AND NOT_CUENTA = %s'
db.execute(sql, U_ID)
nota = db.fetchall()

for nota in lista:
    print("Id", nota[0])
    print("Cuenta", nota[1])
    print("Nombre Nota", nota[2])
    
sys.stdout.flush()
