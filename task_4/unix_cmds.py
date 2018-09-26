from os import system, path, walk, listdir 

def reading_required_paths():
    """This is method we going to read the path from user. """    
    while True:
        # reading file absolute path
        file_path = input('Enter the file absolute path ')
        if not path.isfile(file_path):
            print('The file path or file not exists ')
            continue
        break
    while True:    
        #reading folder path
        folder_path = input('Enter the folder absolute path ')
        if not path.isdir(folder_path):
            print('The folder path is not exist or not a folder')
            continue
        break
    return file_path, folder_path
  

def folder_size(folder_path):
    """This method for calculating the folder size. """
    total_sum = 0    
    for root_name,dirs,files_name in walk(folder_path):
        for name in files_name:            
            total_sum += path.getsize(path.join(root_name,name))
    
    return total_sum

def folder_contains(folder_path):
    """This folder_contains mthod uses the os module lisdir for the listing the files and folders from the given folder. """
    for name in listdir(folder_path):
        print(name)

def unix_cmd_executer():
    """This method is going to execute the basic unix commands like 'ls', 'cat'. """
    try:
        file_path, folder_path  = reading_required_paths()
        #getting the file size 
        print('\nFile size is ',path.getsize(file_path),' bytes and file path is ',file_path)
        #printing the all files and folder using unix cmds         
        print('\nList of the files and folder from the root folder : '+folder_path,'\n')
        folder_contains(folder_path)        
        #Calculating the total size of the root folder
        print('\nThe size of the root folder ',folder_path,' is ',folder_size(folder_path),' bytes')
         
    except (EOFError, KeyboardInterrupt, OSError) :
        print('\nProgram stopped as forced')

def main():
    unix_cmd_executer()

if __name__ == '__main__':
    main()


