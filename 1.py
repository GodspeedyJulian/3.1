A=[[1,1,0,0,1,1,0,1],
   [0,0,1,0,0,0,0,0],
   [1,0,0,1,1,1,0,0],
   [1,1,0,0,0,0,1,0],
   [1,1,0,0,0,1,1,1],
   [0,1,0,0,0,0,0,0],
   [0,1,1,0,1,1,0,0],
   [1,0,1,0,0,1,1,0]]
for i in range (8):
    Sumh=0
    for n in range (8):
        if A[i][n]==1:
            Sumh+=1
    if Sumh%2!=1:
        Yw=i
        print("the error is in row" + str(i+1))
        break
for n in range (8):
    Sumv=0
    for i in range(8):
        if A[i][n]==1:
            Sumv+=1
    if Sumv%2!=1:
        Xw=n
        print("the error is in column" + str(n+1))
        break
if A[Yw][Xw]==1:
    A[Yw][Xw]=0
else:
    A[Yw][Xw]=1
print(A)
        
