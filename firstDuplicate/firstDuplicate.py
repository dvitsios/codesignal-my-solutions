def firstDuplicate(a):

    d = {}
    found = 0

    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

        if(d[a[i]] == 2):
            return a[i]

    if not found:
        return -1

