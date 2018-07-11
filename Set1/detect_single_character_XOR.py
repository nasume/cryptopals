# -*- coding: utf-8 -*-
import single_byte_XOR_cipher
import os
import linecache

def main():
	contents=linecache.getlines('4.txt')
	candidate=[]
	for string in contents:
		hex_string=string[:-1].decode('hex')
		candidate.append(single_byte_XOR_cipher.Traversal_singlechar(hex_string))
	print sorted(candidate,key=lambda c:c['score'])[-1]['plaintext']


if __name__ == '__main__':
	main()