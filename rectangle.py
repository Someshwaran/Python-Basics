from line import Line
class reactangle(Line):
    #for to find the area and the perimeter of the Rectangle 
    def __init__(self):
        """ 
        Here we don't want to send argument to init method because of 
        we going calculate the two values , one for length and another for breath 
        """
        super().__init__()
    
    # This method for calculating the length and breath of the rectangle
    def calculation_of_length_breath(self):
        try:

             print('Enter the co-ordinates of the length side of the rectangle ')
             #reading co-ordinates for length side  
             x1 = int(input('value for the x1 '))
             y1 = int(input('value for the y1 '))
             x2 = int(input('value for the x2 '))
             y2 = int(input('value for the y2 '))
             print('Enter the co-ordinates of the breath side of the rectangle ')
             
             #reading co-ordinates for length side  
             x3 = int(input('value for the x3 '))
             y3 = int(input('value for the y3 '))
             x4 = int(input('value for the x4 '))
             y4 = int(input('value for the y4 '))

             self.length = 0
             self.breath = 0  
             #checking the condition of the rectangle co-ordinates 
             if ( (x1 == x3) and (y1 == y3) ) or ( (x1 == x4) and (y1 == y4)):
                    # calculating the length and breath
                    super().setters(x1,y1,x2,y2)
                    self.length = super().distance_between_2_points()
                    super().setters(x3,y3,x4,y4)
                    self.breath = super().distance_between_2_points()
             elif ( (x2 == x3) and (y2 == y3) ) or ( (x2 == x4) and (y2 == y4)):  
                    # calculating the breath and length             
                    super().setters(x1,y1,x2,y2)
                    self.length = super().distance_between_2_points()
                    super().setters(x3,y3,x4,y4)
                    self.breath = super().distance_between_2_points()
             else:
                    print('It not support the rectangle co-oridinate conditions \n Better give the input as good next time ')
               
        except:
             print('Given input is a string ! give only int co-ordinates value  ')

    
    # calculating area of the rectangle
    def area_of_rectangle(self):
        print(' Area of the rectangle is ',(self.length * self.breath))
    
    # calculating the perimeter of the rectangle 
    def perimeter_of_rectangle(self):
        print(' Perimeter of the rectangle is',(2 * (self.length + self.breath)))
    

#definition of the main method starts here 
def main():

    #creating the object of the rectangle class
    reactangle_object = reactangle()

    # reading input for the co-ordinates
    reactangle_object.calculation_of_length_breath()
    #calculate the area 
    reactangle_object.area_of_rectangle()
    #calculate the perimeter 
    reactangle_object.perimeter_of_rectangle()

# main module here
if __name__ == '__main__':
    main()    
    