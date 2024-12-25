import math
def square():
    a, b = map(int,input().split())
    c,d = map(int,input().split())
    if a == b and c == d:
        return 'No'


    elif a == c and (b+d == a):
        return 'yes'
    elif a == d and (b+c == a):
        return 'yes'
    elif b == c and (a+d== b):
        return 'yes'
    elif b == d and ( a+c == b):
        return 'yes'
    return 'No'

def main():
    for i in range(int(input())):
        print(square())
main()
