# here for satack and Queue operations 
stack =[]
#method for pushing elements starts
def push(number):
    stack.append(number)
# method ends

# poping methods starts 
def poping():
    try:
        # checking for containner is empty or not
        if len(stack) != 0:
             choice =  input('Enter the choice for the pop at front or end \n 1: front \t2: end ')
             if choice == '1':
                print(stack[0])
                del stack[0]                # deleting front element for Queue operation  
             elif choice == '2':
                print(stack.pop())          # deleting top element for the stack operations 
             else:
                print('Sorry you enter the worng choice ! try next time ')
            
        else:
            print('is Empty ')
    except ValueError as identifier:
        print('error ',identifier)
    
# method ends 

#print_ elements method starts 
def print_elments():
    if len(stack) != 0:
        for value in stack:
            print(value,end=' ')
    else:
        print("is Empty")
#method ends 

#main method starts
def main():
     while True:     
         choice = input("Enter the choice for the operations 1: pushing\t2:pop\t3:print\t4:exit  ")
         
         #for the pushing operation
         if choice == '1':
             push(input("Enter the Number for Push operation ")) 
         # for the poping operation
         elif choice == '2':
             poping()
        # for printing all existing element 
         elif choice == '3':
             print_elments()  
             print()   
         elif choice == '4':
            break
         else:
            print('Sorry you enter the worng choice ! try next time ')
#end of the stack operations

#main module starts here
if __name__ == '__main__' :
    main()


         
