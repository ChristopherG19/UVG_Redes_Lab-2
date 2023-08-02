'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from emisorHam import Emisor
from receptorHam import Receptor

def main():
    
    # get input from file
    req = read_txt_file("responseHamming.txt")

    if req == "": 
        print("Error reading file")
        return
          
    Ems = Emisor(req)
    l = Ems.get_response()
    Rec = Receptor(l[2], l[0], l[1], l[3])
    res = Rec.check()

    print()
    print("Data enviada por el emisor: ", req)
    print("Data enviada al receptor: ", l[2])
    print("\nResultado:", res)
    print()

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("File not found.")
        return ""
    except IOError:
        print("Error reading the file.")
        return ""

if __name__ == '__main__':
    main()