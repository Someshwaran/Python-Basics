def push(stack,number):
    """Method for pushing elements in to the list. """
    stack.append(number)

def poping(stack):
    """Method for poping the element from the list. """
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
    
def print_elments(stack):
    """Method for print  the  elements  from the list. """

    if len(stack) != 0:
        for value in stack:
            print(value,end=' ')
    else:
        print("is Empty")


def menu_for_stack_queue_operations():
    """Method for menu_for_stack_queue_operations.
    
    Here for stack and Queue operations
    """    
    stack =[]
    while True:     
        choice = input("Enter the choice for the operations 1: pushing\t2:pop\t3:print\t4:exit  ")         
        #for the pushing operation
        if choice == '1':
            push(stack,input("Enter the Number for Push operation ")) 
        # for the poping operation
        elif choice == '2':
            poping(stack)
        # for printing all existing element 
        elif choice == '3':
            print_elments(stack)  
            print()   
        elif choice == '4':
            break
        else:
            print('Sorry you enter the worng choice ! try next time ')


def main():
    """Main method for driven the program. """
    menu_for_stack_queue_operations()

if __name__ == '__main__' :
    main()


         
