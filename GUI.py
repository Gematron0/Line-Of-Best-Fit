### libary imports ###
import os # clear the colsol
import time # to make the code wait
from colorama import Fore, Back, Style #colloring concol
from colorama import init
init(autoreset=True)

### clears the concle for easey reading ###
clearConsole = lambda: os.system('cls'
    if os.name in ('nt', 'dos') else 'clear')

### gives a countdown so people cant spam the server if they imputed something incurrects ###
def resetOptions():
    i = 3
    while i != 0:
        i = i - 1
        clearConsole()
        print (Fore.BLACK+Back.YELLOW+"your statemnt was invallid")
        print (Fore.BLACK+Back.YELLOW+"Reseting system in",i,Fore.BLACK+Back.YELLOW+"seconds")
        time.sleep(1)
    clearConsole()
    return

### inputs the UI to let the person input some numbers ###
def InputUI(totInputsFrunt, TotInputsBack, Part):
    i = 0
    if Part == 1:
        while i != totInputsFrunt - 1:
            i = i + 1
            print (Fore.BLACK+">",i,Fore.BLACK+"-------------------------------")
        print (Fore.YELLOW+"<",totInputsFrunt,Fore.YELLOW+"-------------------------------")
        i = 0
        return
    
    if Part == 2:
        i = totInputsFrunt
        while i != totInputsFrunt + TotInputsBack - 1:
            i = i + 1
            print (Fore.BLACK+">",i,Fore.BLACK+"-------------------------------")
        i = 0
        return

    if Part == 3:
        print (Fore.BLUE+"###################################")
        inp = input (Fore.BLUE+"enter your input: ")
        clearConsole()
        return inp
    
def LoadingBar(num1, num2):
    clearConsole()
    percentage = int(round((num1/num2)*100, 2))
    if percentage <= 0:
        print(f"[          ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 10:
        print(f"[#         ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 20:
        print(f"[##        ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 30:
        print(f"[###       ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 40:
        print(f"[####      ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 50:
        print(f"[#####     ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 60:
        print(f"[######    ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 70:
        print(f"[#######   ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 80:
        print(f"[########  ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 90:
        print(f"[######### ][{num1}/{num2}][{percentage}%]")
    elif percentage <= 100:
        print(f"[##########][{num1}/{num2}][{percentage}%]")