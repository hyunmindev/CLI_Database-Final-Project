import os
from table import Table
from sql import *


def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


def handle_main_input(input_menu):
    clear_console()
    if input_menu == "1":
        print_insert_prompt(Table.STUDENT)
    elif input_menu == "2":
        print_delete_prompt(Table.STUDENT)
    elif input_menu == "3":
        print_select_prompt(Table.STUDENT)
    elif input_menu == "4":
        print_insert_prompt(Table.COURSE)
    elif input_menu == "5":
        print_delete_prompt(Table.COURSE)
    elif input_menu == "6":
        print_select_prompt(Table.COURSE)
    elif input_menu == "7":
        print_insert_prompt(Table.ENROL)
    elif input_menu == "8":
        print_delete_prompt(Table.ENROL)
    elif input_menu == "9":
        print_select_prompt(Table.ENROL)
    elif input_menu == "*":
        print_main_prompt()
    else:
        print("잘못된 입력")


def handle_student_insert_input(query):
    pass


def handle_student_delete_input(query):
    pass


def handle_student_select_input(query):
    pass


def handle_course_insert_input(query):
    pass


def handle_course_delete_input(query):
    pass


def handle_course_select_input(query):
    pass


def handle_enrol_insert_input(query):
    pass


def handle_enrol_delete_input(query):
    pass


def handle_enrol_select_input(query):
    pass


def print_main_prompt():
    print("1: 학생삽입")
    print("2: 학생삭제")
    print("3: 학생조회")
    print("4: 과목삽입")
    print("5: 과목삭제")
    print("6: 과목조회")
    print("7: 수강삽입")
    print("8: 수강삭제")
    print("9: 수강조회")
    print("0: 종료")
    print("*: 메뉴출력")


def print_insert_prompt(table_type):
    print("0: 종료")
    while True:
        if table_type == Table.STUDENT:
            print("[학번] [이름] [학년] [학과]")
            query = input("학생삽입 > ")
            if query == "0":
                break
            handle_student_insert_input(query)

        elif table_type == Table.COURSE:
            query = input("과목삽입 > ")
            if query == "0":
                break
            handle_course_insert_input(query)

        elif table_type == Table.ENROL:
            query = input("수강삽입 > ")
            if query == "0":
                break
            handle_enrol_insert_input(query)


def print_delete_prompt(table_type):
    print("0: 종료")
    while True:
        if table_type == Table.STUDENT:
            query = input("학생삭제 > ")
            if query == "0":
                break
            handle_student_delete_input(query)

        elif table_type == Table.COURSE:
            query = input("과목삭제 > ")
            if query == "0":
                break
            handle_course_delete_input(query)

        elif table_type == Table.ENROL:
            query = input("수강삭제 > ")
            if query == "0":
                break
            handle_enrol_delete_input(query)


def print_select_prompt(table_type):
    print("0: 종료")
    while True:
        if table_type == Table.STUDENT:
            query = input("학생조회 > ")
            if query == "0":
                break
            handle_student_select_input(query)

        elif table_type == Table.COURSE:
            query = input("과목조회 > ")
            if query == "0":
                break
            handle_course_select_input(query)

        elif table_type == Table.ENROL:
            query = input("수강조회 > ")
            if query == "0":
                break
            handle_enrol_select_input(query)
