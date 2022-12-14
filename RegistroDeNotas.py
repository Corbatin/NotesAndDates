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
return [mycursor, connection]

db = Database()
sql = 'INSERT INTO Nota VALUES(%s,%s,%s,%s)'
db[0].execute(sql,nota)
db[1].commit()

sys.stdout.flush()
