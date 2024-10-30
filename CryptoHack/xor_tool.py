from utils import Color

print(Color.BOLD +Color.GREEN + "XOR Tools")
print(Color.END+Color.GREEN +"By FamilyBoggart\n"+Color.END)
def exercise_data():
	flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104" 
	flag = convert_to_bytes(flag)
	return(flag)

def convert_to_bytes(n):
	if isinstance(n, str):
		n = bytes.fromhex(n)
	if isinstance(n, int):
		n = long_to_bytes(n)
	return n
def xor_conmutative():
	k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
	k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
	k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
	f_k1_k2_k3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
	return k1, k2_k1, k2_k3, f_k1_k2_k3


#Utils

def long_to_bytes(n):
	return n.to_bytes((n.bit_length() + 7) // 8, 'big')

def bytes_to_long(b):
	return int.from_bytes(b, 'big')

#XOR 1 Byte
def xor_1_byte(first, second):
	data = b''
	for i in range(len(first)):
		data += (first[i] ^ second).to_bytes(1, 'big')
	return data

def iterate_all_bytes(flag):
	xor_byte = []
	for byte in range(256):
		xored = xor_1_byte(flag, byte)
		xor_byte.append(xored)
	return xor_byte

def xor_every_byte(flag, key):
	data = b''
	for i in range(len(flag)):
		data += (flag[i] ^ key[i % len(key)]).to_bytes(1, 'big')
	return data


def menu():
	print(Color.BOLD + Color.BLUE + "Menú")
	print("1) Configurar el formato de la flag")
	print("2) Configurar una key")
	print(Color.END + Color.BLUE+ f"\t21) Configurar una key como un entero"+ Color.BOLD)
	print("3) Realizar XOR sobre un byte")
	print("4) Realizar XOR flag ^ Key")
	print("5) Realizar propiedad conmutativa")
	print("6) Mis datos")
	print("7) Deducir Flag a partir del formato")
	print("8) Cambiar flag")
	print("0) Salir")
	print(Color.END)
	option = int(input("Opción > "))
	print()
	return option


def main():
	flag = exercise_data()
	flag_format = None
	key = None
	option = menu()
	while option != 0:
		if not flag_format:
			print(Color.INFO + "Primero configuraremos el formato de la flag")
			option = 1
		if option == 1:
			flag_format = input("Flag > ")
			print(f"Flag formateada: {flag_format}")
		
		if option == 2:
			key = input("Key > ")
			print(f"Key: {key}")
		
		if option == 21:
			key = int(input("Key > "))
			print(f"Key: {key} ")
		
		elif option == 3:
			xored = iterate_all_bytes(flag)
			solution = False
			for b in range(256):
				if xored[b].startswith(flag_format.encode()):
					print(f"Flag encontrada: {xored[b]}")
					solution = True
					break
			if not solution:
				print("No se encontró la flag")
				for b in range(256):
					print(f"Byte {b}: {xored[b]}")
		
		elif option == 4:
			key = convert_to_bytes(key)
			xored = xor_every_byte(flag, key)
			print(f"Flag: {xored}")
		
		elif option == 5:
			k1, k2_k1, k2_k3, f_k1_k2_k3 = xor_conmutative()
			k1 = bytes.fromhex(k1)
			k2_k3 = bytes.fromhex(k2_k3)
			f_k1_k2_k3 = bytes.fromhex(f_k1_k2_k3)
			f_1 = xor_every_byte(f_k1_k2_k3, k1)
			f_2 = xor_every_byte(f_1, k2_k3)
			print(f"Flag: {f_2}")
		
		elif option == 6:
			print(Color.HEADER + "Mis datos" + Color.END)
			print(Color.GREEN)
			print(f"Flag: {flag}")
			print(f"Formato: {flag_format}")
			print(f"Key: {key}")
			print(Color.END)
		
		elif option == 7:
			xored = xor_every_byte(flag, flag_format.encode())
			if xored.startswith(b'\x00' * len(flag_format)):
				print(f"Esta cadena cumple el formato de la flag:\n"+Color.ORANGE+ f"{xored}"+Color.END)
			else:
				print("Realiza XOR con el formato produce esto: \n"+Color.RED+f"{xored}"+Color.END)
		
		elif option == 8:
			flag = input("New flag > ").encode()
		print()	
		option = menu()

main()
