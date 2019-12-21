def get_age_difference(first_year, second_year):
    return "The age difference is {}".format(abs(first_year - second_year))

age1 = 5
def generate1():
    return age1 + 3
result1 = generate1() # 8


age2 = 10;
def generate2():
    age2 = 10
    return age2 + 3
result2 = generate()#13


age3 = 5
def generate3():
    age3 = 8

generate3()
result = age3 # 5