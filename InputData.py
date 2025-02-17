import GUI

### libary imports ###
import csv #read csv files
from colorama import Fore, Back, Style #colloring concol
from colorama import init
import time
init(autoreset=True)

# # # read a CSV file, retures two arracys
def ReadCSVFile(FileName): 
    xdata = False
    ydata = False
    skip = False
    ArrayX = []
    ArrayY = []
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
                    if i.isalpha() == True: # checking if the data shuld be added to the X or Y acesses arrays
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

def AddManualData():
    ArrayX = []
    ArrayY = []
    while True:
        GUI.InputUI(1, 2, 1)
        print(ArrayX)
        print(ArrayY)
        print(f"to add infomration use the following commands in order")
        print(f"(+/-); to or remove data from the (x acess/ y acess)")
        print(f"(x/y); to add this data to the (x acess/ y acess)")
        print(f"(#/#); for waht avlue to add to this acesses (x acess/ y acess)")
        print(f"(+x23); is an example")
        GUI.InputUI(1, 2, 2)
        input = GUI.InputUI(3, 3, 3)

        procesedinput = input.split()
        for i in procesedinput:
            print (i)
            if i[0] == "+":
                print(i[1])
                print ("is +")
                if i[1] == "x":
                    value = int(i[2:])
                    print(f"Adding {value} to ArrayX")
                    ArrayX.append(value)
                if i[1] == "y":
                    value = int(i[2:])
                    print(f"Adding {value} to ArrayY")
                    ArrayY.append(value)