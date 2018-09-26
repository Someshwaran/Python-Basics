  
class employee_data_saver:
    """The employee_data_saver class for reading the data , storing and printing.
    
    Employee class was imported from the employee module
    """
    # to store the all employee objects
    employee_data = []

    def __init__(self):
        """In init method employee class object was created for storing the data.  """
        self.employee_d = Employee()

    def getting_values(self):
        """This method for read and store the data for a employee in Employee class object. """        
        while True:
            value = input('Enter the name of the employee ')
            if value == '':
                print('Don\'t skip the data')
                continue
            else:
                self.employee_d.set__name(value)
                
            value = input('Enter the id ')
            if value == '':
                print('Don\'t skip the data')
                continue
            else:
                self.employee_d.set__id(value)
                
            value = input('Enter the salary ')
            if value == '':
                print('Don\'t skip the data')
                continue
            else:
                self.employee_d.set__salary(value)
                
            value = input('Enter the mailid ')
            if value == '':
                print('Don\'t skip the data')
                continue
            else:                    
                self.employee_d.set__mailid(value)

                break

        # entering the data of the employee to data list 
        employee_data_saver.employee_data.append(self.employee_d)
                
    def printing_details_of_employee(self):
        """This method is used for printing the data of the employee from the list.  """

        # iterate through the for loop
        for employee_object in self.employee_data:
            print()
            print('Name  : ',employee_object.get__name())
            print('Id : ',employee_object.get__id())
            print('Salary : ',employee_object.get__salary())
            print('Mail_ID  : ',employee_object.get__mailid())
            print()
         

def main():    
    """Definition of main method.

    Here we creating the object for the employee_data_saver 
    """
    while True:
        choice = input('enter the choice for the  \n 1: Enter the data for Emplpoyee \n 2: for printing ')
        employee_data_save_object = employee_data_saver()
        if choice == '1':         
            #getting values 
            employee_data_save_object.getting_values()
        elif choice == '2':
            #printing all values 
            employee_data_save_object.printing_details_of_employee()
        elif choice == '3':
            print('program ends.....')
            break
        else:
            print('You entered wrong choice -- try again. ')
            
if __name__ == '__main__':
    main()





        

