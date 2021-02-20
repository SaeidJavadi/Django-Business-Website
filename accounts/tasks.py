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