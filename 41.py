#Список операций сравнения:
#
#  < — меньше
#  <= — меньше или равно
# "> — больше
# ">= — больше или равно
#  == — равно
# "!= — не равно

def is_infant(age):
  return age < 1

print(is_infant(2))

def is_pensioner(age):
    return age >= 60
print(is_pensioner(65))