
#> Приоритет арифметических операций выше логических

def is_even(num):
  return num % 2 == 0

print(is_even(16))
print(is_even(17))

def is_first_letter_an_a(string):
    first_letter = string[0]
    return first_letter == 'a'

print(is_first_letter_an_a('orange'))  # => False
print(is_first_letter_an_a('apple'))   # => True



#> string[i:j] 
#>  * i - индекс начала символа, с которого начинаем выризать 
#>  * j - индекс символа, перед которым заканчиваем выризание
#>  * j - i = длина полученого отрезка

print("Winterfel"[0:6]) # Winter
print("Stark"[0:6]) # Stark

#> string[:n] 
#> В данном случае по умолчанию начинаем вырезать с 0, и до n, не включая его.
print('Winterfell'[:6])  # => 'Winter'
print('Stark'[:6])       # => 'Stark'

#> можно использовать переменные 
n = 6
print('Winterfell'[:n])  # => 'Winter'
print('Stark'[:n])       # => 'Stark'


# берём отрезок, начиная с символа с индексом 2,
# и заканчивая символом с индексом 4
# (т.е. "перед символом с индексом 5")
print('Absolute'[2:5])  # => 'sol'

# начиная с символа с индексом 3
# и не доходя до символа с индексом 3,
# берём пустой отрезок (3 - 3 == 0)
print('Absolute'[3:3])  # => ''



def has_targaryen_reference(string):
    targaryen = "Targaryen"
    length = len(targaryen)
    substring = string[:length]
    return targaryen == substring


