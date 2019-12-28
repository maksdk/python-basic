def shouter(string):
    length = len(string)
    if length > 5:
        counter = 0
        while counter != 100:
            print(string, end='')  # про "end" см. ниже
            counter += 1

shouter('HELLO!')

def shouter(string):
    length = len(string)
    result = ''
    if length > 5:
        counter = 0
        while counter != 100:
            result += string
            counter += 1
    return result

    

def shouter(string):
    length = len(string)
    count = 0
    index = 0
    result = ''

    if length > 0 and length < 5:
        return string

    if length == 5:
        count = 10
    else:
        count = 100

    while index != count:
        result += string
        index += 1

    return result 