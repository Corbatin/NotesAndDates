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

evento1 = ['1', 'Leaves', 'P', 'REC', 1, '2023', 'Discreta', 'estudiar discreta', '2300', '2330' ]

def modificacion_evento(evento):
    db = Database()

    actualizacion = [evento[2], evento[3], evento[4], evento[5], evento[6], evento[7], evento[8], evento[9], evento[0]]
    sql = 'UPDATE Evento SET EVE_MOD = %s, EVE_TIPO = %s, EVE_DNUM = %s, EVE_DANYO = %s, EVE_NOMBRE = %s, EVE_DESCRIPCION = %s, EVE_HORAINICIO = %s, EVE_HORAFIN = %s WHERE EVE_ID = %s' 
    db[0].execute(sql, actualizacion)
    db[1].commit()

modificacion_evento(evento1)