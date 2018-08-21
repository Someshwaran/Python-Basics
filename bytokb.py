#definition of the method Byte to KiolByte Conversion
from decimal import * 
import sys
import math 
def byte_to_readable_format(number):
    #this are the data size list 
    data_size = ['KB','MB','GB','TB','PB','EB','ZB','YB']

    #try except for handling the Not a Number format Exception 
    try:
        list_index = 0
        result = 0             
        # checking size is Neagtive value or not  
        if number < 0:
            print('Enter the Size in positive value')
            return   
        
        # loop for find the readable size of given input  
        while True: 
            if number < 1024:
                print(number,'BYTES')  
                break

            result = number / 1024
            result = round(result,5)
            #print(result,' result list_idex ',list_index)
            if result > 1204:
                number = result
                list_index += 1
                continue 
            else:
                # else for constructing final string              
                string = str(result)
                if len(string) == 3 and string[2] == '0':
                    print(string[0],data_size[list_index])
                else:
                    print(string,data_size[list_index])         
                break
    except:
        print('Check your input is a Number or Not ')
# end of the byte_to_readable_format method 

#main method starts 
def main():
    try:
         byte_to_readable_format(Decimal(input('Enter the Byte value ')))
    except Exception:
        print('Check your input is a Number or Not otherwise limit exceeded',sys.exc_info())
   

#main module starts here
if __name__ == '__main__' :
    main()

 