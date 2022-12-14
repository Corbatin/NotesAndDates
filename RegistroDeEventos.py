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
sql = 'INSERT INTO Evento VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
db[0].execute(sql,evento)
db[1].commit()

sys.stdout.flush()
