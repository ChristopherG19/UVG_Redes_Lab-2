from view import *
from emisor import *
from receptor import *

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
