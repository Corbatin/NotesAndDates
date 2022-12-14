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
sql = 'SELECT * FROM Cuenta WHERE Cuenta.CUE_ID = %s and Cuenta.CUE_PASS = %s and Cuenta.CUE_TUSER = %s and Cuenta.CUE_ESTADO = %s '

db.execute(sql,credencial)
tuser = db.fetchall()

for user in tuser:
    print("ID ",user[0])
    sys.stdout.flush()
    print("NOMBRE: ",user[1])
    sys.stdout.flush()
    print("TUSER:  ",user[2])
    sys.stdout.flush()
    if credencial[2] == 'A':
        print("ADMIN")
        sys.stdout.flush()
        return 'A'
    if credencial[2] == 'U':
        print("user")
        sys.stdout.flush()
        return 'U'   
        #for atts in user:
        #    print("epico")
        #    if credencial[0] == user[0] and credencial[1] == user[1] and credencial[2] == 'A' and credencial[3] == 'A':
        #
        #        print("Usuario tipo Admin")
        #        return 'A'
        #
        #    if credencial[0] == user[0] and credencial[1] == user[1] and credencial[2] == 'U':
        #        
        #        print("Usuario tipo usuario")
        #        return 'U'    
            

     
sys.stdout.flush()   
