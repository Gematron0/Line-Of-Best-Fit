import LinRegMath

def main():
    ArrayX = [1.5, 2, 2.5, 3, 3.5]
    ArrayY = [0.8, 1.3, 1.5, 1.9, 2.5]
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