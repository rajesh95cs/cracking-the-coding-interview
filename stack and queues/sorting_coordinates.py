class coordinate:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def __lt__(self,other):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        def __str__(self):
            out = ""
            out += "("+str(self.x) +","+str(self.y)+")" +" : "
            out += str(self.x**2 + self.y**2)
            return out


c = []
c.append(coordinate(3,5))
c.append(coordinate(2,7))
c.append(coordinate(1,4))
c.append(coordinate(6,8))
c.append(coordinate(4,3))
c.append(coordinate(9,9))
c.append(coordinate(6,8))
c.append(coordinate(2,4))
c.append(coordinate(1,8))
c.append(coordinate(4,0))
c.append(coordinate(5,5))
c.append(coordinate(7,2))
c.append(coordinate(3,9))
c.append(coordinate(0,8))
c = sorted(c)
for item in c:
    print item
