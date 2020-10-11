# this fibo optimal recursive function 
def fibononic(avalue , bvalue, nthvalue):
	# here we print the avalue 
	print(avalue, end=' ')
	if nthvalue <2:
		return None
	cvalue = avalue + bvalue
	fibononic(bvalue, cvalue, nthvalue-1)

def main():
	# this main driver method called the fibononic function 
	# this program generate the fibonoic series in the optimal way of using 
	# the space the stack and running time efficiently  
	nthvalue = input("Enter the total number of fibononic series to generate :> ")
	fibononic(0,1,int(nthvalue))

if __name__ == '__main__':
	main()
