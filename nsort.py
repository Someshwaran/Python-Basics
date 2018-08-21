#it demonstrate the sorting for list 
input_list = []
def inbuild_sort(input_list,type_s):
    if type_s == '1':
         input_list.sort()
    elif type_s == '2':
        input_list.sort(reverse=True)
     
    for value in input_list:
        print(value)
#method def inbuild sort ends
""" 
    The method to sort the list here using is quickSort Algorithm 
"""
#definition of the partition method 
def quicksort_partition(arr,low,high,type_s):
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
#end of the partition method

# Quick sort method starts
def quickSort(arr,low,high,type_s):
     if low < high:
        # for the partition of the list 
        pivot_index = quicksort_partition(arr,low,high,type_s)

        # for the Quicksort first half
        quickSort(arr,low,pivot_index-1,type_s)
        #for the Quicksort second half
        quickSort(arr,pivot_index+1,high,type_s)

#main method 
def main():
     #reading the size of the list 
     list_size = int(input('Enter the size '))
     
     #reading the values
     for index in range(list_size):
        var = int(input())
        input_list.append(var)
     
     # Reading for choice to sort by manully or using inbuild
     choice_Mor_In = input('Enter the Choice for sorting using manully or using inbuilt method \n 1: Manully \t 2: Inbuild ')

     # Reading for choice of sorting Asecending or Descending  
     choice_Asor_Des = input('Enter the Choice for Ascending sort or Descending sort \n 1: Asecending \t2: Descending ')
     if choice_Mor_In == '1':
         print('This is the sorted array using quicksort ')

         # calling the quicksort 
         quickSort(input_list,0, list_size-1,choice_Asor_Des)               
         
         # printing element after the sorting 
         for index in range(list_size):
            print(input_list[index])

     elif choice_Mor_In == '2':
            print('using the inbuild method ')
            # calling the sort method 
            inbuild_sort(input_list,choice_Asor_Des)

#main module starts here
if __name__ == '__main__' :
    main()
 
