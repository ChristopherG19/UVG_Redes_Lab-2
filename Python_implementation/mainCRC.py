from view import *
from emisorCRC import *
from receptorCRC import *

def main():
    
    # Get user info
    userInput = getUserInput()
    print("Input")
    print(userInput)

    
    emisor = Emisor(userInput)
    response = emisor.get_response()

    receptor = Receptor(response)



if __name__ == '__main__':
    main()
