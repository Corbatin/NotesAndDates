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

nota1= ['1', 'Leaves', 'fumar lucky', 'Tocar con pipazp épico' ]

def modificacion_notas(nota):
    db = Database()

    actualizacion = [nota[2], nota[3], nota[0], nota[1]]
    
    
    
    sql = 'UPDATE Nota SET NOT_NOMBRE = %s, NOT_DESCRIPCION = %s WHERE NOT_ID = %s AND NOT_CUENTA= %s'
    db[0].execute(sql, actualizacion)
    db[1].commit()

modificacion_notas(nota1)