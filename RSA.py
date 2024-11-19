import random
from sympy import mod_inverse, isprime

# Función para generar un número primo grande
def generar_primo(bits):
    while True:
        primo = random.getrandbits(bits)
        if isprime(primo):
            return primo

# Generación de claves RSA
def generar_claves(bits=1024):
    # Paso 1: Elegir dos números primos grandes
    p = generar_primo(bits)
    q = generar_primo(bits)
    
    # Paso 2: Calcular n y phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Paso 3: Elegir e (exponente público)
    e = 65537  # Valor comúnmente utilizado, coprimo con muchos phi(n)
    
    # Paso 4: Calcular d (clave privada)
    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)

# Cifrado
def cifrar(mensaje, clave_publica):
    e, n = clave_publica
    mensaje_cifrado = [pow(ord(c), e, n) for c in mensaje]
    return mensaje_cifrado

# Descifrado
def descifrar(mensaje_cifrado, clave_privada):
    d, n = clave_privada
    mensaje_descifrado = ''.join([chr(pow(c, d, n)) for c in mensaje_cifrado])
    return mensaje_descifrado

# Ejemplo de uso
if __name__ == "__main__":
    # Generar claves
    clave_publica, clave_privada = generar_claves(bits=512)
    print(f"Clave pública: {clave_publica}")
    print(f"Clave privada: {clave_privada}")
    
    # Mensaje a cifrar
    mensaje = "Hola, este es un mensaje seguro."
    print(f"Mensaje original: {mensaje}")
    
    # Cifrar el mensaje
    mensaje_cifrado = cifrar(mensaje, clave_publica)
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    
    # Descifrar el mensaje
    mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
    print(f"Mensaje descifrado: {mensaje_descifrado}")
