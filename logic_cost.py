def logic_2(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 6
    elif i == 3:
        return 10
    elif i >= 4:
        k = i/4
        return 12 + 3*logic_2(k) + logic_2(i-3*k)

def logic_3(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 6
    elif i == 3:
        return 8
    elif i == 4:
        return 12
    elif i == 5:
        return 14
    elif i == 6:
        return 16
    elif i == 7:
        return 20
    elif i == 8:
        return 22
    elif i >= 9:
        k = i/3
        return 24 + 8*logic_3(k) + logic_3(i-8*k)

def logic_4(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 6
    elif i == 3:
        return 8
    elif i == 4:
        return 10
    elif i == 5:
        return 14
    elif i == 6:
        return 16
    elif i == 7:
        return 18
    elif i == 8:
        return 20
    elif i == 9:
        return 24
    elif i == 10:
        return 26
    elif i == 11:
        return 28
    elif i == 12:
        return 30
    elif i == 13:
        return 34
    elif i == 14:
        return 36
    elif i == 15:
        return 38
    elif i >= 16:
        k = i/16
        return 40 + 15*logic_4(k) + logic_4(i-15*k)
