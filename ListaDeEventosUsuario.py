import pymysql

def Database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='Notes&Dates'
    )

    print("Conexion establecida correctamente")

    mycursor = connection.cursor()

    return mycursor

U_ID = 'Leaves'

def gListaEventoUsuario(U_ID):

    db = Database()


    sql = 'SELECT * FROM Evento,Cuenta WHERE Cuenta.CUE_ID = Evento.EVE_CUENTA AND EVE_CUENTA = %s'
    db.execute(sql, U_ID)
    evento = db.fetchall()


    return evento

lista = gListaEventoUsuario(U_ID)

for evento in lista:
        print("Id", evento[0])
        print("Cuenta", evento[1])
        print("Nombre Evento", evento[6])
        print("Descripcion Evento", evento[7])
