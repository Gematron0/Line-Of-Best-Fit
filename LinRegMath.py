def Mean(Array):
    LenthOfArray = len(Array)
    sum = 0
    for i in Array:
        sum += i
    Total = sum/LenthOfArray
    return(Total)

def NumSubMean(Array, Mean):
    CompleatArray = []
    for i in Array:
        CompleatArray.append(i - Mean)
    return(CompleatArray)

def TimesTwoArrays(ArrayA, ArrayB):
    CompleatArray = []
    for i, j in zip(ArrayA, ArrayB):
        CompleatArray.append(i * j)
    return(CompleatArray)

def SquaredArray(Array):
    CompleatArray = []
    for i in Array:
        CompleatArray.append(i ** 2)
    return (CompleatArray)

def SumAnArray(Array):
    Total = 0
    for i in Array:
        Total += i
    return (Total)

def FindM(BotFrac, TopFrac):
    return (BotFrac/TopFrac)

def FindB(M, MeanA, MeanB):
    return(MeanB-(M*MeanA))

def findY(m, b, Array):
    CompleatArray = []
    for i in Array:
        CompleatArray.append((m*i)+b)
    return(CompleatArray)

def SubtractTwoArrays(ArrayA, ArrayB):
    CompleatArray = []
    for i, j in zip(ArrayA, ArrayB):
        CompleatArray.append(i - j)
    return(CompleatArray)