import random
def xor(texto, clave):
    resultado = ""
    for i in range(len(texto)):
        resultado += chr(ord(texto[i]) ^ ord(clave[i % len(clave)]))
    return resultado
texto = input("Escribe el texto a cifrar: ")
llave = ''.join(str(random.randint(0, 1)) for _ in range(len(texto)))
print("Llave generada:", llave)
cifrado = xor(texto, llave)
print("Texto cifrado:", cifrado)
descifrado = xor(cifrado, llave)
print("Texto descifrado:", descifrado)
