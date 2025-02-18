### File imports ###
import LinRegMath
import GUI
import InputData

### libary imports ###
import csv #read csv files
import os # clear the colsol
import matplotlib.pyplot as plt # plots
import numpy as np # math
from colorama import Fore, Back, Style #colloring concol
from colorama import init
init(autoreset=True)

def main(): # main function
    ArrayX = []
    ArrayY = []
    while True:
        GUI.clearConsole()
        GUI.InputUI(1, 2, 1)
        print(Fore.GREEN + f"YOUR CURRENT DATA")
        print(f"X ACESS: {ArrayX}")
        print(f"Y ACESS: {ArrayY}")
        print(Fore.GREEN + f"HOW WOULD YOU LIKE TO INPUT DATA")
        print(f"1: read form a CSV file")
        print(f"2: manualy input data")
        GUI.InputUI(1, 2, 2)
        x = GUI.InputUI(1, 2, 3)
        if int(x) == 1:
            GUI.InputUI(2, 2, 1)
            print(Fore.GREEN + f"INPUT THE CSV FILE NAME")
            GUI.InputUI(2, 2, 2)
            FileName = GUI.InputUI(2, 2, 3)
            ArrayX, ArrayY = InputData.ReadCSVFile(FileName)
        if int(x) == 2:
            ArrayX, ArrayY = InputData.AddManualData(ArrayX, ArrayY)


    ArrayX, ArrayY = InputData.ReadCSVFile()
    m, b = FindLineyerEquesion(ArrayX, ArrayY)
    plot(ArrayX, ArrayY, m, b)

# # # producing a plot
def plot(ArrayX, ArrayY, m, b):
    x = np.linspace(min(ArrayX),max(ArrayX),100)
    y = m*x+b
    plt.scatter(ArrayX, ArrayY, label= "stars", color= "green", marker= "*", s=30)
    plt.plot(x, y, '-r')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()

# # # find the lineyer requestion function
def FindLineyerEquesion(ArrayX, ArrayY):
    MeanX = LinRegMath.Mean(ArrayX) # finding the mean
    MeanY = LinRegMath.Mean(ArrayY)
    SubArrayX = LinRegMath.NumSubMean(ArrayX, MeanX) # subreacting the mean from each array
    SubArrayY = LinRegMath.NumSubMean(ArrayY, MeanY)
    BotFracArray = LinRegMath.TimesTwoArrays(SubArrayX, SubArrayY) # mutipplyes two arrays together
    TopFracArray = LinRegMath.SquaredArray(SubArrayX) # squar an array
    BotFrac = LinRegMath.SumAnArray(BotFracArray) # sum an array together
    TopFrac = LinRegMath.SumAnArray(TopFracArray)
    m = LinRegMath.FindM(BotFrac, TopFrac) # find m and b for the functiuon
    b = LinRegMath.FindB(m, MeanX, MeanY)
    print(Fore.RED + f"y={m}x+{b}") # printing the m and b
    SolveForY = LinRegMath.findY(m, b, ArrayX) # can take any y=mx+b equastion and find the y from it, as an array
    SolvedYSubY = LinRegMath.SubtractTwoArrays(SolveForY, ArrayY) # subtracts the original y from the resut
    SqaredSolvedYSubY = LinRegMath.SquaredArray(SolvedYSubY) # squaring the array
    RSS = LinRegMath.SumAnArray(SqaredSolvedYSubY) # adding the array together
    print(f"RSS: {RSS}")
    return(m, b)

    

if __name__ == "__main__":
    main()