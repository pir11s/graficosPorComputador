class Cors:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def slope_intercept(x1,y1,x2,y2):
    L = []
    if x2<x1:
        x1,y1,x2,y2 = x2,y2,x1,y1
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    swap_x_y = False
    if x1 == x2:
        m = 0
    else:
        m = dy / dx
    if m > 1:
        swap_x_y = True
        x,y,x1,x2,y1,y2 = y,x,y1,y2,x1,x2
        m = 1 / m
    b = y - m * x1
    while(x<=x2):
        if x1 == x2:
            L.append(Cors(x1,y))
        elif y1 == y2:
            L.append(Cors(x,y1))
        else:
            L.append(Cors(x,y))
        
        x = x+1
        y = round(m*x+b)
    if (swap_x_y):
        for cors in L:
            cors.x,cors.y = cors.y,cors.x 
    return L


L = slope_intercept(5,3,8,12)
for cors in L:
    print ("x: " +  str(cors.x) +", " + "y:" + str(cors.y))