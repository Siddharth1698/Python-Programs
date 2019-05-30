def compound_interest(p,r,t):
    cii = p * pow((1+r/100),t)
    print("compound intrest is ", cii)


compound_interest(10000, 10.25, 5)
