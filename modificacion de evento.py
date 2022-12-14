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
actualizacion = [evento[2], evento[3], evento[4], evento[5], evento[6], evento[7], evento[8], evento[9], evento[0]]
sql = 'UPDATE Evento SET EVE_MOD = %s, EVE_TIPO = %s, EVE_DNUM = %s, EVE_DANYO = %s, EVE_NOMBRE = %s, EVE_DESCRIPCION = %s, EVE_HORAINICIO = %s, EVE_HORAFIN = %s WHERE EVE_ID = %s' 
db[0].execute(sql, actualizacion)
db[1].commit()

sys.stdout.flush()
