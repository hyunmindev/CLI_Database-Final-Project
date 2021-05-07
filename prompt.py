import os
from sql import *


def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


def run_prompt(print_help, handle_input, prompt_title=""):
    while True:
        print_help()
        input_value = input(prompt_title + "> ")
        clear_console()
        if input_value == "0":  # 0 입력 시 종료
            break
        try:
            handle_input(input_value)
        except Exception as exception:
            print(f"[Error] {exception}")


def handle_main_input(input_menu):
    if input_menu == "1":
        run_prompt(print_student_insert_help, handle_student_insert_input, "학생삽입")
    elif input_menu == "2":
        run_prompt(print_student_delete_help, handle_student_delete_input, "학생삭제")
    elif input_menu == "3":
        run_prompt(print_student_select_help, handle_student_select_input, "학생조회")
    elif input_menu == "4":
        run_prompt(print_course_insert_help, handle_course_insert_input, "과목삽입")
    elif input_menu == "5":
        run_prompt(print_course_delete_help, handle_course_delete_input, "과목삭제")
    elif input_menu == "6":
        run_prompt(print_course_select_help, handle_course_select_input, "과목조회")
    elif input_menu == "7":
        run_prompt(print_enrol_insert_help, handle_enrol_insert_input, "등록삽입")
    elif input_menu == "8":
        run_prompt(print_enrol_delete_help, handle_enrol_delete_input, "등록삭제")
    elif input_menu == "9":
        run_prompt(print_enrol_select_help, handle_enrol_select_input, "등록조회")
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


def print_main_help():
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


def print_student_insert_help():  # 학생삽입 부프롬프트 출력
    print("[학번] [이름] [학년] [학과]: 삽입")
    print("0: 종료")


def print_student_delete_help():  # 학생삭제 부프롬프트 출력
    print("0: 종료")


def print_student_select_help():  # 학생조회 부프롬프트 출력
    print("0: 종료")


def print_course_insert_help():  # 과목삽입 부프롬프트 출력
    print("0: 종료")


def print_course_delete_help():  # 과목삭제 부프롬프트 출력
    print("0: 종료")


def print_course_select_help():  # 과목조회 부프롬프트 출력
    print("0: 종료")


def print_enrol_insert_help():  # 등록삽입 부프롬프트 출력
    print("0: 종료")


def print_enrol_delete_help():  # 등록삭제 부프롬프트 출력
    print("0: 종료")


def print_enrol_select_help():  # 등록조회 부프롬프트 출력
    print("0: 종료")
