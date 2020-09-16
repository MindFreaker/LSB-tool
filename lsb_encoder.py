#!/usr/bin/env python3

import os
import cv2 
import string
import argparse

class Encoder(object):
	""" LSB Encoder Steganography Tool """

	def __init__(self, image_file, message):
		self.image = image_file
		self.img = cv2.imread(self.image)
		self.bin_index = 0
		self.bin_data = "".join([bin(ord(message[i]))[2:].zfill(8) for i in range(len(message))])

	def save_image(self):
		file_name, ext = os.path.splitext(self.image)
		file_path = file_name + "_mod" + ext
		cv2.imwrite(file_path, self.img)


	def r_enocde(self):
		rows, columns, _ = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				r_val = self.img.item(row_val,col_val,2)         # CV2 format : R=2
				if(self.bin_index < len(self.bin_data)):
					r_mod_val = int(bin(r_val)[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
					self.img.itemset((row_val,col_val,2), r_mod_val)
		self.save_image()
	
	def g_enocde(self):
		bin_index = 0
		rows, columns, _ = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				g_val = self.img.item(row_val,col_val,1)         # CV2 format : G=1
				if(self.bin_index < len(self.bin_data)):
					g_mod_val = int(bin(g_val)[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
				self.img.itemset((row_val,col_val,1), g_mod_val)
		self.save_image()
		
	def b_enocde(self):
		bin_index = 0
		rows, columns, _ = self.img.shape
		for row_val in range(rows):
			for col_val in range(columns):
				b_val = self.img.item(row_val,col_val,0)         # CV2 format : B=0
				if(self.bin_index < len(self.bin_data)):
					b_mod_val = int(bin(b_val)[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
				self.img.itemset((row_val,col_val,0), b_mod_val)
		self.save_image()
		
	def rgb_enocde(self):
		bin_index = 0
		rows, columns, dim = self.img.shape
		if dim == 4:
			self.img = cv2.cvtColor(self.img, cv2.COLOR_BGRA2BGR)
		for row_val in range(rows):
			for col_val in range(columns):
				x = self.img[row_val,col_val]
				if(self.bin_index < len(self.bin_data)):
					r_val = int(bin(x[2])[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
				if(self.bin_index < len(self.bin_data)):
					g_val = int(bin(x[1])[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
				if(self.bin_index < len(self.bin_data)):
					b_val = int(bin(x[0])[:-1] + str(self.bin_data[self.bin_index]), 2);self.bin_index+=1
				self.img[row_val, col_val] = (b_val, g_val,r_val)
		self.save_image()


def main():
	parser = argparse.ArgumentParser(description='[+] LSB Encoder [+]')
	parser.add_argument("-i", required=True, help="Image needed!")
	parser.add_argument("-m", required=True, help="Message to be encoded!")
	args = vars(parser.parse_args())
	encoder = Encoder(args["i"], args["m"])

if __name__ == "__main__":
	main()