# Learning objectives
A loop is a code block that runs a set of statements while a given condition is true. A loop is often used for 
performing a repeating task. On this lesson, we will go through:
* While loop
* For loop
* Nested loops
* Break and continue
* Loop else

# While loop
A while loop is a code construct that runs a set of statements, known as the loop body, while a given condition, 
known as the loop expression, is true. At each iteration, once the loop statement is executed, 
the loop expression is evaluated again.

* If true, the loop body will execute at least one more time (also called looping or iterating one more time).
* If false, the loop's execution will terminate and the next statement after the loop body will execute.

```python
value = 1

while value < 10:
    value+=1

value=1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))
```

# For loop
In Python, a container can be a range of numbers, a string of characters, or a list of values. To access objects 
within a container, an iterative loop can be designed to retrieve objects one at a time. A for loop iterates over 
all elements in a container.

```python
names = ["Dave", "Sara", "John"]

for x in names:
     print(x)
```

# Nested loops
A nested loop has one or more loops within the body of another loop. The two loops are referred to as outer loop and 
inner loop. The outer loop controls the number of the inner loop's full execution. More than one inner loop can 
exist in a nested loop.

```python
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
```

# Break and continue
## Break
A break statement is used within a for or a while loop to allow the program execution to exit the loop once a given 
condition is triggered.
```python
value=1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1
```

## Continue
A continue statement allows for skipping the execution of the remainder of the loop without exiting the loop entirely. 
A continue statement can be used in a for or a while loop. After the continue statement's execution, 
the loop expression will be evaluated again and the loop will continue from the loop's expression.

```python
value=1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
```

# Loop else
A loop else statement runs after the loop's execution is completed without being interrupted by a break statement. 
A loop else is used to identify if the loop is terminated normally or the execution is interrupted by a break statement.
```python
value=1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")
```