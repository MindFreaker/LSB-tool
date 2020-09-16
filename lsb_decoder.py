#!/usr/bin/env python3

import cv2 
import string
import argparse
import pyfiglet

class Decoder(object):
	""" LSB Decoder Steganography Tool """
	
	def __init__(self, image_file):
		self.img = cv2.imread(image_file)

	def r_decode(self):
		binary_data = ""
		rows, columns, dim = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				r_val = self.img.item(row_val,col_val,2)
				binary_data+= bin(r_val)[-1]

		msg = "".join([chr(int(binary_data[i:i+8], 2)) for i in range(0,len(binary_data),8)])
		printable_data = ""
		for i in list(msg):
			if i in string.printable:
				printable_data+=i
		print("R data: {} ".format(printable_data))

	def g_decode(self):
		binary_data = ""
		rows, columns, _ = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				g_val = self.img.item(row_val,col_val,1)
				binary_data+= bin(g_val)[-1]

		msg = "".join([chr(int(binary_data[i:i+8], 2)) for i in range(0,len(binary_data),8)])
		printable_data = ""
		for i in list(msg):
			if i in string.printable:
				printable_data+=i
		print("G data: {} ".format(printable_data))

	def b_decode(self):
		binary_data = ""
		rows, columns, _ = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				b_val = self.img.item(row_val,col_val,0)
				binary_data+= bin(b_val)[-1]

		msg = "".join([chr(int(binary_data[i:i+8], 2)) for i in range(0,len(binary_data),8)])
		printable_data = ""
		for i in list(msg):
			if i in string.printable:
				printable_data+=i
		print("B data: {} ".format(printable_data))

	def rgb_decode(self):
		binary_data = ""
		rows, columns, dim = self.img.shape
		if dim == 4:
			self.img = cv2.cvtColor(self.img, cv2.COLOR_BGRA2BGR)
		for row_val in range(rows):
			for col_val in range(columns):
				r_val = self.img.item(row_val,col_val,2)
				g_val = self.img.item(row_val,col_val,1)
				b_val = self.img.item(row_val,col_val,0)
				binary_data+= bin(r_val)[-1] + bin(g_val)[-1] + bin(b_val)[-1]

		msg = "".join([chr(int(binary_data[i:i+8], 2)) for i in range(0,len(binary_data),8)])
		printable_data = ""
		for i in list(msg):
			if i in string.printable:
				printable_data+=i
		print("RGB data: {} ".format(printable_data))

def main():
	parser = argparse.ArgumentParser(description='[+] LSB Decoder [+]')
	parser.add_argument("-i", required=True, help="Image file needed!")
	args = vars(parser.parse_args())
	decoder = Decoder(args["i"])
	#decoder.r_decode()
	#decoder.g_decode()
	#decoder.b_decode()
	#decoder.rgb_decode()


if __name__ == "__main__":
	main()