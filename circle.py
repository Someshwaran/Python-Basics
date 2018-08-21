import math
from line import Line
class circle(Line):
    # this class circle is derived from the class Line 
    #so we send the parmeters to the base class
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        super().__init__(x1, y1, x2, y2)
    
    #area of the circle 
    def area_of_circle(self):
        area_v = 2 * math.pi * ((super().distance_between_2_points() / 2) ** 2)
        print(' Area of the circle is ',round(area_v,1))

    # perimeter of the circle 
    def perimeter_of_circle(self):
        perimeter_v = 2 * math.pi * (super().distance_between_2_points() / 2)    
        print(' Perimeter of the circle is ',round(perimeter_v,2)) 

# Here the main module starts 
def main():
     try:
        print('Enter the co-ordinates of the circle diameter ')
        #reading co-ordinates for radius 
        x1 = int(input('value for the x1 '))
        y1 = int(input('value for the y1 '))
        x2 = int(input('value for the x2 '))
        y2 = int(input('value for the y2 '))

        #creating the object for the circle class
        circle_object = circle(x1,y1,x2,y2)

        # calling the area finder method 
        circle_object.area_of_circle()
        #calling the perimeter finder method 
        circle_object.perimeter_of_circle() 
     except:
        print('Given input is a string ! give only int co-ordinates value  ')

        
#main module definition 
if __name__ == '__main__':
    main()