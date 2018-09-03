def factorial_list(total_count):
    """ Method definition for calculating the factorial list. """
    initial = 1
    value = 1
    #loop for genterating the factorial number
    while initial <= total_count:
        value = value * initial
        initial += 1
    
    return value    

def input_reading():
    """Input reading method. """
    try:
        return int(input('Enter the number for theFactorial Count'))
    except Exception as identifier:
        print ('ther is issue in the reading ',identifier)
        return None

def result_of_factorial(final_value):      
    """Definition for result_of_factorial. """
    print("Factorial value  is {0}".format(final_value))

def main_functions():
    """Main_function method definition. """
    try:         
        input_value = input_reading()
        if input_value != None:            
            value = factorial_list(input_value)            
            result_of_factorial(value)
    except ValueError as identifier:
        print(' Enter the Number only , error is ',identifier)
    
def main():
    """Main module definition. """
    main_functions()

if __name__ == '__main__' :
    main()     