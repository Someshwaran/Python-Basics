def Fibonnoic():
     #variables for the fibonnoic series 
     variable_a = 0
     variable_b = 1

     #loop to generate the series  
     while True:
         if variable_a != 0:
             check_variable = input('Press Enter for next value or to End give any Value')
             #checking for the next value input
             if check_variable != '':   
                 break
         print(variable_a,end=' ')
         # here the main logic of Fibonnoic series 
         variable_c = variable_a + variable_b   
         variable_a = variable_b
         variable_b = variable_c 
          
# main method 
def main():
    #function calling 
    Fibonnoic()     

#main module starts here
if __name__ == '__main__' :
    main()
 