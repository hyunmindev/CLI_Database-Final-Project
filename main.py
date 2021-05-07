from prompt import *

if __name__ == '__main__':
    print_main_prompt()

    while True:
        inputMenu = input("> ")
        if inputMenu == "0":  # 0 입력 시 종료
            break
        handle_main_input(inputMenu)
