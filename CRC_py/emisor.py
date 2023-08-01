from view import *

class Emisor():

    def __init__(self, input):
        input = input

        self.trama = []

        for char in input:
            if char == '1':
                self.trama.append(True)

            elif char == '0':
                self.trama.append(False)

        # Save a copy of the original before padding
        self.tramaOriginal = []
        for t in self.trama:
            self.tramaOriginal.append(t)

        # padding
        for i in range(31):
            self.trama.append(False)

        print("\ncon padding")
        printTrama(self.trama)
        

        

        
        

    