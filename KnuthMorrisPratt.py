def kmpTable(w):
    """construct partial match table for word w"""
    if len(w) == 1:
        return [-1]
    i, p = 0, 0
    t = [-1, 0]
    # basic table
    while i < len(w):
        if w[p] == w[i - 1]:
            p += 1
            t.append(p)
            i += 1
        elif i > 0:
            p = t[p - 1]
        else:
            t.append(0)
            i += 1
    # now improve by adding more -1's
    for i in range(1,len(w)):
        if w[i] == w[t[i]]:
            t[i] = -1
    return t
    
def kmpSearch(s, w):
    """Use Knuth-Morris-Pratt to search string s for word w"""
    if s and w: # nonempty string s and nonempty word w
        t = kmpTable(w)
        sindex = 0
        windex = 0
        while sindex + len(w) <= len(s):
            if s[sindex + windex] == w[windex]:
                windex += 1
                if windex == len(w):
                    return sindex
            else:
                sindex = sindex + windex - t[windex]
                windex = max(0, t[windex])
    elif s:
        return 0 # nonempty string s and empty word w
    return -1

s = "alsdkfjahererestsherasdlfajsdl"
w = "hererestsher"
i = kmpSearch(s, w)
print(s)
for j in range(i):
    print(" ", end="")
print(w)
