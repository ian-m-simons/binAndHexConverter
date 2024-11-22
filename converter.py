

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

def decToBin():
    return 0

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
    print(binToDec(1011101))

if __name__ == "__main__":
    main()
