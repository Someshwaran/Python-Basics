def factorial_list(total_count):
    initial = 1
    value = 1
    #loop for genterating the factorial number
    while initial <= total_count:
        value = value * initial
        initial += 1
    print("Factorial value for the number {0} is {1}".format(total_count,value))
# factorial definition ends 

#main method starts
def main():
    try:
        value = int ( input(" Ente the Numer for the Factorial Count "))
        factorial_list(value)
    except ValueError as identifier:
        print(' Enter the Number only , error is ',identifier)
    
    


#main module starts here
if __name__ == '__main__' :
    main()     