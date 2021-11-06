import math
class Cors:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def digital_differential_analyzer(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    m =   max([abs(dx),abs(dy)])  
    dx2 = dx / m
    dy2 = dy / m
    x = x1 + 0.5
    y = y1 + 0.5
    i = 0
    L = []
    while i < m:
        L.append(Cors(math.floor(x),math.floor(y)))
        x = x + dx2
        y = y + dy2
        i = i + 1
    return L

L = digital_differential_analyzer(0,0,-8,-4)
print("points x1: 0, y1: 0")
print("points x2: -8, y2: -4")
for cors in L:
    print ("x: " +  str(cors.x) +", " + "y:" + str(cors.y))