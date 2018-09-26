import threading
from multiprocessing.pool import ThreadPool
def task1(args):
	print(' task1 printing ===========',args)

def task2():
	print(' task2 printing ---------')

def main():
	count = 0
	nlp_list = [1,2,3,4,5,6,7,8,9]
	
	t1 = threading.Thread(target=task1 ,name='t1',)
	t2 = threading.Thread(target=task1, name='t2')
	l_length = len(nlp_list)
	c_count = 0
	while True:
		if c_count == 0:
			t1._args = [nlp_list[count]]
			count += 1
			t2._agrs = [nlp_list[count]]
			t1.start()
			t2.start()			
		else:			 
			# t1._args = nlp_list[count]
			if t1.is_alive():
				print('Thread one is alive')		
			else:
				print(' Thread  one is dead...')
				count += 1
				if count < l_length:
					t1._args = [nlp_list[count]]
					# t1.run()
				else:				 
					break

			if t2.is_alive():
				print('Thread two is alive')
			else:
				print('Thread two is dead....')
				count += 1
				if count < l_length:
					t2._args = [nlp_list[count]]
					t2.run()
				else:
					break
		c_count += 1
		# print(threading.get_ident())
		print(count,'\n')

	# ending with joining 	
	t1.join()
	t2.join()


if __name__ == '__main__':
	main()