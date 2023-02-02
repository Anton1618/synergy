def pascal(N):
    P = []
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(i +1):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1]+P[i-1][j]
        P.append(row)
    for i in P:
        def func(*val): return val
        width = ' '*(len(P)-P.index(i)-1)
        val = '%3s'*len(i)
        line = (width + val) %(func(*i))
        print(line)

pascal(7)