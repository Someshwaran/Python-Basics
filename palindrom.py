def check_palindrome(string):
    #converting the string to lower for checking 
    string = string.lower()
    index_front = 0 
    index_rear = len(string)-1
    
    # loop run by the half of the string lenth
    while index_front < len(string)/2:             
       #Here we checking the any character is not equal or not  
        if string[index_front] != string[index_rear]:
            print('Not a Palindrome')
            return
        index_rear -= 1
        index_front += 1
    else:
        print('Is a Palindrome')
#def check_palindrom ends

def check_palindrome_inbuild(string):
    #converting the string to lower string for checking  
    string = string.lower()
    #here reversed inbulid method is used to revers the string 
    var = ''.join(reversed(string)) 
    if string == var:
        print('Is a Palindrome from in build ')
    else:
        print('Not a Palindrome from in build ')
#def check_palindrom_inbuild ends 

def main():
    #main method for the driven method for Palindrome checkings

    #Getting the input string for Checking
    string = input(" Enter the string for  Palindrom checking ")

    #Getting the choice as input for the operations 
    choice = input('Enter the Choice to check the string where is manully or Buildin \n 1: Manully \t 2: Buildin \t')
    
    if choice == '1':
        print('This is Manully Checked ')
        check_palindrome(string)                                        #calling the manully checking method
    elif choice == '2':
        print('This is from inbuild checking using reversed() method ') # calling for the inbulid checking  method 
        check_palindrome_inbuild(string)        

#main module starts here
if __name__ == '__main__' :
    main()