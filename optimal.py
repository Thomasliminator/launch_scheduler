def makearr():
    arr = []
    arr.append("Bear I April 1")
    arr.append("Orca I April 3")
    arr.append("Moose I April 5")
    arr.append("Bear II April 10")
    arr.append("Bumblebee I April 12")
    arr.append("Bumblebee II April 13")
    arr.append("Bumblebee III April 14")
    arr.append("Bumblebee IV April 15")
    arr.append("Orca II April 20")
    arr.append("Moose II April 23")
    arr.append("Bear III April 30")
    arr2 = []
    for x in arr:
        curr = x.split(" ")
        arr2.append(curr)
    return arr2

def make2d(arr):
    ret = []
    for x in arr:
        amt = []
        date = int(x[3])
        for y in range(1,31):
            if x[0] == "Bear":
                amt.append(abs(y-date)*2)
            elif x[0] == "Orca":
                amt.append(abs(y-date)*1)
            elif x[0] == "Moose":
                amt.append(abs(y-date)*7)
            else:
                amt.append(abs(y-date)*.5)
        ret.append(amt)
    return ret

first = makearr()
print(first)
#31 along x each rocket along y and cost value stored.
sec = make2d(first)
print(sec)