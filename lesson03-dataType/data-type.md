# Learning objectives
Python Data Types are used to define the type of a variable. And in this lesson, we’ll list out all the data types and 
discussion the functionality of each

# Data Types
There are different types of data types in Python. Some built-in Python data types are:

| **Data Types** | **Classes**         | **Description**                    |
|----------------|---------------------|------------------------------------|
| Numeric        | int, float, complex | holds numeric values               |
| String         | str                 | holds sequence of characters       |
| Sequence       | list, tuple         | holds collection of items          |
| Mapping        | dict                | holds data in key-value pair form  |
| Boolean        | bool                | holds either True or False         |
| Set            | set, frozenset      | hold collection of unique items    |

In Python, we need not declare a datatype while declaring a variable. We can simply just assign values in 
a variable. But if we want to see what type of numerical value is it holding right now, we can use type(), like this:
```python
var1 = 23
var2 = "text"

type(var1)# output: int
type(var2)# output: str
```

# Python Numeric Data Type
Python numeric data type is used to hold numeric values like;
* **int** - holds signed integers of non-limited length.
```python
a = 20
b = int(20)
```
* **float** - holds floating precision numbers, and it’s accurate up to 15 decimal places.
```python
a = 20.2
b = float(20.2)
```
* **complex** - holds complex numbers.
```python
a = 20j
b = complex(20j)
```

# Python String Data Type
The string is a sequence of characters. Python supports Unicode characters. Generally, strings are represented by either
single or double-quotes and they are immutable.
```python
a = "string in a double quote"
b = 'string in a single quote'
print(a)
print(b)
```

# Python sequence Data Type
A sequence is a data structure that contains items arranged in order, and you can access each item using an integer 
index that represents its position in the sequence. You can always find the length of a sequence.
* List: list is an ordered sequence of some data written using square brackets([]) and commas(,) that can hold any type.
```python
# create a List
languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0])   # Swift

# access element at index 2
print(languages[2])   # Python
```
* Tuple: The tuple is another data type which is a sequence of data similar to a list. But it is immutable. That means 
data in a tuple is write-protected. Data in a tuple is written using parenthesis and commas.
```python
# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])   # Microsoft

# access element at index 1
print(product[1])   # Xbox
```

# Python Dictionary Data Type
Python dictionary is an ordered collection of items. It stores elements in key/value pairs. Here, keys are unique 
identifiers that are associated with each value.
```python
# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city) # prints {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city['Nepal'])  # prints Kathmandu

print(capital_city['Kathmandu'])  # throws error message 
```

# Python Set Data Type
Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }.
```python
# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id) # {112, 114, 115, 116, 118}

# display type of student_id
print(type(student_id)) # <class 'set'>
```

# Exercise
Create a program that will create different type and print type and value