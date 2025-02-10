import LinRegMath

def main():
    ArrayA = [1.5, 2, 2.5, 3, 3.5]
    ArrayB = [0.8, 1.3, 1.5, 1.9, 2.5]
    MeanA = LinRegMath.Mean(ArrayA)
    MeanB = LinRegMath.Mean(ArrayB)
    SubArrayA = LinRegMath.NumSubMean(ArrayA, MeanA)
    SubArrayB = LinRegMath.NumSubMean(ArrayB, MeanB)
    BotFracArray = LinRegMath.TimesTwoArrays(SubArrayA, SubArrayB)
    TopFracArray = LinRegMath.SquaredArray(SubArrayA)
    BotFrac = LinRegMath.SumAnArray(BotFracArray)
    TopFrac = LinRegMath.SumAnArray(TopFracArray)
    m = LinRegMath.FindM(BotFrac, TopFrac)
    b = LinRegMath.FindB(m, MeanA, MeanB)
    print(f"y={m}x+{b}")

    

if __name__ == "__main__":
    main()