import pymysql 

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

def gListaModalidad():

    db = Database()   


    sql = 'SELECT * FROM Modalidad'

    db.execute(sql)
    Modalidades = db.fetchall()

    
    return Modalidades   

lista = gListaModalidad()

for modalidad in lista:
        print("ID", modalidad[0])
        print("Nombre", modalidad[1])   