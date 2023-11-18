pc = [list(map(int,input().split())) for _ in range(9)]

maxNum = -1
maxIndex=[0,0]

for colIndex, row in enumerate(pc):
    maxInRow = max(row)
    if maxNum < maxInRow:
        maxIndex = [colIndex+1, row.index(maxInRow)+1]
        maxNum = maxInRow

print(maxNum)
print(" ".join(str(v) for v in maxIndex))