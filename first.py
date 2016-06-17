def convertback(num, base):
	codes = {'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15'}
	if base not in [2, 8, 10, 16]:
		raise TypeError('base number {} is not valid'.format(base))
	result = int()
	for i, j in enumerate(num, 1):
		if j in codes:
			result += int(codes[j]) * (base ** -i)
		else:
			result += int(j) * (base ** -i)
	return result

def convert(num, base):
	codes = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
	if base not in [2, 8, 16]:
		raise TypeError('base number {} is not valid'.format(base))
	result = str()
	num = '0.' + str(num)
	while True:
		num = str(float(num) * base)
		temp = num.split('.')[0]
		if int(temp) > 9:
			result += codes[temp]
		else:
			result += temp
		if not float(num) % 1:
			break
		num = '0.' + num.split('.')[1]
	return result

while True:
	num = input("Input a number (type 'bye' for quitting): ")
	if num == 'bye':
		break
	if num[0] == '-':
		k = '-'
		num = num[1:]
	else:
		k = ''
	from_base = int(input('From base: '))
	to_base = int(input('To base: '))
	if '.' in num:
		if (from_base, to_base) == (10, 2):
			print(k + (bin(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (10, 8):
			print(k + (oct(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (10, 16):
			print(k + (hex(int(num.split('.')[0])) + '.' + convert(int(num.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (2, 10):
			print(k + str((int('0b' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base)))
		elif (from_base, to_base) == (2, 8):
			temp = str((int('0b' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (oct(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (2, 16):
			temp = str((int('0b' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (hex(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (8, 2):
			temp = str((int('0o' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (bin(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (8, 10):
			print(k + str((int('0o' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base)))
		elif (from_base, to_base) == (8, 16):
			temp = str((int('0o' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (hex(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (16, 2):
			temp = str((int('0x' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (bin(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (16, 8):
			temp = str((int('0x' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base))
			print(k + (oct(int(temp.split('.')[0])) + '.' + convert(int(temp.split('.')[1]), to_base))[2:])
		elif (from_base, to_base) == (16, 10):
			print(k + str((int('0x' + num.split('.')[0], from_base)) + convertback(num.split('.')[1], from_base)))
		else:
			raise TypeError('base number {[0]} is not valid'.format(list({from_base, to_base}.difference({2,8,10,16}))))
	else:
		if (from_base, to_base) == (10, 2):
			print(k + bin(int(num))[2:])
		elif (from_base, to_base) == (10, 8):
			print(k + oct(int(num))[2:])
		elif (from_base, to_base) == (10, 16):
			print(k + hex(int(num))[2:])
		elif (from_base, to_base) == (2, 10):
			print(int(k + '0b' + num, from_base))
		elif (from_base, to_base) == (2, 8):
			print(k + (oct(int('0b' + num, from_base)))[1:])
		elif (from_base, to_base) == (2, 16):
			print(k + (hex(int('0b' + num, 10)))[2:])
		elif (from_base, to_base) == (8, 2):
			print(k + (bin(int('0o' + num, from_base)))[2:])
		elif (from_base, to_base) == (8, 10):
			print(int(k + '0o' + num, from_base))
		elif (from_base, to_base) == (8, 16):
			print(k + (hex(int('0o' + num, from_base)))[2:])
		elif (from_base, to_base) == (16, 10):
			print(int(k + '0x' + num, from_base))
		elif (from_base, to_base) == (16, 2):
			print(k + (bin(int('0x' + num, from_base)))[2:])
		elif (from_base, to_base) == (16, 8):
			print(k + (oct(int('0x' + num, from_base)))[2:])
		else:
			raise TypeError('base number {[0]} is not valid'.format(list({from_base, to_base}.difference({2, 8, 10, 16}))))
