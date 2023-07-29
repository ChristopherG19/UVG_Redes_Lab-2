'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from emisor import Emisor
from receptor import Receptor

def main():
    # req = '110011000'     
    req = input("Ingrese cadena: ")           
    Ems = Emisor(req)
    l = Ems.get_response()
    # newL = list(l[2])
    # newL[2] = '1'
    # bad_req = "".join(newL)
    Rec = Receptor(l[2], l[0], l[1], l[3])
    res = Rec.check()
    print()
    print("Data enviada por el emisor: ", req)
    print("Data recibida recibida: ", l[2])
    # print("Data modificada: ", bad_req)
    print("\nResultado:", res)
    print()


if __name__ == '__main__':
    main()