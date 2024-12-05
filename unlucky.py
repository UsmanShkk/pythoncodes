def main():
    n = int(input())
    l = input()
    new1 = list(l[:len(l)//2])
    new2 = list(l[len(l)//2:])
    new1.sort()
    new2.sort()
    if new1[0] < new2[0]:
        for i in range(len(l)//2):
            if (new1[i] > new2[i]) or (new1[i] == new2[i]):
                return "NO"
    else:
        for i in range(len(l)//2):
            if (new1[i] < new2[i]) or (new1[i] == new2[i]):
                return "NO"
    return "YES"
print(main())
