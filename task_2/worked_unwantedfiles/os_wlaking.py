import os
from os.path import join, getsize
total_sum = 0
for root, dirs, files in os.walk('E:\\python-samples\\'):
    print(root, "consumes", end=" ")
    total_sum += sum(getsize(join(root, name)) for name in files)
    print(total_sum, end=" ")
    print("bytes in", len(files), "non-directory files")
    print('files ',files)
    print(' directories ',dirs)
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories

print('total sum of size ',total_sum)