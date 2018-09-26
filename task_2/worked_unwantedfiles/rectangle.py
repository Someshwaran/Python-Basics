from line import Line
from decimal import Decimal
class reactangle(Line):
    """This class for to find the area and the perimeter of the Rectangle. 

    It derives base class as the Line
    """        
    def __init__(self):
        """Here we don't want to send argument to init method.
        
        Because of we going calculate the two values
        One for length and another for breath 
        """
        self.x1 = 0
        self.x2 = 0 
        self.x3 = 0 
        self.x4 = 0
        self.y1 = 0 
        self.y2 = 0 
        self.y3 = 0 
        self.y4 = 0 
        super().__init__()

    
    def reading_inputs(self):
        """Reading the input for the length and breath coordinates. """
        try:            
            print('Enter the co-ordinates of the length side of the rectangle ')
            #reading co-ordinates for length side  
            self.x1 = Decimal(input('value for the x1 '))
            self.y1 = Decimal(input('value for the y1 '))
            self.x2 = Decimal(input('value for the x2 '))
            self.y2 = Decimal(input('value for the y2 '))
            print('Enter the co-ordinates of the breath side of the rectangle ')     
            #reading co-ordinates for length side  
            self.x3 = Decimal(input('value for the x3 '))
            self.y3 = Decimal(input('value for the y3 '))
            self.x4 = Decimal(input('value for the x4 '))
            self.y4 = Decimal(input('value for the y4 '))
            return 'success'
        except Exception as identifier:
            print('Given input is a string ! try next time ',identifier)
            return None
        
    def calculation_of_length_breath(self):
        """This method for calculating the length and breath of the rectangle. """
        try:             
            self.length = 0
            self.breath = 0  
            #checking the condition of the rectangle co-ordinates 
            if ((self.x1 == self.x3) and (self.y1 == self.y3)) or ((self.x1 == self.x4) and (self.y1 == self.y4)):
                # calculating the length and sbreath
                super().setters(self.x1,self.y1,self.x2,self.y2)
                self.length = super().distance_between_2_points()
                super().setters(self.x3,self.y3,self.x4,self.y4)
                self.breath = super().distance_between_2_points()
            elif ((self.x2 == self.x3) and (self.y2 == self.y3)) or ((self.x2 == self.x4) and (self.y2 == self.y4)):  
                # calculating the breath and length             
                super().setters(self.x1,self.y1,self.x2,self.y2)
                self.length = super().distance_between_2_points()
                super().setters(self.x3,self.y3,self.x4,self.y4)
                self.breath = super().distance_between_2_points()
            else:
                print('It not support the rectangle co-oridinate conditions \n Better give the input as good next time ')

        except ValueError as identifier:
             print('Given input is a string ! give only int co-ordinates value  ',identifier)
       
    def area_of_rectangle(self):
        """Calculating area of the rectangle. """
        value = Decimal((self.length + self.breath))        
        print(' Area of the rectangle is ',(round(value,2)))
        
    def perimeter_of_rectangle(self):
        """Calculating the perimeter of the rectangle.  """
        value = Decimal(2 * (self.length + self.breath))        
        print(' Perimeter of the rectangle is',round(value,2))
    
def operations():
    """Definition of the operations method.  """

    #creating the object of the rectangle class
    reactangle_object = reactangle()    
    # reading input for the co-ordinates
    if reactangle_object.reading_inputs() != None:
        #calculation for length and breath 
        reactangle_object.calculation_of_length_breath()
        #calculate the area 
        reactangle_object.area_of_rectangle()
        #calculate the perimeter 
        reactangle_object.perimeter_of_rectangle()

def main():
    operations()

if __name__ == '__main__':
    main()    
    