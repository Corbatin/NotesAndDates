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

    mycursor = connection.cursor()
    return mycursor


db = Database()   

sql = 'SELECT * FROM Estado'

db.execute(sql)
Estados = db.fetchall()  

for estado in lista:
        print("ID", estado[0])
        sys.stdout.flush()
        print("Nombre", estado[1])
        sys.stdout.flush()
        
sys.stdout.flush()
