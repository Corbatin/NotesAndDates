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

    return [mycursor, connection]


nota1= ['21', 'Leaves', 'Ensayar stay', 'Tocar con uñeta' ]


def RegistroDeNota(nota):

    db = Database()


    sql = 'INSERT INTO Nota VALUES(%s,%s,%s,%s)'
    db[0].execute(sql,nota)
    db[1].commit()

RegistroDeNota(nota1)
