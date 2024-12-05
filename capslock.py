s = input("")
new = s
if len(s)==1 and s.islower():
    new = s.upper()
elif s.isupper():
    new = s.lower()
elif s[0].islower() and s[1:].isupper():
    new = s[1:].lower()
    new2 = s[0].upper()
    new = new2+new
print(new)
