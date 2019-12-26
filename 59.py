def is_arguments_for_substr_correct(string, index, length):
    if length < 0: 
        return False
    if index < 0:
        return False
    if index > len(string) - 1:
        return False
    if index + length > len(string):
        return False
    return True