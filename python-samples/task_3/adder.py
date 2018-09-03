 
def result_value(result_sum):
    """This method used to print the result of summing. """
    print( result_sum)


def summing(number_list):
    """This method to perform addition operation to of given list. """   
    try:
        result_sum = 0
        if len(number_list) == 0:
            result_sum = 'No arguments are entered ' 
        for value in number_list:
            result_sum += int(value)        
        return result_sum
    except ValueError as identifier:                        
        print('input list as string ',identifier)
        return None