k = 0
v = 1
sum1 = 0
l = []

for i in range(0,10):
    if i%2==0:
        sum1 = k+v
        k = sum1
        l.append(sum1)
    else:
        sum1 = k+v
        v = sum1
        l.append(sum1)
print(l)