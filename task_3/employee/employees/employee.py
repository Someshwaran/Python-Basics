from re import match, compile 
from .error.employee_error  import SalaryValueError, NameValueError, IdValueError, MailIdValueError 
class Employee:
    """This class is template to stored data of the employee data. 
    
    They are in private variable so we used setters and getters 
    """
    #patterns are required   
    name_pattern_c = compile(r"\"?([a-zA-Z ]*$)\"?")
    id_pattern_c = compile(r"\"?(^[a-zA-Z-0-9a-zA-Z]*$)\"?")
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
        if self.validating_name(name):                        
            self.__name = name.upper()
            return True
            
    def set_id(self,employee_id):
        """Setter method for the employee id. """        
        if self.validating_id(employee_id):                                           
            self.__id = employee_id.lower()
            return True        

    def set_salary(self,salary):
        """Setter method for the salary. """  
        if self.validating_salary(salary):             
            self.__salary = salary
            return True
            
    def set_mailid(self,mailid):
        """This setter for mailid setter for employee data. """
        if self.verify_email(mailid):            
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
 
        if not name:
            raise NameValueError('Name can not be empty')
                                                
        if not match(Employee.name_pattern_c,name):
            raise NameValueError('Name must only have Alphabets and space.')
        return True
     
    @staticmethod
    def validating_id(employee_id):
        """validating id is the method for the validating the id. """                
        if not employee_id:
            raise IdValueError('Employee can\'t be empty')
            
        employee_id =  employee_id.lower()                 
        if match(Employee.id_pattern_c,employee_id):                   
            return True
   
        raise  IdValueError('Employee id must be a alpha numeric.\n')
        

    @staticmethod
    def validating_salary(salary):
        """Validating salary for salary must be positive and validating the inf and nan values. """
 
        if not salary.isdigit():            
            raise SalaryValueError('Enter the integer only for salary')                
        salary = int(salary)                 
        if  salary < 0:
            raise SalaryValueError('\nSalary must be numeric and whole number.\n so your salary is not going to update.\n')
                
        return True
 
    @staticmethod
    def verify_email(mailid):
        """This Verify_email class method for mathing the email pattern. """         
        
        if not match(Employee.mailid_pattern_c,mailid):
            raise MailIdValueError('Email id is not in valid format.\nplease Enter the right format.')
            
        return True
        
  