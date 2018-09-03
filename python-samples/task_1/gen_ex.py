def fibonnoic():
    """ Definition of the fibonnoic method.  """
    
    #variables for the fibonnoic series 
    variable_a = 0
    variable_b = 1       
    
    #loop to generate the series  
    while True:
        yield variable_a                
        # here the main logic of Fibonnoic series 
        variable_b = variable_a + variable_b   
        variable_a = variable_b - variable_a
                 
def reading_input():     
    """Reading the input value. """
    try:
        value_i = int (input('Enter the value for the fibonnoic series '))
        if value_i <= 0:
            print('value can not be Zero or Negative -- Give positive value ')
            return None

        return value_i
    except ValueError as identifier:
        print('error ',identifier)
        
def printing_fibonnoic(total_count):
    """Definition of the printing_fibonnoic.
    
    Here we are using the genterator     
    """     
    for _, value  in zip(range(total_count),fibonnoic()):                
        print(value)          

def main_fuctions():
    """ Defintion of the  main_function method. """
    try:
        value = reading_input()
        if value != None: 
            printing_fibonnoic(value)
    except ValueError as identifier:
        print('error is ',identifier)
        
def main():
    """Definition of the main method. """
    main_fuctions()

if __name__ == '__main__' :
    main()
 