# this module for remove the read only for the files and folder in the given folder path and deleted all the files in it
import os
import shutil
import stat
import win32security

def removeReadOnlyAccess(path=None):
    try:
        if os.path.exists(path):
            everyone=win32security.CreateWellKnownSid(win32security.WinWorldSid)            
                #Delete ace
            sd = win32security.GetNamedSecurityInfo(path, win32security.SE_FILE_OBJECT, win32security.DACL_SECURITY_INFORMATION)
            dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()    
            #print("Ace count=",dacl.GetAceCount())
            num_delete = 0
            for index in range(0, dacl.GetAceCount()):
                ace = dacl.GetAce(index)
                    
            for index in range(0, dacl.GetAceCount()):
                ace = dacl.GetAce(index-num_delete)
                if ace[2]==everyone:
                    dacl.DeleteAce(index-num_delete)
                    num_delete+=1
                
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetNamedSecurityInfo(path, win32security.SE_FILE_OBJECT, win32security.DACL_SECURITY_INFORMATION, None, None, dacl, None)
    except Exception as err:
        print("exeption {}".format(str(err)))



def remove_read_only(path=None):
    # this method is used to read only permission 
    removeReadOnlyAccess(path)
    try:
        if path is not None:
            os.chmod(path=path,mode=stat.S_IWRITE)
            os.unlink(path=path)
            print("path {} removed read only ".format(str(path)))
    except Exception as why:
        print("Exception in remove_read_only {}".format(str(why)))
def walker_over_dir(folder_path=None):
    # This method is used travase the all the folder and files inside the folder path given 
    with os.scandir(folder_path) as iterator:
        for the_path in iterator:
            print("the path {}".format(str(the_path.path)))
            if the_path.is_file():
                remove_read_only(the_path.path)
            elif the_path.is_dir():
                remove_read_only(the_path.path)
                walker_over_dir(the_path.path)


def main():
    # this main method for the trigering the file and folder permission remove.
    # read the input 
    f_path = input("Enter the file or folder path:> ")
    # out_file_path = input("\nEnter the file name to be stored :>  ")
    if os.path.isdir(f_path):
        walker_over_dir(f_path)
        shutil.rmtree(f_path)
    elif os.path.isfile(f_path):
        remove_read_only(f_path)
    else:
        print("Enter path is neither File or Folder")

if __name__ == "__main__":
    main()