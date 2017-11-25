

def getStringLength(strIn):
    lenght = 0
    lenght = len(strIn)
    return lenght

def isNumber(strIn):
    isNum = True
    try:
        int(strIn)
    except:
        isNum = False
    return isNum

def determineLenght(strIn):
    length = 0
    if (isNumber(strIn)):
        print("This function is NOT applicable to numbers")
    else:
        length = getStringLength(strIn)
        print("Length of the String: '" + strIn + "' is:\n" + str(length))
    return length

########################RUNNING FUNCTIONS###########################
myString = input("Please enter a String: \n")
determineLenght(myString)
