# -*- coding: utf-8 -*-

def xor_repeat_key(key,string):
	key_len=len(key)
	result=''
	str_result=''
	for index,ch in enumerate(string):
		n=index%key_len
		b=chr(ord(key[n])^ord(ch))
		str_result+=b
	return str_result


def main():
	string1='Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
	key='ICE'
	print xor_repeat_key(key,string1).encode('hex')



if __name__ == '__main__':
	main()