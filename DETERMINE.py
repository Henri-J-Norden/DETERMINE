from copy import deepcopy
from fractions import Fraction

LOG = False

def reduce(m, r, c):
    mn = deepcopy(m)
    mn.pop(r)
    for i in range(len(mn)):
        mn[i].pop(c)
    return mn
    

def determine(m):
    d = 0
    if len(m) == 1:
        return m[0][0]
    for r in range(len(m)):
        d += (-1)**(r+2) * m[r][0] * determine(reduce(m, r, 0))
        #print("Row {} column 1: {}".format(r+1, d))
    return d


def _getInput():
    size = [int(input("Matrix rows: "))]
    size.append(size[0])
    l = [[] for i in range(size[0])]
    if size[0] < 1:
        print("<rows> must be larger than 1!")
        return l
    for i in range(size[0]):
        while True:
            l[i] = []
            try:
                vals = input("Row " + str(i+1) + ": ")
                j = 0
                for val in vals.split(" "):
                    if "/" in val:
                        val = list(map(int, val.split("/")))
                        l[i].append(Fraction(*val))
                    else:
                        l[i].append(Fraction(float(val)))
                    j += 1
                if len(l[i]) != size[1]:
                    print("Input does not match column count! (use spaces as separators between numbers)")
                    continue
                break
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    print("Input cancelled!\n")
                    raise KeyboardInterrupt()
                print(e)
    return l

def getInput():
    while True:
        try:
            return _getInput()
        except:
            print("Input parsing failed!")


while True:
    print("\nDeterminant: {}\n".format(determine(getInput())))

