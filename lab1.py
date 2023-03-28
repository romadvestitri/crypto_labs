#column's method

EN_LETTERS=''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) + ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
NUMS=''.join([chr(i) for i in range(ord('0'), ord('9')+1)])
RU_LETTERS = 'АБВГДЕЁ' + ''.join([chr(i) for i in range(ord('Ж'), ord('Я') + 1)]) + 'абвгдеё' + ''.join(
	[chr(i) for i in range(ord('ж'), ord('я') + 1)])
en_alp_len = 52
import math as m

def CheckValidTextColumn(text):
	new_instr = ''
	for let in text:
		if let in EN_LETTERS:
			new_instr += let

	return new_instr
def CheckValidKeyColumn(key):
	new_key = ''
	for let in key:
		if let in EN_LETTERS:
			new_key += let

	return new_key

def MakeMatrix(text, key):
	text = text.replace(' ', '').upper()
	key = key.upper()
	cryptomatrix = [['']*len(key) for i in range(3)]

	cryptomatrix[0] = list(key)
	temp = list(key)
	temp.sort()

	for i in range(len(temp)):
		for j in range(len(temp)):
			if (cryptomatrix[0][j] == temp[i]) and cryptomatrix[1][j] == '':
				cryptomatrix[1][j] = i+1
				break
	return cryptomatrix

def FullMatrix(cryptomatrix, text, key):
	text = text.replace(' ', '').upper()
	key = key.upper()
	k = 0
	i = 1
	row = 1
	while k < len(text):
		j = 0
		while (j <= cryptomatrix[1].index(i) and k < len(text)):
			if text[k] in EN_LETTERS:
				cryptomatrix[row+1][j] = text[k]
				j += 1
			k += 1
		i += 1
		row += 1
		if i > len(key):
			i = 1

		cryptomatrix.append(['']*len(key))

	return row-1

def Decrypt(cryptomatrix, cryptotext, key, rows):
	cryptotext = cryptotext.replace(' ', '').upper()
	key = key.upper()
	text = ''
	k = 0
	for i in range(len(key)):
		for j in range(2, rows+2):
			if cryptomatrix[j][cryptomatrix[1].index(i+1)] != '':
				cryptomatrix[j][cryptomatrix[1].index(i+1)] = cryptotext[k]
				k += 1
	for i in range(2, rows + 2):
		for j in range(len(key)):
			text += cryptomatrix[i][j]
	return text


def Encrypt(cryptomatrix, text, key, rows):
	text = text.replace(' ', '').upper()
	key = key.upper()
	cryptotext = ''
	for i in range(len(key)):
		for j in range(2, rows+2):
			cryptotext += cryptomatrix[j][cryptomatrix[1].index(i+1)]
	return cryptotext

def PrintMatrix(cryptomatrix, text, key, rows):
	text = text.replace(' ', '').upper()
	key = key.upper()
	for i in range(rows+2):
		for j in range(len(key)):
			print(cryptomatrix[i][j], end = ' ')
		print()

text='ромик'
key='bcad564'

Matrix = MakeMatrix(text, key)
rows = FullMatrix(Matrix, text, key)
cryptotext = Encrypt(Matrix, text, key, rows)
PrintMatrix(Matrix, text, key, rows)
print(len(cryptotext))

Matrix = MakeMatrix(cryptotext, key)
rows = FullMatrix(Matrix, cryptotext, key)
text = Decrypt(Matrix, cryptotext, key, rows)
print(text)



#PrintMatrix(Matrix, 'LLMHLOOIEEWRSD', 'BCAD', rows)
#print(Encrypt(Matrix, 'LLMHLOOIEEWRSD', 'BCAD', rows))



#vigener's method

def CheckKeyVig(key):
	newkey = ''
	for sym in key:
		if sym in RU_LETTERS:
			newkey += sym

	return newkey
	

def MakeTable():
	table = [['']*34 for i in range(34)]
	sym = ord('А')
	for i in range(1,34):
		if sym == 1026:
			sym = ord('Ж')
		table[0][i] = chr(sym)
		#table[i][0] = chr(sym)
		if chr(sym) == 'Е':
			sym = 1024
		sym += 1 

	k = 1
	for i in range(1,34):
		for j in range(1,34):
			if k == 34:
				k = 1
			table[i][j] = table[0][k]
			k += 1
		if k >= 33:
			k = 2
		else:
			k += 1


	for i in range(34):
		for j in range(34):
			print(table[i][j], end = '')
		print()
	return table

def EncryptV(text, key, table):
	text = text.upper()
	key = key.upper()
	textmod = text.replace(' ', '').upper()
	keymod = ''
	k = 0
	for i in range(len(text)):
		if text[i] in table[0]:
			keymod += key[k]
			k += 1
		else:
			keymod += text[i]
		if k == len(key):
			k = 0

	
	cryptotext = ''

	for i in range(len(text)):
		try:
			cryptotext += table[table[0].index(text[i])][table[0].index(keymod[i])]
		except:
			cryptotext += text[i]

	return cryptotext

def DecryptV(cryptotext, key, table):
	cryptotext = cryptotext.upper()
	key = key.upper()

	keymod = ''
	k = 0
	for i in range(len(cryptotext)):
		if cryptotext[i] in table[0]:
			keymod += key[k]
			k += 1
		else:
			keymod += cryptotext[i]
		if k == len(key):
			k = 0

	text = ''
	for i in range(len(cryptotext)):
		try:
			text += table[0][table[table[0].index(keymod[i])].index(cryptotext[i])]
		except:
			text += cryptotext[i]	
	return text


#table = MakeTable()
#cryptotext = EncryptV('САНКТ-ПЕТЕРБУРГ  –  ГОРОД СВЯТОГО ПЕТРА', 'ленин', table)
#print(cryptotext)
#print(DecryptV(cryptotext, 'ленин', table))

#decimacies method

def findModInverse(a,n):
	if m.gcd(a,n) != 1:
		return None
	u1,u2,u3 = 1, 0, a
	v1, v2, v3 = 0, 1, n

	while v3 != 0:
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (u1 -q*v1), (u2 -q*v2), (u3 - q*v3), v1, v2, v3
	return u1 % n

def CheckKeyDec(key):
	nums = '0123456789'
	new_key = ''
	for let in key:
		if let in nums:
			new_key += let

	if new_key != '':
		int_new_key = int(new_key)
		if m.gcd(int_new_key, en_alp_len) != 1:
			return None
		return str(int_new_key)
	else:
		return None

	
def Encrypt_D(text, key, n):
	
	cryptotext = ''
	text = text.lower()
	if m.gcd(int(key), n) == 1:
		for i in range(len(text)):
			if text[i] in EN_LETTERS:
				cryptotext += chr(ord('a')+(((ord(text[i])-ord('a'))*int(key)) % n))
			else: 
				cryptotext += text[i]
	else:
		print("pizda")
	print(cryptotext)
	return cryptotext

def Decrypt_D(cryptotext, key, n):
	cryptotext = cryptotext.lower()
	text = ''
	if m.gcd(int(key), n) == 1:
		for i in range(len(cryptotext)):
			if cryptotext[i] in EN_LETTERS:
				text += chr(ord('a')+(((ord(cryptotext[i])-ord('a'))*findModInverse(int(key), n)) % n))
			else:
				text += cryptotext[i]
	return text



#text = Encrypt_D('cryptography', 3, 26)

#print(Decrypt_D(text, 3, 26))













	


