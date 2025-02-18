import GUI

### libary imports ###
import csv #read csv files
from colorama import Fore, Back, Style #colloring concol
from colorama import init
import time
init(autoreset=True)

# # # read a CSV file, retures two arracys
def ReadCSVFile(FileName, ArrayX, ArrayY): 
    xdata = False
    ydata = False
    skip = False
    NumOfTotalChericters = 0
    NumOfChericters = 0
    with open(f"{FileName}.csv", "r") as f: # read CSV file
        data = csv.reader(f)
        for line in data:
            for i in line: # each chericter inside of a CSV file
                NumOfTotalChericters += 1
    with open(f"{FileName}.csv", "r") as f: # read CSV file
        data = csv.reader(f)
        for line in data:
            for i in line: # each chericter inside of a CSV file
                NumOfChericters += 1
                GUI.LoadingBar(NumOfChericters, NumOfTotalChericters)
                if i == "//": # checking if its requerd to skip some section of reading
                    if skip == True:
                        skip = False
                    else:
                        skip = True
                elif skip != True:
                    if i.isalpha() == True: # checking if the data shuld be added to the X or Y arrays
                        if i == "x":
                            if skip != True:
                                xdata = True
                                ydata = False
                        elif i == "y":
                            if skip != True:
                                xdata = False
                                ydata = True
                    else:
                        i = float(i) # converting the data and adding it to the array
                        if xdata == True:
                            ArrayX.append(i)
                        elif ydata == True:
                            ArrayY.append(i)
    return(ArrayX,ArrayY)

# # # lets users to add manul data
def AddManualData(ArrayX, ArrayY):
    while True:
        GUI.InputUI(1, 2, 1)
        print(ArrayX)
        print(ArrayY)
        print(f"to add infomration use the following commands in order")
        print(f"(+/-); to add or subtract enteys/numbers)")
        print(f"(x/y); to add this data to the (x acess/ y acess)")
        print(f"(##); add the numebr, another number, another number")
        print(f"(+x23,56 -y63,-12); is an example")
        print(f"x.CLEAR will creat the array")
        print(f"0 or DONE will send you back")
        GUI.InputUI(1, 2, 2)
        input = GUI.InputUI(1, 2, 3)

        procesedinput = input.split()
        for i in procesedinput:
            print (i)
            if i[0] == "+":
                if i[1] == "x":
                    value = i[2:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        x = float(x)
                        print(f"Adding {x} to ArrayX")
                        ArrayX.append(x)
                elif i[1] == "y":
                    value = i[2:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        x = float(x)
                        print(f"Adding {x} to ArrayY")
                        ArrayY.append(x)
                elif i[1] == "xy" or i[1] == "yx":
                    value = i[2:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        x = float(x)
                        print(f"Adding {x} to ArrayX and Y")
                        ArrayX.append(x)
                        ArrayY.append(x)

            elif i[0] == "-":
                print(i[1:2])
                if i[1:3] == "xi":
                    value = i[3:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        print(f"removing index {x} from ArrayX")
                        x = int(x)
                        ArrayX.pop(x)
                elif i[1:3] == "yi":
                    value = i[3:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        print(f"removing index {x} from ArrayY")
                        x = int(x)
                        ArrayY.pop(x)

                elif i[1:4] == "xyi":
                    value = i[4:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        print(f"removing index {x} from ArrayX and Y")
                        x = int(x)
                        ArrayX.pop(x)
                        ArrayY.pop(x)
                elif i[1:4] == "yxi":
                    value = i[4:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        print(f"removing index {x} from ArrayY and X")
                        x = float(x)
                        ArrayY.pop(x)
                        ArrayX.pop(x)

                elif i[1] == "x":
                    value = i[2:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        x = float(x)
                        print(f"removing {x} from ArrayX")
                        ArrayX.remove(x)
                elif i[1] == "y":
                    value = i[2:]
                    procesedvalue = value.split(',')
                    for x in procesedvalue:
                        x = float(x)
                        print(f"removing {x} from ArrayY")
                        ArrayY.remove(x)
            elif i == "x.CLEAR":
                GUI.InputUI(2, 2, 1)
                print(Fore.RED + f"YOU ARE AOBUT TO CLEAR ARRAY X; ARE YOU SHURE (Y/n)")
                GUI.InputUI(2, 2, 2)
                output = GUI.InputUI(2, 2, 3)
                if output == "Y":
                    ArrayX.clear()
            elif i == "y.CLEAR":
                GUI.InputUI(2, 2, 1)
                print(Fore.RED + f"YOU ARE AOBUT TO CLEAR ARRAY Y; ARE YOU SHURE (Y/n)")
                GUI.InputUI(2, 2, 2)
                output = GUI.InputUI(2, 2, 3)
                if output == "Y":
                    ArrayY.clear()
            elif i == "xy.CLEAR" or i == "yx.CLEAR":
                GUI.InputUI(2, 2, 1)
                print(Fore.RED + f"YOU ARE AOBUT TO CLEAR ARRAY X AND Y; ARE YOU SHURE (Y/n)")
                GUI.InputUI(2, 2, 2)
                output = GUI.InputUI(2, 2, 3)
                if output == "Y":
                    ArrayX.clear()
                    ArrayY.clear()
            elif i == "0" or i == "DONE":
                GUI.InputUI(2, 2, 1)
                print(Fore.RED + f"DO YOU WANT TO LEAVE (Y/n)")
                GUI.InputUI(2, 2, 2)
                output = GUI.InputUI(2, 2, 3)
                if output == "Y":
                    return(ArrayX, ArrayY)
