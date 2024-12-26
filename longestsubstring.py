s = input("")
index = 1
dicc = {}
maxx = 0
for i in range(len(s)):
    if s[i] not in dicc:
        dicc[s[i]] = index
        index +=1
    else:
        if dicc[s[i-1]] > maxx:
            maxx = dicc[s[i-1]]
        new_index = dicc[s[i]]
        keys = list(dicc.keys())[new_index:]
        dicc = {key: j + 1 for j, key in enumerate(keys)}
        dicc[s[i]] = len(dicc)+1
        index  = len(dicc)+1

if dicc[s[i]]> maxx:
    maxx = dicc[s[i]]


