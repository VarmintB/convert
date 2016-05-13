# -*- coding: utf-8 -*-

def convertback(num, base):
	codes = {'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15'}
	if base not in [2, 8, 16]:
		raise TypeError('base number {} is not valid'.format(base))
	result = int()
	for i, j in enumerate(num, 1):
		result += int(j) * (base ** -i)
	return result
def convert(num, base):
	codes = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
	if base not in [2, 8, 16]:
		raise TypeError('base number {} is not valid'.format(base))
	result = str()
	num = '0.' + str(num)
	#print(num)
	while True:
		num = str(float(num) * base)
		temp = num.split('.')[0]
		if int(temp) > 9:
			result += codes[temp]
		else:
			result += temp
		print(num)
		if not float(num) % 1:
			break
		num = '0.' + num.split('.')[1]
		#print(num)
	return result
	
while True:
	
	num = raw_input('Input a number: ')
	from_base = input('From base: ')
	to_base = input('To base: ')
	if '.' in num:
		if (from_base, to_base) == (10, 2):
			print((bin(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (10, 8):
			print((oct(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_baze))[1:])
		elif (from_base, to_base) == (10, 16):
			print((hex(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (2, 10):
			
		elif (from_base, to_base) == (2, 8):
			
		elif (from_base, to_base) == (2, 16):
			
		elif (from_base, to_base) == (8, 2):
			
		elif (from_base, to_base) == (8, 10):
			
		elif (from_base, to_base) == (8, 16):
			
		elif (from_base, to_base) == (16, 2):
			
		elif (from_base, to_base) == (16, 8):
			
		elif (from_base, to_base) == (16, 10):
			
	else:
		if base == 2:
			print(bin(int(num))[2:])
		elif base == 8:
			print(oct(int(num))[1:])
		else:
			print(hex(int(num))[2:])
