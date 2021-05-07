import os
from sql import *


def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


def handle_main_input(input_menu):
    clear_console()
    if input_menu == "1":
        print_student_insert_prompt()
    elif input_menu == "2":
        print_student_delete_prompt()
    elif input_menu == "3":
        print_student_select_prompt()
    elif input_menu == "4":
        print_course_insert_prompt()
    elif input_menu == "5":
        print_course_delete_prompt()
    elif input_menu == "6":
        print_course_select_prompt()
    elif input_menu == "7":
        print_enrol_insert_prompt()
    elif input_menu == "8":
        print_enrol_delete_prompt()
    elif input_menu == "9":
        print_enrol_select_prompt()
    elif input_menu == "*":
        print_main_prompt()
    else:
        print("잘못된 입력")


def handle_student_insert_input(query):
    query = query.split()
    if len(query) < 4:
        raise Exception("인자부족")
    [sno, sname, syear, dept] = query
    print(sno)
    print(sname)
    print(syear)
    print(dept)
    # TODO


def handle_student_delete_input(query):
    pass
    # TODO


def handle_student_select_input(query):
    pass
    # TODO


def handle_course_insert_input(query):
    pass
    # TODO


def handle_course_delete_input(query):
    pass
    # TODO


def handle_course_select_input(query):
    pass
    # TODO


def handle_enrol_insert_input(query):
    pass
    # TODO


def handle_enrol_delete_input(query):
    pass
    # TODO


def handle_enrol_select_input(query):
    pass
    # TODO


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


def print_student_insert_prompt():
    print("0: 종료")
    print("[학번] [이름] [학년] [학과]: 삽입")
    while True:
        query = input("학생삽입 > ")
        clear_console()
        if query == "0":
            break
        try:
            handle_student_insert_input(query=query)
        except Exception as exception:
            print(f"[Error] {exception}")


def print_student_delete_prompt():
    while True:
        print("0: 종료")
        query = input("학생삭제 > ")
        if query == "0":
            break
        handle_student_delete_input(query=query)


def print_student_select_prompt():
    print("0: 종료")
    while True:
        query = input("학생조회 > ")
        if query == "0":
            break
        handle_student_select_input(query=query)


def print_course_insert_prompt():
    while True:
        query = input("과목삽입 > ")
        if query == "0":
            break
        handle_course_insert_input(query=query)


def print_course_delete_prompt():
    while True:
        print("0: 종료")
        query = input("과목삭제 > ")
        if query == "0":
            break
        handle_course_delete_input(query=query)


def print_course_select_prompt():
    while True:
        print("0: 종료")
        query = input("과목조회 > ")
        if query == "0":
            break
        handle_course_select_input(query=query)


def print_enrol_insert_prompt():
    while True:
        print("0: 종료")
        query = input("수강삽입 > ")
        if query == "0":
            break
        handle_enrol_insert_input(query=query)


def print_enrol_delete_prompt():
    while True:
        print("0: 종료")
        query = input("수강삭제 > ")
        if query == "0":
            break
        handle_enrol_delete_input(query=query)


def print_enrol_select_prompt():
    while True:
        print("0: 종료")
        query = input("수강조회 > ")
        if query == "0":
            break
        handle_enrol_select_input(query=query)
