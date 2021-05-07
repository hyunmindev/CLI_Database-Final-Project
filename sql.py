import pymysql

myDB = pymysql.connect(host="localhost", user="root", password="4646", db="university")
curs = myDB.cursor(pymysql.cursors.DictCursor)


def temp():
    sql = "select * from student"
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print(f"학번: {row['sno']} 이름 {row['sname']}")
        row = curs.fetchone()

    curs.close()
    myDB.close()
