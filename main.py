import os, msvcrt
from colorama import Fore,Style
import pyfiglet

def clear_stdin_buffer_windows():
    while msvcrt.kbhit():
        msvcrt.getch()

def one_character(chars_list, figlet):
    print(Style.RESET_ALL)
    os.system("cls")

    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" SINGLE CHARACTER MODULE "+"-"*7+"\n"*2)

    print(Style.RESET_ALL)
    single_char = input(Fore.YELLOW+"Choose the character: ")
    clear_stdin_buffer_windows()
    print()    

    if len(single_char)==0 or len(single_char)>1:
        print(Fore.RED+"------------Invalid INPUT------------")
    else:
        print(figlet.renderText(single_char))
        # p = (ord(single_char)-17)*6 if ord(single_char)>=48 and ord(single_char) <= 57 else 26*6 if single_char ==" " else 27 * 6 if single_char == "@" else 28 * 6 if single_char == "_" else 29 * 6 if single_char == "-" else 30 * 6 if single_char == "." else ((ord(single_char) - 64)-1)*6
        # for i in chars_list:
        #     for j  in range(p, p+6):
        #         print(i[j],end="")
        #     print()
    
    print(Fore.RED+"\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def words(chars_list, figlet):
    print(Style.RESET_ALL)
    os.system("cls")

    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" WORDS MODULE "+"-"*7+"\n"*2)

    print(Style.RESET_ALL)
    string = input(Fore.YELLOW+"Enter String (Only <= 15 Character): ")
    clear_stdin_buffer_windows()
    print()


    if len(string)>15 or len(string)==0:
        print(Fore.RED+"------------Invalid INPUT------------")
    else:
        print(figlet.renderText(string))
        # for i in chars_list:
        #     for j in string:
        #         p =(ord(j)-17)*6 if ord(j)>=48 and ord(j) <= 57 else 26*6 if j ==" " else 27 * 6 if j == "@" else 28 * 6 if j == "_" else 29 * 6 if j == "-" else 30 * 6 if j == "." else ((ord(j) - 64)-1)*6 
        #         for x in range(p, p+6):
        #             print(i[x],end="")
        #     print()
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def range_op(chars_list, figlet):
    print(Style.RESET_ALL)
    os.system("cls")

    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" RANGE MODULE "+"-"*7+"\n"*2)

    print(Style.RESET_ALL)
    string = input(Fore.YELLOW+"Enter Range Between (1 to 15 Letters) & in this format (A-D): ")
    clear_stdin_buffer_windows()
    print()

    if not (len(string)==3):
        print(Fore.RED+"------------Invalid INPUT------------")
    else:
        sr = ord(string[0])
        er = ord(string[2])
        if sr > er or (abs(er - sr) >= 15):
            print(Fore.RED+"\n\n------------Please Enter Valid Range in Sequence------------\n\n")
        else:
            text = "".join(chr(c) for c in range(ord(string[0]), ord(string[2]) + 1))
            print(figlet.renderText(text))
            # for x in range(sr, er+1):
            #     n = (x -1)*6
            #     for j in range(n , n + 6):
            #         print(i[j],end="")
            # print()
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def only_alphabets(chars_list, figlet):
    print(Style.RESET_ALL)
    os.system("cls")

    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" ONLY ALPHABETS MODULE "+"-"*7+"\n"*2)

    print(Style.RESET_ALL)
    string = input(Fore.YELLOW+"Enter String (Only <= 15 Character): ")
    clear_stdin_buffer_windows()
    print()
    
    if not (len(string)>=1 and len(string)<=15):
        print(Fore.RED+"------------Invalid INPUT------------")
    else:
        if string.isalpha() == False:
            print(Fore.RED+"------------Invalid INPUT - Please Enter Only Alphabets------------")
        else:
            print(figlet.renderText(string))
            # for i in chars_list:
            #     for x in string:
            #         n =((ord(x) - 64)-1)*6 
            #         for j in range(n , n + 6):
            #             print(i[j],end="")
            #     print()
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def only_numbers(chars_list, figlet):
    print(Style.RESET_ALL)
    os.system("cls")

    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" ONLY NUMBERS MODULE "+"-"*7+"\n"*2)

    print(Style.RESET_ALL)
    string = input(Fore.YELLOW+"Enter String (Only <= 15 Character): ")
    clear_stdin_buffer_windows()
    print()
    
    if not (len(string)>=1 and len(string)<=15):
        print(Fore.RED+"------------Invalid INPUT------------")
    else:
        if string.isnumeric() == False:
            print(Fore.RED+"------------Invalid INPUT - Please Enter Only Numbers------------")
        else:
            print(figlet.renderText(string))
            # for i in chars_list:
            #     for x in string:
            #         n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else ((ord(x) - 64)-1)*6 
            #         for j in range(n , n + 6):
            #             print(i[j],end="")
            #     print()
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()


