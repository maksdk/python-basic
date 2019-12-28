def get_even_numbers_up_to(number):
    counter = 1
    result = ''

    while counter <= number:
        if counter % 2 == 0:
            result = result + str(counter)

        counter += 1

    return result

    print(get_even_numbers_up_to(5))
    print(get_even_numbers_up_to(9))

    def get_even_numbers_up_to(number):
    counter = 1
    result = ""

    while counter <= number:
        if counter % 2 == 0:
            result = result + str(counter) + ","
        
        counter += 1

    return result

    def get_even_numbers_up_to(number):
    counter = 1
    result = ""
    separator = ","

    while counter <= number:
        if counter % 2 == 0:
            result = result + str(counter) + separator

        counter += 1

    return result[:len(result) - 1] + "."

print(get_even_numbers_up_to(9))