from abc import ABC, abstractmethod 
class Shape(ABC):
    """Shape is the abstract base class for all shapes. """
    
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def area(self,arg):
        """This area method is a abstract method for finding the area of the given shape."""
        print('In the area method')
    
    @abstractmethod
    def perimeter(self, arg):
        """This perimeter method is the abstract method for finding the perimeter of the shape. """
        print('In the perimeter method')


    