isChoosingDone=False
figlet=None
def main_function():
    global isChoosingDone
    global figlet
    
    if isChoosingDone==False:
        os.system("cls")
        print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
        print("-"*7+" Choose font ----"+"-"*7+"\n"*2)
        print(Style.RESET_ALL)

        print(Fore.GREEN+"1.")
        figlet = pyfiglet.Figlet(font="graffiti")
        print(figlet.renderText("Graffiti"))
        
        print(Fore.GREEN+"2.")
        figlet = pyfiglet.Figlet(font="big")
        print(figlet.renderText("Big"))
        
        print(Fore.GREEN+"3.")
        figlet = pyfiglet.Figlet(font="epic")
        print(figlet.renderText("Epic"))
        
        print(Fore.GREEN+"4.")
        figlet = pyfiglet.Figlet(font="modular")
        print(figlet.renderText("Modular"))
        
        print(Fore.GREEN+"5.")
        figlet = pyfiglet.Figlet(font="electronic", width=140)
        print(figlet.renderText("Electronic"))

        print("6. exit"+"\n"*2)
        print(Fore.YELLOW+"CHOOSE: ")
        print(Style.RESET_ALL)
        
        clear_stdin_buffer_windows()
        ip = msvcrt.getch()
        if ip == b'1':
            figlet = pyfiglet.Figlet(font="graffiti")
            isChoosingDone=True
        elif ip == b'2':
            figlet = pyfiglet.Figlet(font="big")
            isChoosingDone=True
        elif ip == b'3':
            figlet = pyfiglet.Figlet(font="epic")
            isChoosingDone=True
        elif ip == b'4':
            figlet = pyfiglet.Figlet(font="modular")
            isChoosingDone=True
        elif ip == b'5':
            figlet = pyfiglet.Figlet(font="electronic", width=140)
            isChoosingDone=True
        elif ip == b'6':
            exit()
        else:
            main_function()


    characters = [
        r"            ____     _____   _____    ______   ______    _____   _    _   _____        _   _  __  _        __  __   _   _    ____    _____     ____    _____     _____   _______   _    _  __      __ __          __ __   __ __     __  ______                                    ___    __   ___    ____    _  _     _____     __    ______    ___     ___            _                  _           __           _       _   _   _      _                                                            _                                                    ",
        r"    /\     |  _ \   / ____| |  __ \  |  ____| |  ____|  / ____| | |  | | |_   _|      | | | |/ / | |      |  \/  | | \ | |  / __ \  |  __ \   / __ \  |  __ \   / ____| |__   __| | |  | | \ \    / / \ \        / / \ \ / / \ \   / / |___  /    ____                           / _ \  /_ | |__ \  |___ \  | || |   | ____|   / /   |____  |  / _ \   / _ \          | |                | |         / _|         | |     (_) (_) | |    | |                                                          | |                                                   ",
        r"   /  \    | |_) | | |      | |  | | | |__    | |__    | |  __  | |__| |   | |        | | | ' /  | |      | \  / | |  \| | | |  | | | |__) | | |  | | | |__) | | (___      | |    | |  | |  \ \  / /   \ \  /\  / /   \ V /   \ \_/ /     / /    / __ \             ______      | | | |  | |    ) |   __) | | || |_  | |__    / /_       / /  | (_) | | (_) |   __ _  | |__     ___    __| |   ___  | |_    __ _  | |__    _   _  | | __ | |  _ __ ___    _ __     ___    _ __     __ _   _ __   ___  | |_   _   _  __   __ __      __ __  __  _   _   ____ ",
        r"  / /\ \   |  _ <  | |      | |  | | |  __|   |  __|   | | |_ | |  __  |   | |    _   | | |  <   | |      | |\/| | | . ` | | |  | | |  ___/  | |  | | |  _  /   \___ \     | |    | |  | |   \ \/ /     \ \/  \/ /     > <     \   /     / /    / / _` |           |______|     | | | |  | |   / /   |__ <  |__   _| |___ \  | '_ \     / /    > _ <   \__, |  / _` | | '_ \   / __|  / _` |  / _ \ |  _|  / _` | | '_ \  | | | | | |/ / | | | '_ ` _ \  | '_ \   / _ \  | '_ \   / _` | | '__| / __| | __| | | | | \ \ / / \ \ /\ / / \ \/ / | | | | |_  / ",
        r" / ____ \  | |_) | | |____  | |__| | | |____  | |      | |__| | | |  | |  _| |_  | |__| | | . \  | |____  | |  | | | |\  | | |__| | | |      | |__| | | | \ \   ____) |    | |    | |__| |    \  /       \  /\  /     / . \     | |     / /__  | | (_| |                     _  | |_| |  | |  / /_   ___) |    | |    ___) | | (_) |   / /    | (_) |    / /  | (_| | | |_) | | (__  | (_| | |  __/ | |   | (_| | | | | | | | | | |   <  | | | | | | | | | | | | | (_) | | |_) | | (_| | | |    \__ \ | |_  | |_| |  \ V /   \ V  V /   >  <  | |_| |  / /  ",
        r"/_/    \_\ |____/   \_____| |_____/  |______| |_|       \_____| |_|  |_| |_____|  \____/  |_|\_\ |______| |_|  |_| |_| \_|  \____/  |_|       \___\_\ |_|  \_\ |_____/     |_|     \____/      \/         \/  \/     /_/ \_\    |_|    /_____|  \ \__,_|                    (_)  \___/   |_| |____| |____/     |_|   |____/   \___/   /_/      \___/    /_/    \__,_| |_.__/   \___|  \__,_|  \___| |_|    \__, | |_| |_| |_| | | |_|\_\ |_| |_| |_| |_| |_| |_|  \___/  | .__/   \__, | |_|    |___/  \__|  \__,_|   \_/     \_/\_/   /_/\_\  \__, | /___| ",
        r"                                                                                                                                                                                                                                                 \____/   ______                                                                                                                                            __/ |            _/ |                                        | |         | |                                                        __/ |       ",
        r"                                                                                                                                                                                                                                                         |______|                                                                                                                                          |___/            |__/                                         |_|         |_|                                                       |___/        "
    ]

    os.system("cls")
    print(Fore.LIGHTMAGENTA_EX+"\n"*3+"*"*7+" ASCII ART PROJECT "+"*"*7+"\n"*2)
    print("-"*7+" CHOOSE ONE OF THE FOLLOWING OPTIONS "+"-"*7+"\n"*2)
    print(Style.RESET_ALL)
    print(Fore.GREEN+"1. one character")
    print("2. words(max 15 letters)")
    print("3. range(input in sequence -- maximum 15 letters)")
    print("4. only alphabets")
    print("5. only numbers")
    print("6. exit"+"\n"*2)
    print(Fore.YELLOW+"CHOOSE: ")
    print(Style.RESET_ALL)
    
    clear_stdin_buffer_windows()
    ip = msvcrt.getch()
    if ip == b'1':
        one_character(characters, figlet)
    elif ip == b'2':
        words(characters, figlet)
    elif ip == b'3':
        range_op(characters, figlet)
    elif ip == b'4':
        only_alphabets(characters, figlet)
    elif ip == b'5':
        only_numbers(characters, figlet)
    elif ip == b'6':
        exit()
    else:
        main_function()
        


main_function()
    