import random
from werkzeug.security import generate_password_hash

LetrasMinus = "abcdefghijklmnopqrstuvwxyz"
LetrasMayu = LetrasMinus.upper()
Number = "0123456789"
Simbolos = "@()[]{}*,;/-_?'+<#>!$%&=|."

Base = LetrasMinus + LetrasMayu + Number + Simbolos
Longitud = 12

for i in range(10):
    muestra = random.sample(Base, Longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))

'''
Random password generator and 
enrolls it with a function called "generate_password_hash"
'''
