 
def check_palindrome(string):
    """ Definition of the check_palindrome method.  """
    #converting the string to lower for checking 
    string = string.lower()
    index_front = 0 
    index_rear = len(string)-1
    
    # loop run by the half of the string lenth
    while index_front < len(string)/2:             
       #Here we checking the any character is not equal or not  
        if string[index_front] != string[index_rear]:             
            return 'Not a Palindrome'

        index_rear -= 1
        index_front += 1
    return 'Is a Palindrome'         

def check_palindrome_inbuild(string):
    """ This method for checking the string is palindrome or not using inbuild methods. """
    #converting the string to lower string for checking  
    string = string.lower()
    #here reversed inbulid method is used to revers the string 
    var = ''.join(reversed(string)) 
    if string == var:        
        return 'Is a Palindrome from in build ' 

    return 'Not a Palindrome from in build '

def result_of_palidrome(result_string):
    """ This method just printing the result string of palindrome program. """
    print(result_string)

def menu_for_checking_palindrome():    
    """Menu method for checing the palindrome by manually or using inbulid methods.  """

    #Getting the input string for Checking
    string = input(" Enter the string for  Palindrom checking ").strip()
    if len(string) == 0 :
        print('Empty string can not be validate -- try next time with a string ')
        return None

    result_string = ''
    #Getting the choice as input for the operations 
    choice = input('Enter the Choice to check the string where is manully or Buildin \n 1: Manully \t 2: Buildin \t')
    
    if choice == '1':
        print('This is Manully Checked ')
        result_string = check_palindrome(string)                                        #calling the manully checking method
    elif choice == '2':
        print('This is from inbuild checking using reversed() method ')                 #calling for the inbulid checking  method 
        result_string = check_palindrome_inbuild(string)     
    else:
        print('invalid option -try next time ')
    return None   

def main_function():
    """Main method for the driven method for Palindrome checkings."""
    result_string = menu_for_checking_palindrome()
    if result_string != None:
        result_of_palidrome(result_string)

def main():
    """Main module.  """
    main_function()

if __name__ == '__main__' :
    main()