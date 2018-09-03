""" Definition of the method Byte to KiolByte Conversion. """
from decimal import Decimal  

def result_printing(result_string):
    """Result printing method. """
    print(result_string)

def byte_to_readable_format(number):
    """ This byte to readable format method is performing the operation. """
    #this are the data size list 
    data_size = ['BYTE','KB','MB','GB','TB','PB','EB','ZB','YB']

    #try except for handling the Not a Number format Exception 
    try:
        list_index = 0
        result = 0             
        # checking size is Neagtive value or not  
        if number < 0:
            print('Enter the Size in positive value')
            return  None  
        
        if number < 1024:                
            variable = str(number)        
            return variable +' '+ data_size[list_index]
      
        list_index += 1 

        try:
            # loop for find the readable size of given input          
            while True:
                result = number / 1024                            
                result = round(result,5)            
                if result >= 1024:
                    number = result
                    list_index += 1
                    continue 

                string = str(result)
                if len(string) == 3 and string[2] == '0':                
                    return  string[0] +' '+data_size[list_index]
                        
                return string+' '+data_size[list_index]   
        except Exception as identiy:
            print('Size limite Exicited... please enter the size within YB ')

    except ValueError as identifier:
        print('Check your input is a Number or Not ',identifier)
# end of the byte_to_readable_format method 

def input_reading():
    """This reading the input for bytes. """
    try:
        return Decimal(input('Enter the Byte Value'))
    except Exception as identifier:
        print('Check your input is a Number or Not otherwise limit exceeded ')
        return None

def main_functions():
    """ In main_function method is use for calling all operation methods. """
    try:
        input_value = input_reading()
        if input_value != None:
            result_string = byte_to_readable_format(input_value)
            if result_string != None:
                result_printing(result_string)
    except ValueError as identifier:
        print('Check your input is a Number or Not otherwise limit exceeded ',identifier)
   
def main():
    """ The main method has used to call the main_function method. """
    main_functions()

if __name__ == '__main__' :
    main()
  

 