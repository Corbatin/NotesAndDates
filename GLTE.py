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

def gListaTEstados():

    db = Database()   

    sql = 'SELECT * FROM Estado'

    db.execute(sql)
    Estados = db.fetchall()

    return Estados    

lista = gListaTEstados()

for estado in lista:
        print("ID", estado[0])
        print("Nombre", estado[1])   