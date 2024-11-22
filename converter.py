

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
    #create menu
    num = inputInt("enter a number ")
    print(decToBin(num))

if __name__ == "__main__":
    main()
