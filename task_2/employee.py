from re import match, compile 
import math
class Employee:
    """This class is template to stored data of the employee data. 
    
    They are in private variable so we used setters and getters 
    """
    #patterns are required   
    name_pattern_c = compile(r"\"?([a-zA-Z ]*$)\"?")
    id_pattern_c = compile(r"\"?([0-9]|[a-zA-Z-]+[0-9]|[0-9]+[-a-zA-Z]+)\"?")
    mailid_pattern_c = compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

    #pattern for the mailid, employee 
    def __init__(self,name,employee_id,salary,mailid):
        self.__name = name.upper() 
        self.__id = employee_id.lower()
        self.__salary = salary
        self.__mailid = mailid

    # setter for all attributes 
    def set_name(self,name):
        """Setter method for name. """
        if not self.validating_name(name):
            print('so your new name is not going update.\n')
            return False            
        self.__name = name.upper()
        return True
        
    def set_id(self,employee_id):
        """Setter method for the employee id. """        
        if not self.validating_id(employee_id):                              
            return False       
        self.__id = employee_id.lower()
        return True        

    def set_salary(self,salary):
        """Setter method for the salary. """  
        if not self.validating_salary(salary):
            return False
        self.__salary = salary
        return True
        
    def set_mailid(self,mailid):
        """This setter for mailid setter for employee data. """
        if not self.verify_email(mailid):
            return False
        self.__mailid = mailid
        return True
        
    # getter for all attributes 
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_salary(self):
        return self.__salary
    def get_mailid(self):
        return self.__mailid
    
    @classmethod
    def validation_of_values(cls,name, id, salary, mailid):
        """This class method is used for validating the values given by the user. """         
                     
        return (cls.validating_name(name) and  cls.validating_id(id)  and cls.validating_salary(salary) and cls.verify_email(mailid))            
        
    @staticmethod
    def validating_name(name):
        """Validating name method validate the name must have only alphabets. """
        try:
            if not name:
                raise ValueError('Name can not be empty')
                                    
            if not match(Employee.name_pattern_c,name):
                raise ValueError('Name must only have Alphabets and space.')
            return True
        except ValueError as identifier:
            print(identifier)
            return False        
    
    @staticmethod
    def validating_id(employee_id):
        """validating id is the method for the validating the id. """                
        employee_id =  employee_id.lower()         
        if match(Employee.id_pattern_c,employee_id):                   
            return True
   
        print('Employee id must be a alpha numeric.\n')
        return False

    @staticmethod
    def validating_salary(salary):
        """Validating salary for salary must be positive and validating the inf and nan values. """
        try:
            if not salary.isdigit():            
                raise ValueError('Enter the integer only for salary')                
            salary = int(salary)                 
            if  salary < 0:
                raise ValueError('\nSalary must be numeric and whole number.\n so your salary is not going to update.\n')
                
            return True
        except ValueError as identifier:
            print(identifier)
            return False

    @staticmethod
    def verify_email(mailid):
        """This Verify_email class method for mathing the email pattern. """         
        
        if not match(Employee.mailid_pattern_c,mailid):
            print('Email id is not in valid format.\nplease Enter the right format.')
            return False
        return True
        
 
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
                  
                if not Employee.validation_of_values(name,emp_id,salary,mailid):
                    raise ValueError('Give proper data. \n try next time ')
                if self.checking_id_existing(emp_id) is not None:
                    raise ValueError('Employee id exist. Give another id\n')
                    continue

                break               
            except ValueError  as identifier:
                print(identifier)
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
            print('There is no Employee Data. \n')    
    
    def deleting_data(self):
        """This is used to delete the data in the record. """
        #reading the id to delete the record 
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
                
            # if data is exit then only menu will be enable
            if data_exist:
                print('\nThe record is ready to edit.')                
                while True:                    
                    print('\n Enter your choice for editing the employee ',employee.get_name(),' details \n1:name \n2:id \n3:salary \n4:mailid \n5:exit')
                    choice =  input('Enter the choice for editing.\n')

                    if choice == '1':
                        name = input('Enter the new name. ')
                        if not employee.set_name(name):
                            continue
                                    
                    #for new id 
                    elif choice == '2':
                        new_em_id = input('Enter the id. ')
                        if self.checking_id_existing(new_em_id) is  None:
                            if not employee.set_id(new_em_id):
                                continue                                
                            print('New id ',new_em_id,' has been updated.\n')   
                        else:
                            print('Employee id must be unique.')                            

                    #for new salary                                                       
                    elif choice == '3':                    
                        salary = input('Enter the salary. ')                             
                        if not employee.set_salary(salary):
                            continue                            
                        print('Salary has benn updated.\n')                             

                    #for new mailid
                    elif choice == '4':
                        mailid = input('Enter the mail id ')
                        if not employee.set_mailid(mailid):
                            continue                                
                        print('New mailid ',mailid,' has been updated.\n')                            

                    #for exit choice
                    elif choice == '5':
                        print('Edit completed.\n')
                        break
                    else:
                        print('Your Enter the wrong choice. ')                                                                                                 
            else:
                print('Record is not available for the Emplooye id ',employee_id)
        else:
            print('Record is Empty.')
 
def menu_for_operations():    
    """Definition of menu for operations method.

    Here we creating the object for the employee_data_saver 
    """
    employee_data_save_object = EmployeeDataSaver()
    try:
        while True:
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
    except (EOFError, KeyboardInterrupt):    
        print('Program stopped as forced ')

def main():
    menu_for_operations()
            
if __name__ == '__main__':
    main()





        


