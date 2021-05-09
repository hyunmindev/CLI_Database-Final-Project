import pymysql

university = pymysql.connect(host="localhost", user="root", password="4646", db="university")
cursor = university.cursor(pymysql.cursors.DictCursor)


def insert_student(sno, sname, syear, dept):
    sql = "insert into STUDENT values (%s, %s, %s, %s)"
    cursor.execute(sql, (sno, sname, syear, dept))
    university.commit()


def delete_student(sno):
    sql = "delete from STUDENT where %s = STUDENT.sno"
    cursor.execute(sql, sno)
    university.commit()


def select_student(sno=""):
    if sno == "":
        sql = "select * from STUDENT"
        cursor.execute(sql)
    else:
        sql = "select * from STUDENT where %s = STUDENT.sno"
        cursor.execute(sql, sno)
    row = cursor.fetchone()
    while row:
        print(f"학번: {row['sno']}, 이름: {row['sname']}, 학년: {row['syear']}, 학과: {row['dept']}")
        row = cursor.fetchone()


def insert_course(cno, cnmae, credit, dept, prname):
    sql = "insert into COURSE values (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (cno, cnmae, credit, dept, prname))
    university.commit()


def delete_course(cno):
    sql = "delete from COURSE where %s = COURSE.cno"
    cursor.execute(sql, cno)
    university.commit()


def select_course(cno=""):
    if cno == "":
        sql = "select * from COURSE"
        cursor.execute(sql)
    else:
        sql = "select * from COURSE where %s = COURSE.cno"
        cursor.execute(sql, cno)
    row = cursor.fetchone()
    while row:
        print(f"과목번호: {row['cno']}, 이름: {row['cname']}, 학점: {row['credit']}, 학과: {row['dept']}, 교수: {row['prname']}")
        row = cursor.fetchone()


def insert_enrol(sno, cno, grade, midterm, final):
    sql = "insert into ENROL values (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (sno, cno, grade, midterm, final))
    university.commit()


def delete_enrol(sno, cno):
    sql = "delete from ENROL where %s = ENROL.sno and %s = ENROL.cno"
    cursor.execute(sql, (sno, cno))
    university.commit()


def select_enrol(sno="", cno=""):
    if sno == "" and cno == "":
        sql = "select * from ENROL"
        cursor.execute(sql)
    elif sno == "*" and cno == "*":
        sql = "select * from ENROL"
        cursor.execute(sql)
    elif sno == "*":
        sql = "select * from ENROL where %s = ENROL.cno"
        cursor.execute(sql, cno)
    elif cno == "*":
        sql = "select * from ENROL where %s = ENROL.sno"
        cursor.execute(sql, sno)
    else:
        sql = "select * from ENROL where %s = ENROL.sno and %s = ENROL.cno"
        cursor.execute(sql, (sno, cno))
    row = cursor.fetchone()
    while row:
        print(f"학번: {row['sno']}, 과목번호: {row['cno']}, 성적: {row['grade']}, 중간점수: {row['midterm']}, 기말점수: {row['final']}")
        row = cursor.fetchone()
