import sys
import math
from cm_line.error.cmd_line_error import InvalidInputError, EmptyInputError 
def result_value(result_sum):
    """This method used to print the result of summing. """        
    print('The total sum is ',result_sum)

def isfloat(number):
    """The is float method to check the number is float or not. """
    try:
        float(number)
        return True
    except ValueError:
        return False

def validate_number(number):
    """The validate number method is to validate the string is number or not. """
    return isfloat(number)
            

def summing(number_list):
    """This method to perform addition operation to of given list. """       
    result_sum = 0                   
    for value in number_list:
        if not validate_number(value):
            raise InvalidInputError('input list as string')

        value = float(value)
        if not math.isfinite(value):            
            raise InvalidInputError('Input can\'t be Infinity ')             
        result_sum += value  

    return result_sum
    

def main(args):
    """It have the methods for functioning the addition operation. """
    try:         
        if not args[1:]:
            raise EmptyInputError('Unexpected program stopped or input not Given(No arguments are entered).\nNote : It Reads the input as command line input. ')                        
        result = summing(args[1:])     # calling the summing method from the adder module         
         
        result_value(result)        # calling the result_value method from the adder module            
    except (InvalidInputError, EmptyInputError) as error:
        print(error)
        
     
if __name__ == '__main__':
    main(sys.argv)