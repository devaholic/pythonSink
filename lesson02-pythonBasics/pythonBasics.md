# Learning objectives
* Statement
* Variables
* String basics
* Number basics
* Error messages
* Comments

# Statement
Any instruction written in the source code and executed by the Python interpreter is called a statement.
The Python language has many different types of statements like assignment statements, conditional statements,
looping statements, etc., that help a programmer get the desired output.

```python
tep = float(input('What is the water temperature? '))
if tep > 24:
	print('Water is safe!')
	print('Jump in!')
else:
	print('Better not go in!')
# First line after if-else 
```

# Variables
Variables allow programs to refer to values using names rather than memory locations. 
Ex: age refers to a person's age, and birth refers to a person's date of birth.
```python
city = "Chicago"
age = 2
result = 4 + 4
```
## NoneType
The NoneType object is a special type in Python that represents the absence of a value. In other words, NoneType is the 
type for the None object, which is an object that contains no value or defines a null value. It is used to indicate 
that a variable or expression does not have a value or has an undefined value. “None” basically means the absence 
of a value.
```python
value = None

print(value) # Output: None
```

## Naming Convention
A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. 
Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total. 
Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in 
between each word, such as first_name or total_price.
<br>
Python has reserved words, known as keywords, which have special functions and cannot be used as names for variables 
(or other objects).

| False  | await    | else    | import   | pass   |
|--------|----------|---------|----------|--------|
| None   | break    | except  | in       | raise  |
| True   | class    | finally | is       | return |
| and    | continue | for     | lambda   | try    |
| as     | def      | from    | nonlocal | while  |
| assert | del      | global  | not      | with   |
| asynch | elif     | if      | or       | yield  |

## Types
One of the best features of Python is its flexibility when it comes to handling various data types.
<br>
Python variables can hold various data types, including integers, floats, strings, booleans, tuples and lists.
<br>
Python is what is known as a dynamically-typed language. This means that the type of a variable can change during the 
execution of a program. Another feature of dynamic typing is that it is not necessary to manually declare the type of 
each variable, unlike other programming languages such as Java. You can use the type() function to determine the type of a variable. For instance:
```python
var1=23
var2="text"

type(var1)# output: int
type(var2)# output: string

var1="change to string"
type(var1)# output: str
```

# String basics
A string is a sequence of characters enclosed by matching single (') or double (") quotes. 
* Ex: "Happy birthday!"
* Ex: '21' are both strings.

To include a single quote (') in a string, enclose the string with matching double quotes ("). 
* Ex: "Won't this work?" To include a double quote ("), enclose the string with matching single quotes ('). 
* Ex: 'They said "Try it!", so I did'.

# Number basics
Python supports two basic number formats, integer and floating-point. An integer represents a whole number, 
and a floating-point format represents a decimal number.

# Comments
The # character should be followed by a single space. Ex: # End of menu is easier to read than #End of menu.

# Exercise
write a program that prints below:
```text
***************
*             *
*   WELCOME   *
*             *
***************
```