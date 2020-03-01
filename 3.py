def sumup():
    Sum=0
    A=input("input a sequence of number: ")
    for i in range(len(A)):
        Sum+=int(A[i])
    if Sum>=100:
        Sum=Sum%100
    if Sum<10:
        A=A+"0"
    A=A+str(Sum)
    print(A)
    return A
def checksum(A):
    Sum=0
    for i in range(len(A)-2):
        Sum+=int(A[i])
    if Sum>=100:
        Sum=Sum%100
    #print(A[2:])
    if Sum==int(A[2:]):
        
        print("data correct")
    else:
        print("resend the data")
        sumup()
A=sumup()
checksum(A)
    
