from hexlet.code_basics import parent_for

# BEGIN
def get_parent_names_total_length (child_name):
    father_name = parent_for(child_name, "father")
    mother_name = parent_for(child_name)
    return len(father_name) + len(mother_name)
# END

def sub(a, b):
    result = a - b
    return result
print(sub(10, 7))