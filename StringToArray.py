
# String To Array
import os
import time

def removeBreakInArray(array):
    for element in array:
        if element == '':
            array.remove(element)

def main():
    print("Inserisci la stringa... \n")

    timeout = time.time() + 5
    array = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        array.append(line)

        if time.time() > timeout:
            os.system('cls')
            break

    # Check and remove breaks in array
    removeBreakInArray(array)

    # Print Result    
    print(array)

if __name__ == "__main__":
    main()

