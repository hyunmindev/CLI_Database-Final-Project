import os
from sql import *
from termcolor import colored


def clear_console():
    """clear console"""
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


def run_prompt(print_help, handle_input, prompt_title=""):
    """Run prompt while input is "0"

    Args:
        print_help(function): Function that outputs the prompt's help
        handle_input(function): Functions that handle input values
        prompt_title(string): Title of prompt

    """
    while True:
        print_help()
        input_value = input(prompt_title + "> ")
        clear_console()
        if input_value == "0":  # 0 입력 시 종료
            break
        try:
            result = handle_input(input_value)
        except Exception as exception:
            print(colored(f"[Error] {exception}", "red"))
        else:
            print(colored(f"[Success] {prompt_title} {result}", "green"))


def handle_main_input(input_value):
    """Handle main input values

    Args:
        input_value(int): Value typed by user at main prompt

    Returns:

    """
    if input_value == "1":
        run_prompt(print_student_insert_help, handle_student_insert_input, "학생삽입")
    elif input_value == "2":
        run_prompt(print_student_delete_help, handle_student_delete_input, "학생삭제")
    elif input_value == "3":
        run_prompt(print_student_select_help, handle_student_select_input, "학생조회")
    elif input_value == "4":
        run_prompt(print_course_insert_help, handle_course_insert_input, "과목삽입")
    elif input_value == "5":
        run_prompt(print_course_delete_help, handle_course_delete_input, "과목삭제")
    elif input_value == "6":
        run_prompt(print_course_select_help, handle_course_select_input, "과목조회")
    elif input_value == "7":
        run_prompt(print_enrol_insert_help, handle_enrol_insert_input, "등록삽입")
    elif input_value == "8":
        run_prompt(print_enrol_delete_help, handle_enrol_delete_input, "등록삭제")
    elif input_value == "9":
        run_prompt(print_enrol_select_help, handle_enrol_select_input, "등록조회")
    else:
        raise Exception("존재하지 않는 입력")
    return input_value


def handle_sub_input(input_value, query, argument_count):
    input_value = input_value.split()
    if len(input_value) < argument_count:
        raise ValueError("Too few arguments")
    elif len(input_value) > argument_count:
        raise ValueError("Too many arguments")
    try:
        query(*input_value)
    except Exception:
        raise


def handle_student_insert_input(input_value):
    handle_sub_input(input_value, insert_student, 4)
    return input_value


def handle_student_delete_input(input_value):
    handle_sub_input(input_value, delete_student, 1)
    return input_value


def handle_student_select_input(input_value):
    if input_value == "1":
        select_student()
    else:
        handle_sub_input(input_value, select_student, 1)
    return input_value


def handle_course_insert_input(input_value):
    handle_sub_input(input_value, insert_course, 5)
    return input_value


def handle_course_delete_input(input_value):
    handle_sub_input(input_value, delete_course, 1)
    return input_value


def handle_course_select_input(input_value):
    if input_value == "1":
        select_course()
    else:
        handle_sub_input(input_value, select_course, 1)
    return input_value


def handle_enrol_insert_input(input_value):
    handle_sub_input(input_value, insert_enrol, 5)
    return input_value


def handle_enrol_delete_input(input_value):
    handle_sub_input(input_value, delete_enrol, 2)
    return input_value


def handle_enrol_select_input(input_value):
    if input_value == "1":
        select_enrol()
    else:
        handle_sub_input(input_value, select_enrol, 2)
    return input_value


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
    print("[학번]: 삭제")
    print("0: 종료")


def print_student_select_help():  # 학생조회 부프롬프트 출력
    print("[학번]: 특정 학생 조회")
    print("1: 전체 학생 조회 (학번 오름차순)")
    print("0: 종료")


def print_course_insert_help():  # 과목삽입 부프롬프트 출력
    print("[과목번호] [이름] [학년] [학과] [교수]: 삽입")
    print("0: 종료")


def print_course_delete_help():  # 과목삭제 부프롬프트 출력
    print("[과목번호]: 삭제")
    print("0: 종료")


def print_course_select_help():  # 과목조회 부프롬프트 출력
    print("[과목번호]: 특정 과목 조회")
    print("1: 전체 과목 조회 (과목번호 오름차순)")
    print("0: 종료")


def print_enrol_insert_help():  # 등록삽입 부프롬프트 출력
    print("[학번] [과목번호] [성적] [중간점수] [기말점수]: 삽입")
    print("0: 종료")


def print_enrol_delete_help():  # 등록삭제 부프롬프트 출력
    print("[학번] [과목번호]: 삭제")
    print("0: 종료")


def print_enrol_select_help():  # 등록조회 부프롬프트 출력
    print("[학번] [과목번호]: 특정 등록 조회")
    print("1: 전체 등록 조회")
    print("0: 종료")
