# Here this module for perparing the multipart content 
try:
	import os
	import sys
	import io
	import logging
	import mimetypes	
	from urllib.request import Request, urlopen 
	from uuid import uuid4
except Exception as e:
	print("There is package is missing error : {}".format(str(e)))

# class name for the working purpouse 

class MultipartGenerator(object):
	"""docstring for MultipartGenerator"""
	
	# boundary for multipart 
	multipart_boundary = uuid4().hex
	
	# Content-Type 
	content_type = "multipart/form-data; boundary={}".format(str(multipart_boundary))
	
	def __init__(self):
		super(MultipartGenerator, self).__init__()
		# self.arg = arg
		self.files = []
		self.parts = []

	def reading_files(self):
		# Reading the files from the user 
		try:
			count_of_files  = int(input("Enter the total number of file to upload "))
			for _ in range(0,count_of_files):
				file_path  = input("File path : ")
				
				# checking the entered path is file
				if not os.path.isfile(file_path):
					print("Entered path is not a file path pls Enter the file path")
					count_of_files += 1
					continue
				# append in the list 
				self.files.append(file_path)

		except Exception as e:
			print("error :>{}".format(e))
			sys.exit(0)
	
	def get_content_type(self, file_path):
		# getting the file content-type
		return mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

	def generating_multiparts(self):
		# Genreating the parts for mutlipart encoding
		self.byte_length = 0
		encode_bound = ("--{}\r\n".format(str(MultipartGenerator.multipart_boundary))).encode()
		
		self.byte_length += len(encode_bound)  
		self.parts.append(encode_bound)

		for path_  in self.files:
			# fetching the path fromt the file_lists 
			self.byte_length += len(encode_bound)  
			# self.parts.append(encode_bound)
			basename = os.path.basename(path_)
			
			content_dis = ('Content-Disposition: from-data; name="{}";  filename="{}"\r\n'.format(basename.split('.'[0]), basename)).encode()
			self.byte_length += len(content_dis)
			byte_content_type = ('Content-Type : {}\r\n\r\n'.format(str(self.get_content_type(path_)))).encode()
			self.byte_length += len(byte_content_type)
			self.parts.append(content_dis)
			self.parts.append(byte_content_type)
			# file_buffer = ''
			# print()
			with open(path_, mode="rb") as _file:
				self.file_buffer = _file.read()
				# self.file_buffer
				print("Type value {}".format(str(type(self.file_buffer))))
				print("length of the file {}".format(str(len(self.file_buffer))))

			self.byte_length += len(self.file_buffer)
			self.parts.append(self.file_buffer)
			self.byte_length += len('\r\n'.encode())
			self.parts.append('\r\n'.encode())			
			self.parts.append(encode_bound)

		# inserting the boundary in last 
		self.byte_length -= len(encode_bound)
		self.byte_length += len("--{}--\r\n".format(str(MultipartGenerator.multipart_boundary)).encode())
		self.parts[len(self.parts)-1] = "--{}--\r\n".format(str(MultipartGenerator.multipart_boundary)).encode()

		# return 

	# def conten_lenght(self):
	# 	# This method return's the content lenght of the multipart encode file 
	# 	length = 0
	# 	for var in self.parts:
	# 		if type(var) == str:
	# 			length += len(var)
	# 		else:
	# 			print(var.decode("utf-8"))
	# 			length += len(str(''.join(var.decode('utf-8'))))	
		
	# 	return length	

		"""
		Header content 
		POST /something HTTP/1.1
		Content-Type: multipart/form-data; boundary=------------070002080409050901090203
		Host: domain
		Content-Length: 546 """

def connection():
	# Connecting the server for the testing the multipart file uplaoding 
	multipart_object = MultipartGenerator()

	# reading file 
	multipart_object.reading_files()

	# genreating parts
	# data_parts = 
	multipart_object.generating_multiparts()
	print('Total byte_length {}'.format(str(multipart_object.byte_length)))
	# creating headers 
	headers = {
				'Content-Type': MultipartGenerator.content_type,
				'Content-Length':multipart_object.byte_length}
	# url 
	URL = 'http://vijay-7433.csez.zohocorpin.com:8080'

	try:
		request_ = Request(url= URL,  data =multipart_object.parts ,headers= headers,  method= "POST")
		response = urlopen(request_)
		print("response of the multipart receiver {}".format(str(response.read().decode('utf-8'))))
	except Exception as e:
		print("error in connection {}".format(str(e)))


def main():
	# main method for the multipart uploader
	# calling Connection 
	connection()


if __name__ == '__main__':
		main()	







