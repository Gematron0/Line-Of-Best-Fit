import LinRegMath

import csv

def main():
    ArrayX, ArrayY = ReadCSVFile()
    FindLineyerEquesion(ArrayX, ArrayY)

def ReadCSVFile():
    xdata = False
    ydata = False
    skip = False
    ArrayX = []
    ArrayY = []
    with open("input.csv", "r") as f:
        data = csv.reader(f)
        for line in data:
            for i in line:
                if i == "//":
                    if skip == True:
                        skip = False
                    else:
                        skip = True
                elif skip != True:
                    if i.isalpha() == True:
                        if i == "x":
                            if skip != True:
                                xdata = True
                                ydata = False
                        elif i == "y":
                            if skip != True:
                                xdata = False
                                ydata = True
                    else:
                        i = float(i)
                        if xdata == True:
                            ArrayX.append(i)
                        elif ydata == True:
                            ArrayY.append(i)
    return(ArrayX,ArrayY)

def FindLineyerEquesion(ArrayX, ArrayY):
    MeanX = LinRegMath.Mean(ArrayX)
    MeanY = LinRegMath.Mean(ArrayY)
    SubArrayX = LinRegMath.NumSubMean(ArrayX, MeanX)
    SubArrayY = LinRegMath.NumSubMean(ArrayY, MeanY)
    BotFracArray = LinRegMath.TimesTwoArrays(SubArrayX, SubArrayY)
    TopFracArray = LinRegMath.SquaredArray(SubArrayX)
    BotFrac = LinRegMath.SumAnArray(BotFracArray)
    TopFrac = LinRegMath.SumAnArray(TopFracArray)
    m = LinRegMath.FindM(BotFrac, TopFrac)
    b = LinRegMath.FindB(m, MeanX, MeanY)
    print(f"y={m}x+{b}")
    SolveForY = LinRegMath.findY(m, b, ArrayX)
    SolvedYSubY = LinRegMath.SubtractTwoArrays(SolveForY, ArrayY)
    SqaredSolvedYSubY = LinRegMath.SquaredArray(SolvedYSubY)
    RSS = LinRegMath.SumAnArray(SqaredSolvedYSubY)
    print(f"RSS: {RSS}")

    

if __name__ == "__main__":
    main()