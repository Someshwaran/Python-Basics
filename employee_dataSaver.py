from employee import Employee 
class employee_data_saver:

        # to store the all employee objects
        employee_data = []

        def __init__(self):
            self.employee_d = Employee()

        # this method for read and store the data for a employee
        def getting_values(self):
            self.employee_d.set__name(input('Enter the name of the employee '))
            self.employee_d.set__id(input('Enter the id '))
            self.employee_d.set__salary(input('Enter the salary '))
            self.employee_d.set__mailid(input('Enter the mailid '))

            # entering the data of the employee to data list 
            employee_data_saver.employee_data.append(self.employee_d)
        
        #this method is used for printing the data of the employee from the list 
        def printing_details_of_employee(self):

            # iterate through the for loop
            for employee_object in self.employee_data:
                print()
                print('Name  : ',employee_object.get__name())
                print('Id : ',employee_object.get__id())
                print('Salary : ',employee_object.get__salary())
                print('Mail_ID  : ',employee_object.get__mailid())
                print()
        
        # to remove the details of the employee 
      #  def remove_employee_details(self,id):
      """   
        we can add the remove and update method up_coming  
      """

#definition of main method 
def main():    
    # here we creating the object for the employee_data_saver
    while True:
        choice = input('enter the choice for the  \n 1: Enter the data for Emplpoyee \n 2: for printing ')
        employee_data_save_object = employee_data_saver()
        if choice == '1':         
            #getting values 
            employee_data_save_object.getting_values()
        elif choice == '2':
            #printing all values 
            employee_data_save_object.printing_details_of_employee()
        else:
            break

#def main 
if __name__ == '__main__':
    main()





        

