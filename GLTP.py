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

def gListaTEvento():

    db = Database()   


    sql = 'SELECT * FROM TEvento'

    db.execute(sql)
    teventos = db.fetchall()

    
    return teventos    

lista = gListaTEvento()

for tevento in lista:
        print("Id", tevento[0])
        print("Nombre", tevento[1])   
         