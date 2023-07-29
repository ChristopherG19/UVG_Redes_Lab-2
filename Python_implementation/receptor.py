'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from prettytable import PrettyTable

class Receptor():
    def __init__(self, data, pars, original, changes):
        self.data = data
        self.pars = pars
        self.parsO = original
        self.changes = changes
                
    def new_word(self):
        new_w = {}
        l = list(self.data)
        l.reverse()
        for index in range(len(l),0,-1):
            new_w[index] = int(l[index-1])

        return new_w

    def get_values(self):
        newDic = {}
        bits = {}
        toCalc = {}
        for k,v in self.pars.items():
            for k2,v2 in v.items():
                bits[k] = k2
                temp = []
                for key, value in zip(list(v2.keys()), list(v2.values())):
                    temp.append(key)
                    if key not in newDic:
                        newDic[key] = value
                toCalc[k] = temp
                     
        newDic = dict(sorted(newDic.items(), key=lambda item:item[0], reverse=True))   

        return (newDic, bits, toCalc)
    
    def get_bit_paridad(self, ls):
        count = ls.count(1)
        change = 0
        if (count % 2 != 0):
            change = 1        
        
        return change
    
    def binario_a_decimal(self, numero_binario):
        numero_decimal = 0 

        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion

        return numero_decimal
    
    def check(self):
        resultTemp = []
        for k,v in self.get_values()[2].items():
            for el,el2 in self.changes.items():
                if k == el:
                    newL = []
                    for el3 in v:
                        newL.append(self.new_word()[el3])

                    bitP = self.get_bit_paridad(newL)
                    resultTemp.append(bitP)
            
        correct = []        
        for el, v in self.changes.items():
            correct.append(v[1])

        if correct != resultTemp and not all(elemento == 0 for elemento in resultTemp):
            decimal = self.binario_a_decimal("".join([str(x) for x in resultTemp]))
            return f"Hubo un error en el bit {decimal}"
        return "Todo correcto, el mensaje no cuenta con errores"
                
        