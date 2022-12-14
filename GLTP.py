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
return [mycursor, connection]

db = Database()   
sql = 'SELECT * FROM TEvento'
db.execute(sql)
teventos = db.fetchall()

for tevento in lista:
        print("Id", tevento[0])
        print("Nombre", tevento[1])
        
sys.stdout.flush()        
