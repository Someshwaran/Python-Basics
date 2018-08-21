def Fibonnoic(max_number):
     #variables for the fibonnoic series 
     variable_a = 0
     variable_b = 1
     initial_v = 1 
     #loop to generate the series  
     while initial_v <= max_number:
         yield variable_a
         initial_v += 1 
         #print(variable_a,end=' ')
         # here the main logic of Fibonnoic series 
         variable_c = variable_a + variable_b   
         variable_a = variable_b
         variable_b = variable_c 
          
# main method 
def main():
    try:
        value_i = int (input('Enter the value for the fibonnoic series '))
        #function calling  
        for value in  Fibonnoic(value_i):
            print(value) 
    except ValueError as identifier:
        print('error is ',identifier)
        

#main module starts here
if __name__ == '__main__' :
    main()
 