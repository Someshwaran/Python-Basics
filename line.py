import math
class Line:
    """
        For base class Line ,it is basic for all math operations 
    """
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    #this setter method to set the co-ordinate values 
    def setters(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    # this below method gives the distance between the two points of line 
    def distance_between_2_points(self):
        variable_value =  math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        return variable_value
    