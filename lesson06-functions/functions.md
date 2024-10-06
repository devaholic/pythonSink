# Learning objectives
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. 
A function can return data as a result.  On this lesson, we will go through:
* Definition
* Variable scope 
* Parameters and Arguments 
* Return values
* Recursion

# Definition
A function is defined using the def keyword. The first line contains def followed by the function name (in snake case), 
parentheses (with any parameters—discussed later), and a colon. The indented body begins with a documentation string 
describing the function's task and contains the function statements. A function must be defined before the function is 
called.
```python
def print_hello_world():
    print("hello world!")

print_hello_world()
```

# Variable scope
A variable's scope is the part of a program where the variable can be accessed and the life of the variable is bound to 
that scope. There is 2 main scopes: global and local
## Global
A variable created in the main body of the Python code is a global variable and belongs to the global scope, therefore 
the life cycle of the variable is the application span. Global variables are available from within any scope, 
global and local.
```python
global_variable=10

def print_something():
    print(global_variable)

print_something()
print(global_variable)
```
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword. 
The global keyword makes the variable global.
```python
def print_something():
    global global_variable
    global_variable=10
    print(global_variable)

print_something()
print(global_variable)
```
Also, use the global keyword if you want to make a change to a global variable inside a function.
```python
global_variable=10

def print_something():
    global global_variable
    print(global_variable)
    global_variable=10

print_something()
print(global_variable)
```

## Local
A variable created within a function has local scope and only exists within the function. A local variable cannot be 
accessed outside of the function in which the variable was created. After a function finishes executing, the function's 
local variables no longer exist.
```python
def print_something():
    local_variable=10
    print(local_variable)

print_something()
# print(global_variable) this cause issue 
```
As explained in the example above, the variable local_variable is not available outside the function, but it is available for any 
function inside the function:
```python
def print_something():
    local_variable=10
    def print_inner_func():
        print(local_variable)

print_something()
# print(global_variable) this cause issue 
```

# Parameters and Arguments
A function argument is a value passed as input during a function call. Good practice is to pass values directly to a 
function rather than relying on global variables.
```python
def print_welcome(name):
      print(f"Welcome {name}!")
username = "dev"
print_welcome(username)

def print_div(op_1, op_2):
    print(f"{op_1}/{op_2} = {op_1/op_2}")

num_1 = 6
num_2 = 3
print_div(num_1, num_2) # Prints "6/3 = 2.0"
```

## Default parameter values
Functions can define default parameter values to use if a positional or keyword argument is not provided for the 
parameter. Default parameter values are only defined once to be used by the function, so mutable objects (such as lists) 
should not be used as default values.
```python
def print_div(op_1, op_2=1):
    print(f"{op_1}/{op_2} = {op_1/op_2}")

num_1 = 6
print_div(num_1) # Prints "6/1 = 6"
```

## Variable number of Arguments (*args )
***args** (arguments) allows you to pass a variable number of positional arguments to a function.
```python
#args is type tuple
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))
print(my_sum([1, 2, 3]))
```

## Keyword arguments
So far, functions have been called using positional arguments, which are arguments that are assigned to parameters in
order. Python also allows keyword arguments, which are arguments that use parameter names to assign values rather than
order. When mixing positional and keyword arguments, positional arguments must come first in the correct order, before
any keyword arguments.
```python
def greeting(msg, name, count):
  i = 0
  for i in range(0, count):
    print(msg, name)

greeting(count=1, name="Ash", msg="Hiya")

greeting("Hiya", count=1, name="Ash")
```
****kwargs** (keyword arguments) allows you to pass a variable number of keyword arguments (key-value pairs) to a function.
```python
#kwargs is type dictionary
def example_function(**kwargs):
    print(kwargs)
example_function(name='Alice', age=30) # output: {'name': 'Alice', 'age': 30}
```

## Modifying arguments and mutability
In Python, a variable is a name that refers to an object stored in memory, aka an object reference, so Python uses a 
pass-by-object-reference system. If an argument is changed in a function, the changes are kept or lost depending on 
the object's mutability. A mutable object can be modified after creation. A function's changes to the object then 
appear outside the function. An immutable(int, float, bool, string, Unicode, and tuple) object cannot be modified 
after creation. So a function must make a local copy to modify, and the local copy's changes don't appear outside the 
function.

# Return values
When a function finishes, the function returns and provides a result to the calling code. A return statement finishes 
the function execution and can specify a value to return to the function's caller. Functions introduced so far have 
not had a return statement, which is the same as returning None, representing no value.
```python
def print_div(op_1, op_2):
    return op_1/op_2

num_1 = 6
num_2 = 3
result = print_div(num_1, num_2)
print(result)
```

# Recursion
Recursion enables a piece of code, a function, to call the same piece of code, the same function, with different parameters.
```python
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 3
print("The factorial of", num, "is", factorial(num))
```