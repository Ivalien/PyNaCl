import os
from typing import SupportsBytes, Type, TypeVar
import nacl.bindings
from nacl import encoding
#Generacion de la semilla con numeros random de acuerdo a los datos del sistema operativo
def random(size: int = 32) -> bytes:
    return os.urandom(size)
#De acuerdo al tmaño requerido de bytes de los numeros y la semilla del sistema operativo
#La funcion randombytes_deterministic regresa un valor en raw de bytes
def randombytes_deterministic(
    size: int, seed: bytes, encoder: encoding.Encoder = encoding.RawEncoder) -> bytes:
    """
    Returns ``size`` number of deterministically generated pseudorandom bytes
    from a seed

    :param size: int
    :param seed: bytes
    :param encoder: The encoder class used to encode the produced bytes
    :rtype: bytes
    """
    raw_data = nacl.bindings.randombytes_buf_deterministic(size, seed)

    return encoder.encode(raw_data)
print("Esta es el valor random en formato hexadecimal:")
#Valor de bytes que se van a utilizar y tamaño de los bytes que va utilizar la semilla
salt=randombytes_deterministic(256,bytes(random(32)))
print(bytes(salt).hex())