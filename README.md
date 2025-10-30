# Encriptador-Desencriptador-XOR

En el programa implementa un cifrado simple con XOR, donde cada carácter del texto se combina con una llave aleatoria formada por ceros y unos (0 y 1).
El mismo proceso se utiliza tanto para cifrar como para descifrar, ya que aplicar la operación XOR dos veces con la misma llave recupera el texto original.

Hay que tener instalado:

import random

python3

Tenemos que implementar en el codigo:

random.randint(0, 1) genera una llave aleatoria compuesta solo por ceros y unos.

ord() convierte un carácter en código numérico (ASCII).

chr() convierte el número que nos salio de nuevo en carácter.

^ aplica la operación XOR bit a bit, que se usa para cifrar y descifrar


Para ejecutar el programa ponemos en la terminal:

python xor_cipher.py

Ejemplo de ejecucion:

<img width="426" height="140" alt="image" src="https://github.com/user-attachments/assets/834b8f4c-516d-420d-a20f-ad5dc76e671b" />
