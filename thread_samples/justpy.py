import os 

for it in os.scandir('E:'):
    # print('type in for ',type(it))
    if not it.name.startswith('.') and it.is_file():
        print('File name', it.name)
    else:
        print('Folder name', it.name)
print()
    # for entry in it:
    #     if not entry.name.startswith('.') and entry.is_file():
    #         print(entry.name)
    #     else:
    #     	print(entry.name)

 #      print(it)
	# print(' type ',type(it))

with os.scandir('E:') as iterator:
	print(' type in with ', type(iterator))
	for entry in iterator:
		print('type of the iterator ',type(entry))

# def folder_size(folder_path):
#     """This method for the folder scan and calculate size. """
#     total_sum = 0
#     with scandir(folder_path) as iterator:
#         for entry in iterator:
#             if not entry.name.startswith('.') and entry.is_file():                                 
#                 total_sum += path.getsize(path.join(folder_path,entry.name))                
#             else:                                
#                 total_sum += folder_walker(path.join(folder_path,entry.name))
#     return total_sum