def reverseString(stringVal):

    length = len(stringVal) - 1

 
    def recursive(string, index):
        if index < 0:
            return ""
        

        return stringVal[index] + recursive(string, index - 1)
    

    return recursive(stringVal, length)
    




print(reverseString("Hello"))