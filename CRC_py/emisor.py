from view import *

class Emisor():

    def __init__(self, userInfo):
        userInfo = userInfo

        self.trama = []

        for char in userInfo:
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


        # generate polinomio
        self.polinomio = [
            True, False, True, True, False, True, False, True, 
            False, False, False, True, False, True, False, True,
            False, False, False, False, True, True, True, False, 
            True, False, False, True, True, False, True, False
        ]

        self.CRC()

    def CRC(self):
        actual = []

        # initialize by coping the first 32 bites
        for i in range(len(self.polinomio)):
            actual.append(self.trama[i])

        EOL = len(self.polinomio)

        while(EOL < len(self.trama)):

            temp = []

            print()
            printTrama(actual)
            printTrama(self.polinomio)

            for i in range(len(self.polinomio)):
                temp.append(actual[i] ^ self.polinomio[i])

            printTrama(temp)

            # pass the zeros
            while(not temp[0] and EOL < len(self.trama)):
                temp.append(self.trama[EOL])
                EOL += 1

                temp.pop()

            # replace actual for temporal
            actual = temp

        print("\nActual")
        printTrama(actual)
        actual.pop()
        printTrama(actual)

        # Add the result to the original trama
        self.result = []
        for b in self.tramaOriginal:
            self.result.append(b)
        for b in actual:
            self.result.append(b)

        print("\nFinal result")
        printTrama(self.result)
        


        

        

        
        

    