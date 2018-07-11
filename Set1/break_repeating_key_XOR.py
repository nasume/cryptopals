# -*- coding: utf-8 -*-

import itertools
import linecache
import implement_repeating_key_XOR
import single_byte_XOR_cipher


def hamming_distance(a_str,b_str):
	dist=0
	for x,y in zip(a_str,b_str):
		b=bin(ord(x)^ord(y)) #转换为二进制（以字符串形式表示，如“0b100000”，0b表示二进制）
		dist+=b.count('1')
	return dist

def guess_keysize(string):
	normals=[]
	for keysize in range(2,40):
		blocks=[]
		cnt=0
		distance=0
		#根据建议获得四个block，将这四个block两两得到hamming_distance。
		for i in range(0,len(string),keysize):
			cnt+=1
			blocks.append(string[i:i+keysize])
			if cnt==4:
				break
		pairs=itertools.combinations(blocks,2)
		for (x,y) in pairs:
			distance+=hamming_distance(x,y)
		#平均一下
		distance=distance/(6.0)
		#Normalize this result by dividing by KEYSIZE.
		normal_distance=distance/keysize
		key={
		'keysize':keysize,
		'distance':normal_distance
		}
		normals.append(key)
		#print key
	#选3个最小的为待选的keysize
	candidate_keysize=sorted(normals,key=lambda c:c['distance'])[0:3]
	return candidate_keysize

def guess_key(keysize,string):
	now_str=''
	key=''
	for i in range(keysize):
		now_str=''
		for index,ch in enumerate(string):
			if index%keysize==i:
				now_str+=ch
		#获得key的第i位的值,转换为字符
		#print now_str
		key+=chr(single_byte_XOR_cipher.Traversal_singlechar(now_str)['key'])
	return key

def get_plaint(string):
	keysize_list=guess_keysize(string)
	candidate_key=[]
	possible_plaints=[]
	for keysize in keysize_list:
		key=guess_key(keysize['keysize'],string)
		#print key
		possible_plaints.append((implement_repeating_key_XOR.xor_repeat_key(key,string),key))

	'''
	for i in possible_plaints:
		print i[1]
		print get_score(i[0].decode('hex'))
		print len(i[0])
		print i[0].decode('hex')
	'''
	
	return sorted(possible_plaints,key=lambda c:single_byte_XOR_cipher.get_score(c[0]))[-1]
	#return sorted(possible_plaints,key=lambda c:get_score(c[0]))[-1]



def main():
	assert hamming_distance('this is a test', 'wokka wokka!!!') == 37
	contents=open('6.txt').read()
	#base64解码
	string=str(contents).decode('base64')
	result=get_plaint(string)
	print result[0]
	print result[1]

	





if __name__ == '__main__':
	main()