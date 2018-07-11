# -*- coding: utf-8 -*-

# http://www.data-compression.com/english.html
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

#获得概率分数
def get_score(string):
	score=0
	for char in string:
		char=char.lower()
		if char in CHARACTER_FREQ:
			score+=CHARACTER_FREQ[char]
	return score


#将hex的每个字符与备选密钥进行xor
def single_xor(candidate_key,hex_string):
	result=""
	for i in hex_string:
		b=chr(candidate_key^ord(i))
		result+=b
	return result

#遍历备选密钥
def Traversal_singlechar(hex_string):
	candidate=[]
	for candidate_key in range(256):
		plaintext=single_xor(candidate_key,hex_string)
		score=get_score(plaintext)
		result={
		'score':score,
		'plaintext':plaintext,
		'key':candidate_key
		}
		candidate.append(result)
	return sorted(candidate,key=lambda c:c['score'])[-1]

def main():
	#hex_string1=raw_input("input hex1:\n").decode('hex')
	string='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	hex_string1=string.decode('hex')
	result=Traversal_singlechar(hex_string1)['plaintext']
	key=chr(Traversal_singlechar(hex_string1)['key'])
	print result
	print key


if __name__ == '__main__':
	main()







