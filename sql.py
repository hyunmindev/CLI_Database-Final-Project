import pymysql

university = pymysql.connect(host="localhost", user="root", password="4646", db="university")
cursor = university.cursor(pymysql.cursors.DictCursor)


def insert_student(sno, sname, syear, dept):
    sql = "insert into STUDENT values (%s, %s, %s, %s)"
    cursor.execute(sql, (sno, sname, syear, dept))
    university.commit()


def delete_student():
    pass


def select_student():
    pass


def insert_course(cno, cnmae, credit, dept, prname):
    sql = "insert into COURSE values (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (cno, cnmae, credit, dept, prname))
    university.commit()


def delete_course():
    pass


def select_course():
    pass


def insert_enrol(sno, cno, grade, midterm, final):
    sql = "insert into ENROL values (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (sno, cno, grade, midterm, final))
    university.commit()


def delete_enrol():
    pass


def select_enrol():
    pass


def temp():
    sql = "select * from student"
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print(f"학번: {row['sno']} 이름 {row['sname']}")
        row = cursor.fetchone()
