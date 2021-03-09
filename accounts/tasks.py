from jdatetime import datetime as dt


def checkbirth(date):
    a = str(date)
    b = str(dt.now())
    aa = dt.strptime(a,"%Y-%m-%d")
    bb = dt.strptime(b, "%Y-%m-%d")
    c = bb - aa
    if int(c.days) >= 6575:
        return True
    else:
        return False


def checkidcode(value):
    a = int(value[-1])
    print(a)
    i = 0
    b = 0
    for num in reversed(range(2, 11)):
        b += int(value[i]) * num
        print(f'{value[i]}*{num}')
        i += 1
    c = b - (b / 11) * 11
    print(b, c)
    if c == 0 and a == c:
        return True
    elif c == 1 and a == 1:
        return True
    elif c > 1 and (a == c - 11):
        return True
    else:
        return False