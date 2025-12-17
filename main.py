import os, msvcrt
from colorama import Fore,Style
import pyfiglet

def clear_stdin_buffer_windows():
    while msvcrt.kbhit():
        msvcrt.getch()

def one_character(figlet):
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
    
    print(Fore.RED+"\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def words(figlet):
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
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def range_op(figlet):
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
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def only_alphabets(figlet):
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
        
    
    print("\n\nTo continue with the menu press any key... To exit press 'n'")
    ip = msvcrt.getch()
    if ip == b'n':
        print(Style.RESET_ALL)
        exit()
    else:
        main_function()

def only_numbers(figlet):
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
        one_character(figlet)
    elif ip == b'2':
        words(figlet)
    elif ip == b'3':
        range_op(figlet)
    elif ip == b'4':
        only_alphabets(figlet)
    elif ip == b'5':
        only_numbers(figlet)
    elif ip == b'6':
        exit()
    else:
        main_function()
        


main_function()
    