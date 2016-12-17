def split_n(lis, n):
    lis1 = []
    lis2 = []
    for i in range(len(lis)):
        if i < n:
            lis1.append(lis[i])
        else:
            lis2.append(lis[i])
    return(lis1, lis2)
