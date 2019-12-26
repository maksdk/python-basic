def reverse_string(string):
    index = len(string) - 1
    reversed_string = ""

    while index >= 0:
        curr_chart = string[index]
        reversed_string = reversed_string + curr_chart
        index -= 1
        
    return reversed_string

print(reverse_string('Game Of Thrones'))
# => senorhT fO emaG

# BEGIN
def my_substr(string, length):
    i = 0
    substring = ''

    while i < length:
        curr_chart = string[i]
        substring = substring + curr_chart
        i += 1

    return substring 
# END