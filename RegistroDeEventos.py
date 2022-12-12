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

    return [mycursor, connection]


evento = ['17', 'Leaves', 'V', 'REU', '1', '2023', 'Webinar de la empresa', 'El enlace será enviado en las proximas horas', '0900', '1000' ]


def RegistroDeEventos(evento):

    db = Database()


    sql = 'INSERT INTO Evento VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    db[0].execute(sql,evento)
    db[1].commit()

RegistroDeEventos(evento)