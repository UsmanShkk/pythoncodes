n = int(input())
x = input()
count = 0
for i in range(0,n-1,2):
    print(x[i],end='')
    print(x[i+1],end='')
    count += 1
    if count != (n//2):
        print('-',end='')
if (n % 2)!=0:
    print(x[-1])

