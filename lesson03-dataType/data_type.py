# Int
a = 20
b = int(20)
print(type(a))
print(a)
print(type(b))
print(b)

# Float
a_f = 20.2
b_f = float(20.2)
print(type(a_f))
print(a_f)
print(type(b_f))
print(b_f)

# Complex
a_c = 20j
b_c = complex(20j)
print(type(a_c))
print(a_c)
print(type(a_c))
print(b_c)

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# List
languages = ["Swift", "Java", "Python"]
print(type(languages))
# access element at index 0
print(languages[0])   # Swift
# access element at index 2
print(languages[2])   # Python

# Tuple
product = ('Microsoft', 'Xbox', 499.99)
print(type(product))
# access element at index 0
print(product[0])   # Microsoft
# access element at index 1
print(product[1])   # Xbox

# Dic
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(type(capital_city))
print(capital_city) # prints {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])  # prints Kathmandu

# set
student_id = {112, 114, 116, 118, 115}
print(type(student_id))
# display student_id elements
print(student_id) # {112, 114, 115, 116, 118}
# display type of student_id
print(type(student_id)) # <class 'set'>
