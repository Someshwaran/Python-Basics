class MatrixPrinter(object):
	"""docstring for MatrixPrinter"""
	def __init__(self):
		super(MatrixPrinter, self).__init__()
		# self.arg = arg
	def add_values(self, matrix, iIndex, jIndex, value):
		# this method used to assign the values in matrix walls
		size = value + value - 1
		# print("i ",iIndex," j ",jIndex," size ",size)
		# this for top and bottom
		top = iIndex
		bottom = iIndex + size - 1
		# print("top ",top," bottom ",bottom)
		if value == 1:			
			matrix[iIndex][jIndex] = value
			return matrix
		for i in range(jIndex,size+jIndex):
			matrix[top][i] , matrix[bottom][i] = value, value
		# this for right and left
		right = jIndex
		left = jIndex + size - 1
		# print("right ",right," left ",left)
		for j in range(iIndex,size+iIndex):
			matrix[j][right] , matrix[j][left] = value, value
		return matrix

	def print_matrix(self,number_of_walls):
		# this going to print the matrix
		size = self.matrix_size(number_of_walls)
		matrix = [[0 for _ in range(size)] for _ in range(size)]
		iIndex , jIndex = 0, 0
		for value in range(number_of_walls,0,-1):
			# print("value ",value)
			matrix = self.add_values(matrix, iIndex, jIndex, value)
			iIndex += 1
			jIndex += 1
			
		# print matrix 
		for i in range(size):
			for j in range(size):
				print(matrix[i][j],end=" ")
			print("\n")
	def matrix_size(self,number_of_walls):
		n = number_of_walls-1
		n = n + number_of_walls
		return n
		
		
