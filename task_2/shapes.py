from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    """Shape is the abstract base class for all shapes. """
    
    @abstractmethod
    def area(self,arg):
        """This area method is a abstract method for finding the area of the given shape."""
        print('In the area method')
    
    @abstractmethod
    def perimeter(self, arg):
        """This perimeter method is the abstract method for finding the perimeter of the shape. """
        print('In the perimeter method')
         
    @staticmethod
    def reading_required_values():
        """This abstract class method for reading the value for the shape. """
        while True:
            try:           
                value = float(input())                     
                if not math.isfinite(value) or value <= 0:
                    raise ValueError()                    
                return value
            except ValueError:
                print('input type not matched \nGiven right input.')
    
    @staticmethod
    def print_result(value,operation,shape):
        """Print method for printing the result of operations. """
        print('Operation ',operation,' of the ',shape,round(value,2))


class Circle(Shape):
    """This Circle class is drived from the Base class Shape. """
    #name of thr shape
    name = 'Circle'

    def __init__(self,radius):     
        self.radius = radius
     
    def area(self):
        """Circle is arc based shape so we need radius to calculate area. """
        return  math.pi * (self.radius ** 2)

    def perimeter(self):
        """Circle is arc based shape so we need radius to calculate perimater also. """
        return 2 * math.pi * self.radius
    
    
class Rectangle(Shape):
    """Rectangle is Derived class from the base class Shape. """
    #name of the shape
    name = 'Rectangle'

    def __init__(self,length,width):                                 
        self.length = length        
        self.width = width
         

    def area(self):
        """Area method used to calculate the area of the shape rectangle. """
        return self.length * self.width
    
    def perimeter(self):
        """Perimeter of this shape is calculating here in this method. """
        return 2 * (self.length+self.width)
     

class Square(Rectangle):
    """Square class is drived from the rectangle class. 
    
    Because why we are drive the Square class from the Rectangle class,
    Similarly performing same mathematical operations  but it differes by the  values are we given  
    """
    #name of the shape
    name = 'Sqaure'

    def __init__(self,side):         
        Rectangle.__init__(self,side,side)          
         
 
def shape_operations(p_object):
    """Rectangle operations methods perform the reactangle shape operations like calculating the area and perimeter. """
    object_ = p_object    
    #getting the result for operations 
    result = object_.area()
    Shape.print_result(result,'Area',object_.name)
    result = object_.perimeter()
    Shape.print_result(result,'Perimeter',object_.name) 


def main():
    """Main method for all operations. """
    try:
        #calling the circle operations 
        print('Operations for the Circle \nReading input for the radius ')
        shape_operations(Circle(Shape.reading_required_values()))
        #calling the rectangle operations
        print('\nOperations for the Rectangle \nEnter the value for Length and Width')
        shape_operations(Rectangle(Shape.reading_required_values(),Shape.reading_required_values()))
        print('\nOperations for the Square\nEnter the side value ')
        shape_operations(Square(Shape.reading_required_values()))
    except (EOFError, KeyboardInterrupt):
        print('Program stopped as forced')
        
if __name__ == '__main__':
    main()
    

