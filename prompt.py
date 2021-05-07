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
            print(colored(f"[Success] {result}", "green"))


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


def handle_student_insert_input(input_value):
    input_value = input_value.split()
    if len(input_value) < 4:
        raise ValueError("Too few arguments")
    elif len(input_value) > 4:
        raise ValueError("Too many arguments")
    [sno, sname, syear, dept] = input_value
    try:
        insert_student(sno, sname, syear, dept)
    except Exception:
        raise
    return input_value


def handle_student_delete_input(input_value):
    pass
    # TODO


def handle_student_select_input(input_value):
    pass
    # TODO


def handle_course_insert_input(input_value):
    input_value = input_value.split()
    if len(input_value) < 5:
        raise ValueError("Too few arguments")
    elif len(input_value) > 5:
        raise ValueError("Too many arguments")
    [cno, cnmae, credit, dept, prname] = input_value
    try:
        insert_course(cno, cnmae, credit, dept, prname)
    except Exception:
        raise
    return input_value


def handle_course_delete_input(input_value):
    pass
    # TODO


def handle_course_select_input(input_value):
    pass
    # TODO


def handle_enrol_insert_input(input_value):
    input_value = input_value.split()
    if len(input_value) < 5:
        raise ValueError("Too few arguments")
    elif len(input_value) > 5:
        raise ValueError("Too many arguments")
    [sno, cno, grade, midterm, final] = input_value
    try:
        insert_enrol(sno, cno, grade, midterm, final)
    except Exception:
        raise
    return input_value


def handle_enrol_delete_input(input_value):
    pass
    # TODO


def handle_enrol_select_input(input_value):
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
    print("[과목번호] [이름] [학년] [학과] [교수]: 삽입")
    print("0: 종료")


def print_course_delete_help():  # 과목삭제 부프롬프트 출력
    print("0: 종료")


def print_course_select_help():  # 과목조회 부프롬프트 출력
    print("0: 종료")


def print_enrol_insert_help():  # 등록삽입 부프롬프트 출력
    print("[학번] [과목번호] [성적] [중간 점수] [기말 점수]: 삽입")
    print("0: 종료")


def print_enrol_delete_help():  # 등록삭제 부프롬프트 출력
    print("0: 종료")


def print_enrol_select_help():  # 등록조회 부프롬프트 출력
    print("0: 종료")
