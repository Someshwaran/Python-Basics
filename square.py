from line import Line
class square(Line):
    # Square have the 4 equal sides so we need only one side 
     #so we send the parmeters to the base class
     def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
         super().__init__(x1, y1, x2, y2)

    # below method is used to find the area of the Square 
     def area_of_square(self):
        #calculating the area of the square
        area_v = super().distance_between_2_points() ** 2
        print(' Area of the Square is ',round(area_v,1))
    
    #below method is used to find the perimeter of the Square
     def perimeter_of_square(self):
        #calculating the perimater of the square 
        perimeter_v = 4 * super().distance_between_2_points()
        print(' Perimeter of the square is ',round(perimeter_v,1))

# definition of main module
def main():
    try:

         print('Enter the co-ordinates of the side of the square ')
         #reading co-ordinates for side  
         x1 = int(input('value for the x1 '))
         y1 = int(input('value for the y1 '))
         x2 = int(input('value for the x2 '))
         y2 = int(input('value for the y2 '))
         #object creating for the Square class
         square_object = square(x1,y1,x2,y2)

         #calling the area mothed  for the area of the Square
         square_object.area_of_square()
         #calling the perimeter metod of the Square class
         square_object.perimeter_of_square()

    except:
        print('Given input is a string ! give only int co-ordinates value  ')

#main module 
if __name__ == '__main__':
    main()    