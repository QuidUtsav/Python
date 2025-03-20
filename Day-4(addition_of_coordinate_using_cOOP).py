# create the Coordinate class
class Coordinate:

    # initialize x and y attributes inside __init__()
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # define the add_coordinates() method
    def add_coordinates(self, given):
        sum_x=self.x+given.x
        sum_y=self.y+given.y
        result= Coordinate(sum_x,sum_y)
        return result
# create objects c1 and c2
c1 = Coordinate(5,6)
c2 = Coordinate(7,9)

# call the add_coordinates() method
c3 = c1.add_coordinates(c2)

# print attributes of the c3 object
print(c3.x)
print(c3.y)
