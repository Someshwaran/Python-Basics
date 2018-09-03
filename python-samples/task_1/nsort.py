def inbuild_sort(input_list,type_s):
    """This method sort the list using buildin methods. 
    
    It demonstrate the sorting for list 
    """
    if type_s == '1':
        input_list.sort()
    elif type_s == '2':
        input_list.sort(reverse=True)
     
    for value in input_list:
        print(value)


def quicksort_partition(arr,low,high,type_s):
    """ Definition of the partition method. 
    
    The method to sort the list here using is quickSort Algorithm
    """
    pivot = arr[high]
    index_i = low - 1
    # checking for the type of sorting 
    # type '1' for ascending order sorting 
    if type_s == '1':
        for index_j in range(low,high):
            if arr[index_j] <= pivot:
                index_i += 1
                arr[index_i],arr[index_j] = arr[index_j],arr[index_i]
    # type '2' for descending order sorting
    elif type_s == '2':        
        for index_j in range(low,high):
            if arr[index_j] >= pivot:
                index_i += 1
                arr[index_i],arr[index_j] = arr[index_j],arr[index_i]

    arr[index_i+1],arr[high] = arr[high],arr[index_i+1]
    return index_i + 1



def quick_sort(arr,low,high,type_s):
    """Quick sort  method  """
    if low < high:
        # for the partition of the list 
        pivot_index = quicksort_partition(arr,low,high,type_s)

        # for the Quicksort first half
        quick_sort(arr,low,pivot_index-1,type_s)
        #for the Quicksort second half
        quick_sort(arr,pivot_index+1,high,type_s)

def reading_input():
    """Reading the input for the list.
    
    Reading the size of the list  
    After that reading total number of elements 
    """
    list_size = int(input('Enter the size '))
    input_list = []
    
    #reading the values
    for index in range(list_size):
        var = int(input())
        input_list.append(var)
    return input_list

def printing_after_sorted(input_list):
    """Printing method for sorted element.  
    
    printing element after the sorting 
    """      
    for value in input_list:
        print(value)



def menu_for_sorting():
    """Menu method for sorting  """
    try:                
        #reading input 
        input_list = reading_input()    
        # Reading for choice to sort by manully or using inbuild
        choice_Mor_In = input('Enter the Choice for sorting using manully or using inbuilt method \n 1: Manully \t 2: Inbuild ')
        # Reading for choice of sorting Asecending or Descending  
        choice_Asor_Des = input('Enter the Choice for Ascending sort or Descending sort \n 1: Asecending \t2: Descending ')     
         
        if not choice_Asor_Des in ['1','2']:
            print('You enter the wrong choice for ascending and decending ,\n so it\'s default run as ascending')
            choice_Asor_Des = '1'

        if choice_Mor_In == '1':
            print('This is the sorted array using quicksort ')
            # calling the quicksort 
            quick_sort(input_list,0, len(input_list)-1,choice_Asor_Des) 
            # calling the printing method  
            printing_after_sorted(input_list)                       
        elif choice_Mor_In == '2':            
            print('using the inbuild method ')
            # calling the sort method 
            inbuild_sort(input_list,choice_Asor_Des)
        else:            
            print('You Enter the wrong choice ')
    except ValueError as identifier:
        print('error ',identifier)

# main method 
def main():
    menu_for_sorting()

#main module starts here
if __name__ == '__main__' :
    main()
 
