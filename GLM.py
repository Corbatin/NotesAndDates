import pymysql 
import sys

def Database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='NotesandDates'
    )

    print("Conexion establecida correctamente")
    sys.stdout.flush()

    mycursor = connection.cursor()
    return mycursor

db = Database()   
sql = 'SELECT * FROM Modalidad'
db.execute(sql)
Modalidades = db.fetchall()    
     

for modalidad in lista:
        print("ID", modalidad[0])
        sys.stdout.flush()
        print("Nombre", modalidad[1])
        sys.stdout.flush()
