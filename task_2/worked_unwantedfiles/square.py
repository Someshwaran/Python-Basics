from line import Line
from decimal import Decimal
class square(Line):
    """This square class as to performe for finding the area and perimeter of a square.

    Square have the 4 equal sides so we need only one side  
    It derives base class as the Line 
    So we send the parmeters to the base class
    """
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        super().__init__(x1, y1, x2, y2)
    
    def area_of_square(self):
        """This method is used to find the area of the Square.  """

        #calculating the area of the square
        area_v = super().distance_between_2_points() ** 2
        #area_v = Decimal(area_v)
        print('area ',area_v)
        print(' Area of the Square is ',round(area_v,1))
        
    def perimeter_of_square(self):
        """This method is used to find the perimeter of the Square. """

        #calculating the perimater of the square 
        perimeter_v = 4 * super().distance_between_2_points()
        #perimeter_v =  Decimal(perimeter_v)
        print('perimeter ',perimeter_v)
        print(' Perimeter of the square is ',round(perimeter_v,1))


def reading_input():    
    """Reading the input. """
    print('Enter the co-ordinates of the side of the Square ')
    #reading co-ordinates for radius 
    x1 = Decimal(input('value for the x1 '))
    y1 = Decimal(input('value for the y1 '))
    x2 = Decimal(input('value for the x2 '))
    y2 = Decimal(input('value for the y2 '))

    return x1, y1, x2, y2


def main():
    """Definition of main module. """
    try:          
        #reading co-ordinates for side  
        x1, y1, x2, y2 = reading_input()
        #object creating for the Square class
        square_object = square(x1,y1,x2,y2)

        #calling the area mothed  for the area of the Square
        square_object.area_of_square()
        #calling the perimeter metod of the Square class
        square_object.perimeter_of_square()
        
    except Exception as identifier:
        print('Given input is a string ! give only int co-ordinates value  ',identifier)

if __name__ == '__main__':
    main()    