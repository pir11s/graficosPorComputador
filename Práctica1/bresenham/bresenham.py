class Cors:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def bresenham(x1,y1,x2,y2):
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    m = dy / dx
    ne= 2*dy - dx
    L = []
    i = 0
    while i <= dx:
        L.append(Cors(x,y))
        while ne > 0:
            y = y + 1
            ne = ne - 2*dx
        x = x + 1
        ne = ne + 2*dy
        i = i + 1
    return L

L = bresenham(0,0,8,3)
print("points x1: 0, y1: 0")
print("points x2: 8, y2: 3")
for cors in L:
    print ("x: " +  str(cors.x) +", " + "y:" + str(cors.y))