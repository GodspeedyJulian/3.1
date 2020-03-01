def weight(Weight):
    if Weight == 3:
        Weight=1
    else:
        Weight=3
    return Weight
Weight=1
total=0
for i in range(12):
    digit=int(input('digit: '))
    value=digit*Weight
    total+=value
    Weight=weight(Weight)
r=total%10
c=10-r
print('校验码为: ' +str(c))
