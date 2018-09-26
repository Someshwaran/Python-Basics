import math
from line import Line
from decimal import Decimal
class circle(Line):
    """This class circle is derived from the class Line.

    So we send the parmeters to the base class 
    """
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        super().__init__(x1, y1, x2, y2)
        
    def area_of_circle(self):
        """Area of the circle has been cal.  """
        area_v = 2 * math.pi * ((super().distance_between_2_points() / 2) ** 2)
        #area_v = Decimal(area_v)        
        print(' Area of the circle is ',round(area_v,1))
        
   
    def perimeter_of_circle(self):
        """perimeter of the circle to be calculated here.  """
        perimeter_v = 2 * math.pi * (super().distance_between_2_points() / 2)    
        #perimeter_v = Decimal(perimeter_v)
        print(' Perimeter of the circle is ',round(perimeter_v,1)) 

 
def reading_input():    
    """Reading the input. """
    
    print('Enter the co-ordinates of the circle diameter ')
    #reading co-ordinates for radius      
    x1 = Decimal(input('value for the x1 '))
    y1 = Decimal(input('value for the y1 '))
    x2 = Decimal(input('value for the x2 '))
    y2 = Decimal(input('value for the y2 '))
    return x1, y1, x2, y2

def main():
    try:
        #reading the input for circle coordinates       
        x1, y1, x2, y2 = reading_input()
        #creating the object for the circle class
        circle_object = circle(x1,y1,x2,y2)

        # calling the area finder method 
        circle_object.area_of_circle()
        #calling the perimeter finder method 
        circle_object.perimeter_of_circle() 
    except Exception as identifier:
        print('Given input is a string ! give only decimal co-ordinates value  ',identifier)

        
if __name__ == '__main__':
    main()  
