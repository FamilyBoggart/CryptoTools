from Crypto.Util.number import long_to_bytes

#XOR Ejemplo 1. key = (integer)
def xor_int_key(texto, clave):
    resultado = ""
    
    # Asegurarnos de que la clave sea un número entero
    if not isinstance(clave, int):
        raise ValueError("La clave debe ser un número entero")
    
    # Iterar sobre cada caracter del texto
    for char in texto:
        ascii_valor = ord(char)
        xor_resultado = ascii_valor ^ clave
        resultado_caracter = chr(xor_resultado)
        resultado += resultado_caracter
    
    return resultado

texto_original = "label"
clave = 13

cifrado = xor_int_key(texto_original, clave)
descifrado = xor_int_key(cifrado, clave)

print(f"Texto original: {texto_original}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")

#XOR Ejemplo 2. Key = string
def xor_str(texto, clave):
    resultado = ""
    
    # Verificar que tanto el texto como la clave sean cadenas
    if not isinstance(texto, str) or not isinstance(clave, str):
        raise ValueError("Ambos parámetros deben ser cadenas")
    
    # Convertir la clave a una lista de enteros
    clave_enteros = [ord(c) for c in clave]
    
    # Iterar sobre cada caracter del texto
    for char in texto:
        # Convertir el carácter a su valor ASCII
        ascii_valor = ord(char)
        
        # Realizar el XOR entre el valor ASCII y el primer dígito de la clave
        xor_resultado = ascii_valor ^ clave_enteros[0]
        
        # Agregar el carácter cifrado al resultado final
        resultado += chr(xor_resultado)
        
        # Mover a la siguiente posición en la clave
        clave_enteros = clave_enteros[1:] + clave_enteros[:1]
    
    return resultado

def xor_str_2(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
# Ejemplo de uso

texto_original = "y0ur_p4ssword:910574"
clave = "how to use XOR"

cifrado = xor_str(texto_original, clave)
descifrado = xor_str(cifrado, clave)

print(f"Texto original: {texto_original}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")


KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 #KEY 1
KEY1_KEY2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e #KEY 1 ^ KEY 2
KEY2_KEY3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 #KEY 2 ^ KEY 3
KEY4 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf # FLAG ^ KEY 1 ^ KEY 2 ^ KEY 3

flag = k4 ^ KEY2_KEY3 ^ KEY1
print(f"flag: {long_to_bytes(flag).decode()}")
