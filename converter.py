

#features
def binToDec(num):
    index = 0
    result = 0
    while num > 0:
        if num % 10 == 1:
            result += 2**index
        else:
            pass
        num = num // 10
        index = index + 1
    return result

def decToBin(num):
    highestSquare = 0
    solution = ""
    while 2 ** highestSquare < num:
        highestSquare += 1
    for i in range(highestSquare, -1, -1):
        if 2 ** i <= num:
            num -= 2**i
            solution += "1"
        else:
            solution += "0"
    solution = int(solution)
    return solution


def hexToDec():
    return 0

def decToHex():
    return 0

def binToHex():
    return 0

def hexToBin():
    return 0

#input verification functions
def inputInt(prompt):
    success = False
    while (not success):
        num = input(prompt)
        try:
            num = int(num)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return num

def verifyDec():
    return 0

def verifyHex():
    return 0

def verifyBin():
    return 0

#mainMenu
def main():
    print("Welcome!")
    while True:
        print("Please select an option below")
        print("1) Convert decimal to binary")
        print("2) Convert binary to decimal")
        print("0) exit")
        choice = inputInt("option: ")

        if choice == 1:
            num = inputInt("please enter a decimal number: ")
            print(decToBin(num))
        elif choice == 2:
            num = inputInt("please enter a binary number: ")
            print(binToDec(num))
        elif choice == 0:
            exit(0)
        else:
            print("[Error] Invalid option")

if __name__ == "__main__":
    main()
