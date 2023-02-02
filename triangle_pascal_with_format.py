P = []
N = 7
for i in range(N):
    row = [1] * (i + 1)
    for j in range(i +1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1]+P[i-1][j]
    P.append(row)

for i in range(N):
    width = N-P.index(P[i])-1
    lst = [f'{{{i}:3}}' for i in range(len(P[i]))]
    st = ''
    for j in lst:
        st += j
    line = ' '* width + st.format(*P[i])
    print(line)