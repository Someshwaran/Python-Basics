from threading import Thread, current_thread
import os 
import queue

class OsWalker:
    """docstring for OsWalker"""
    folder_path_list = {}
    folder_with_size = {}
    folder_path_queue = queue.Queue()

    def reading_folder(self):
        """This method for reading the folder absolute path. """       
        while True:
            print('Enter the path otherwise it ends...')
            f_path = input()
            if not os.path.isdir(f_path):
                print(' Entered input is not a folder path..\n so Tata Bye ...')
                break
            OsWalker.folder_path_list.update({f_path:'ready'})   
            OsWalker.folder_path_queue.put(f_path)
        
        
    @classmethod
    def calculating_folder_size(cls,folder_path_q):
        """This folder size method for finding the folder size using the os walk api. """
        total_sum = 0        
        # print('current thread ',current_thread().getName())        
        while True:
            # print(' in the while ')            
            f_path = folder_path_q.get()
            print(' folder path ',f_path)            
            for root_name,dirs,files_name in os.walk(f_path):
                for name in files_name:
                    # print(' file name ',name)
                    total_sum += os.path.getsize(os.path.join(root_name,name))        
            # print('t_ sum ',total_sum)            
            OsWalker.folder_with_size.update({f_path:total_sum}) 
            folder_path_q.task_done()        
            # print(' last line ')       
            
    def getting_folders_size_by_threading(self,thread_count=2):
        """This calculating folder size parallel using this method ."""
        threads = []
        
        for index in range(thread_count):
            thread = Thread(target=OsWalker.calculating_folder_size,name='thread'+str(index),args=(OsWalker.folder_path_queue,))                                    
            thread.setDaemon(True)
            thread.start()           
            threads.append(thread)

        OsWalker.folder_path_queue.join()
      
    
    def displaying_result(self):
        """This method for displaying the folder size results. """
        for key in OsWalker.folder_with_size.keys():
            print(' folder :',key,' size : ',OsWalker.folder_with_size[key])


def main_driven():
    """This method for the accessing the all method for the OsWalker class. """
    try:
        object_osw = OsWalker()

        #Reading the folder paths 
        object_osw.reading_folder()
        #Calculating the foldersize by threads.
        object_osw.getting_folders_size_by_threading(3)
        #Displaying the result
        object_osw.displaying_result()
    except (EOFError, KeyboardInterrupt):
        print('Program stopped as Forced')

def main():
    main_driven()

if __name__ == '__main__':
    main()
    