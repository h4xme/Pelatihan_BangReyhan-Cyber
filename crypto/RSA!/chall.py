from Crypto.Util.number import *
from secret import flag

x = getPrime(128)

def primeDet(bit):
    las_pas = 2**2048 + getPrime(bit) + x
    las_pas |= 1
    while True:
        if(isPrime(las_pas)): return las_pas
        las_pas+=2

def generate():
    p = primeDet(512)
    q = primeDet(512)
    return p, q

if __name__ == '__main__':
    p,q = generate()
    e = 0x10001
    c = pow(bytes_to_long(flag), e, p*q)
    with open("output.txt","w") as f:
        f.write(f'{p*q=}\n')
        f.write(f'{e=}\n')
        f.write(f'{c=}\n')