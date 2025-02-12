### File imports ###
import LinRegMath

### libary imports ###
import csv

def main(): # main function
    ArrayX, ArrayY = ReadCSVFile()
    FindLineyerEquesion(ArrayX, ArrayY)

# # # read a CSV file, retures two arracys
def ReadCSVFile(): 
    xdata = False
    ydata = False
    skip = False
    ArrayX = []
    ArrayY = []
    with open("input.csv", "r") as f: # read CSV file
        data = csv.reader(f)
        for line in data:
            for i in line: # each chericter inside of a CSV file
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
    print(f"y={m}x+{b}") # printing the m and b
    SolveForY = LinRegMath.findY(m, b, ArrayX) # can take any y=mx+b equastion and find the y from it, as an array
    SolvedYSubY = LinRegMath.SubtractTwoArrays(SolveForY, ArrayY) # subtracts the original y from the resut
    SqaredSolvedYSubY = LinRegMath.SquaredArray(SolvedYSubY) # squaring the array
    RSS = LinRegMath.SumAnArray(SqaredSolvedYSubY) # adding the array together
    print(f"RSS: {RSS}")

    

if __name__ == "__main__":
    main()