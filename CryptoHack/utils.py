import pexpect

#Clase para manejar los colores
class Color:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	PURPLE = '\033[95m'
	ORANGE = '\033[33m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BLINK = '\033[5m'
	INVERTED = '\033[7m'
	ITALIC = '\033[3m'
	INFO = ITALIC + CYAN + "[*] "
	HEADER = BOLD + CYAN

# Clase para manejar las conexiones
class Connection:
	online = True
	offline_file = "main.py"
	default_host = "localhost"
	default_port = 1337

	@staticmethod
	def set_port(newport):
		default_port = newport
	
	@staticmethod
	def set_host(newhost):
		default_host = newhost
	
	@staticmethod
	def connect(host, port):
		return pexpect.spawn(f"nc {host} {port}")

class Math:

	@staticmethod
	def ext_euclidean(a, b):
		if a == 0:
			return b, 0, 1
		else:
			gcd,x, y = Math.ext_euclidean( b % a, a)
			return gcd, y - (b // a) * x, x
	
	@staticmethod
	def modulus (a, b):
		return (a % b)
	
	@staticmethod
	def abs(x):
		if x < 0:
			return (-x)	

class Prime:
	@staticmethod
	def isPrime(a):
		i = 2
		if a < 1:
			return False
		while i * i < a:
			if a % i == 0:
				return False
			i += 1
		return True

