
def solution(phoneBook):
    #Hash Table
    hash = {}
    for number in phoneBook:
        hash[number] = 1
    #Loop Each Number
    for number in phoneBook:
        prefix = ""
        #loop each substring and check if its in hash
        for num in number:
            prefix += num
            if prefix in hash and prefix != number:
                return False
    return True