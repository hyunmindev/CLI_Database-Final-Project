import os
from sql import *
from termcolor import colored


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
        if input_value == "0":
            break
        try:
            result = handle_input(input_value)
        except Exception as exception:
            print(colored(f"[Error] {exception}", "red"))
        else:
            print(colored(f"[Success] {prompt_title} {result}", "green"))


def handle_main_input(input_value):
    if input_value == "1":
        run_prompt(print_select_by_title_help, handle_select_by_title_input, "검색")
    elif input_value == "2":
        run_prompt(print_select_by_actor_help, handle_select_by_actor_input, "검색")
    elif input_value == "3":
        run_prompt(print_select_by_director_help, handle_select_by_director_input, "검색")
    elif input_value == "4":
        run_prompt(print_select_by_genre_help, handle_select_by_genre_input, "검색")
    elif input_value == "5":
        run_prompt(print_select_etc_help, handle_select_etc_input, "기타")
    else:
        raise Exception("존재하지 않는 입력")
    return input_value


def handle_sub_input(input_value, query):
    try:
        result = query(input_value)
    except Exception:
        raise
    return result


def handle_select_by_title_input(input_value):
    try:
        result = select_by_title(input_value)
    except Exception:
        raise
    return {'title': input_value, 'result': result}


def handle_select_by_actor_input(input_value):
    try:
        if input_value[0] == '1':
            result = select_by_actor(input_value[2:], '1')
        elif input_value[0] == '2':
            result = select_by_actor(input_value[2:], '2')
        else:
            raise Exception("존재하지 않는 입력")
    except Exception:
        raise
    return {'actor': input_value[2:], 'result': result}


def handle_select_by_director_input(input_value):
    try:
        result = select_by_director(input_value)
    except Exception:
        raise
    return {'director': input_value, 'result': result}


def handle_select_by_genre_input(input_value):
    try:
        if input_value[0] == '1':
            result = select_by_genre(input_value[2:], '1')
        elif input_value[0] == '2':
            result = select_by_genre(input_value[2:], '2')
        else:
            raise Exception("존재하지 않는 입력")
    except Exception:
        raise
    return {'genre': input_value[2:], 'result': result}


def handle_select_etc_input(input_value):
    try:
        if input_value[0] == '1':
            result = select_oldest_actor()
        elif input_value[0] == '2':
            result = select_actor_movie_count_actor(input_value[2:])
        else:
            raise Exception('존재하지 않는 입력')
    except Exception:
        raise
    return {'result': result}


def print_main_help():
    print("영화 검색")
    print("1: 제목으로 검색")
    print("2: 배우 이름으로 검색")
    print("3: 감독 이름으로 검색")
    print("4: 장르로 검색")
    print("5: 기타")
    print("0: 종료")


def print_select_by_title_help():
    print("[제목]: 검색")
    print("0: 종료")


def print_select_by_actor_help():
    print("1 [배우 이름]: 검색 (평점 내림차순)")
    print("2 [배우 이름]: 검색 (평가수 내림차순)")
    print("0: 종료")


def print_select_by_director_help():
    print("[감독 이름]: 검색")
    print("0: 종료")


def print_select_by_genre_help():
    print("1 [장르]: 검색")
    print("2 [장르]: 검색")
    print("0: 종료")


def print_select_etc_help():
    print("1: 나이가 제일 많은 배우")
    print("2 [배우 이름]: 배우의 영화 촬영 개수")
    print("0: 종료")
