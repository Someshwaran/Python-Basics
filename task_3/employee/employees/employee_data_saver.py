from .employee import Employee
from .error.employee_error import  EmployeeDataIsEmpty, NameValueError, SalaryValueError, IdValueError, MailIdValueError

class EmployeeDataSaver:
    """The EmployeeDataSaver class for reading the data , storing and printing.
    
    Employee class was imported from the employee module
    """
    
    def __init__(self):
        """In init method employee class object was created for storing the data.  """
        # to store the all employee objects
        self.employee_data = []
     
    def getting_values(self):
        """This method for read and store the data for a employee in Employee class object. """        
        
        while True:
            try:                
                name = input('Enter the name of the employee ')                                                     
                emp_id = input('Enter the id ')                            
                salary = input('Enter the salary ')                
                mailid = input('Enter the mailid ')
                  
                Employee.validation_of_values(name,emp_id,salary,mailid)
                    
                if self.checking_id_existing(emp_id) is not None:
                    raise IdValueError('Employee id exist. Give another id\n')
                    
                break               
            except (NameValueError, SalaryValueError, IdValueError, MailIdValueError) as identifier:
                print(identifier,'\n')
                continue

        # entering the data of the employee to data list 
        self.employee_data.append(Employee(name,emp_id,salary,mailid))

    def checking_id_existing(self,employee_id):
        """This method is checking the id is exist or not. """
        employee_id = employee_id.lower()
        for employee in self.employee_data:
            if employee_id == employee.get_id():                                                           
                return employee
        return None


    def printing_details_of_employee(self):
        """This method is used for printing the data of the employee from the list.  """
         
        if self.employee_data:
            # iterate through the for loop
            print('\nTotal Count of Employees is ',len(self.employee_data))           
            print('Name'.ljust(20,' '),'id'.ljust(10,' '),'Salary'.ljust(15,' '),'Mail Id')
            for employee_object in self.employee_data:                
                print(employee_object.get_name().ljust(20,' '),employee_object.get_id().ljust(10,' '),str(employee_object.get_salary()).ljust(15,' '),employee_object.get_mailid())               
                
            print()    
        else:
            raise EmployeeDataIsEmpty('There is no Employee Data. \n')    
    
    def deleting_data(self):
        """This is used to delete the data in the record. """
        #reading the id to delete the record 
        if not self.employee_data:
            raise EmployeeDataIsEmpty(' Employee Data records are Empty. \n')

        employee_id = input('Enter the id ')        
        if Employee.validating_id(employee_id):
            employee = self.checking_id_existing(employee_id)
            if employee is not None:             
                print('The record has been deleted. ')
                self.employee_data.remove(employee)                
            else:            
                print('data is not avilabile.')

    def editing_records(self):
        """This method for editing the data in the records."""
        if self.employee_data:
            #reading the id for editing the record 
            employee_id = input('Enter the id ')             
            data_exist = False
            if Employee.validating_id(employee_id):
                employee = self.checking_id_existing(employee_id)
                if employee is not None:             
                    data_exist = True
        else:
            raise EmployeeDataIsEmpty(' Employee Data records are Empty. \n')

        # if data is exit then only menu will be enable
        if data_exist:
            print('\nThe record is ready to edit.')                
            while True:                    
                try:
                    print('\n Enter your choice for editing the employee ',employee.get_name(),' details \n1:name \n2:id \n3:salary \n4:mailid \n5:exit')
                    choice =  input('Enter the choice for editing.\n')

                    if choice == '1':
                        name = input('Enter the new name. ')
                        employee.set_name(name)

                    #for new id 
                    elif choice == '2':
                        new_em_id = input('Enter the id. ')
                        if self.checking_id_existing(new_em_id) is  None:
                            employee.set_id(new_em_id)
                            print('New id ',new_em_id,' has been updated.\n')   
                        else:
                            print('Employee id must be unique.')                            

                    #for new salary                                                       
                    elif choice == '3':                    
                        salary = input('Enter the salary. ')                             
                        employee.set_salary(salary)                            
                        print('Salary has benn updated.\n')                             

                    #for new mailid
                    elif choice == '4':
                        mailid = input('Enter the mail id ')
                        employee.set_mailid(mailid)                            
                        print('New mailid ',mailid,' has been updated.\n')                            

                    #for exit choice
                    elif choice == '5':
                        print('Edit completed.\n')
                        break
                    else:
                        print('Your Enter the wrong choice. ')  
                except (NameValueError, IdValueError, SalaryValueError, MailIdValueError) as identifier:
                    print(identifier,'\n')                                                                                                
        else:
            print('Record is not available for the Emplooye id ',employee_id)
        
 
def menu_for_operations():    
    """Definition of menu for operations method.

    Here we creating the object for the employee_data_saver 
    """
    employee_data_save_object = EmployeeDataSaver()
    try:
        while True:
            try:
                choice = input('enter the choice for the  \n 1: Enter the data for Emplpoyee \n 2: for printing \n 3: delete \n 4: Editing \n 5: exit \n')        
                if choice == '1':                     
                    #getting values 
                    employee_data_save_object.getting_values()
                elif choice == '2':
                    #printing all values 
                    employee_data_save_object.printing_details_of_employee()
                elif choice == '3':
                    #for deleting the data
                    employee_data_save_object.deleting_data()
                elif choice == '4':
                    #for editing the data
                    employee_data_save_object.editing_records()
                elif choice == '5':
                    print('program ends.....')
                    break
                else:
                    print('You entered wrong choice -- try again. ')
            except (EmployeeDataIsEmpty, IdValueError) as identifier:
                print(identifier,'\n')
    except (EOFError, KeyboardInterrupt):    
        print('Program stopped as forced ')
      

def main():
    menu_for_operations()
            
if __name__ == '__main__':
    main()





        


