# Learning objectives
Operators are used to perform operations on variables and values. On this lesson, we will go through:
* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators

# Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator |                                  Description                                   | Syntax |
|:--------:|:------------------------------------------------------------------------------:|:------:|
|    +     |                          Addition: adds two operands                           |  x + y |
|    –     |                      Subtraction: subtracts two operands                       |  x – y |
|    *     |                    Multiplication: multiplies two operands                     |  x * y |
|    /     |           Division (float): divides the first operand by the second            |  x / y |
|    //    |           Division (floor): divides the first operand by the second            | x // y |
|    %     | Modulus: returns the remainder when the first operand is divided by the second |  x % y |
|    **    |                  Power: Returns first raised to power second                   | x ** y |

# Assignment Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

|                Operators                | Sign |                                            Description                                            |  Syntax   |
|:---------------------------------------:|:----:|:-------------------------------------------------------------------------------------------------:|:---------:|
|           Assignment Operator           |  =   |           Assign the value of the right side of the expression to the left side operand           | c = a + b |
|      Addition Assignment Operator       |  +=  |     Add right side operand with left side operand and then assign the result to left operand      |  a += b   |
|     Subtraction Assignment Operator     |  -=  |   Subtract right side operand from left side operand and then assign the result to left operand   |  a -= b   |
|   Multiplication Assignment Operator    |  *=  |      Multiply right operand with left operand and then assign the result to the left operand      |  a *= b   |
|      Division Assignment Operator       |  /=  |       Divide left operand with right operand and then assign the result to the left operand       |  a /= b   |
|       Modulus Assignment Operator       |  %=  | Divides the left operand with the right operand and then assign the remainder to the left operand |  a %= b   |
|   Floor Division Assignment Operator    | //=  |      Divide left operand with right operand and then assign the value(floor) to left operand      |  a //= b  |
|   Exponentiation Assignment Operator    | **=  |  Calculate exponent(raise power) value using operands and then assign the result to left operand  |  a **= b  |
|     Bitwise AND Assignment Operator     |  &=  |              Performs Bitwise AND on operands and assign the result to left operand               |  a &= b   |
|     Bitwise OR Assignment Operator      | \|=  |               Performs Bitwise OR on operands and assign the value to left operand                |  a \|= b  |
|     Bitwise XOR Assignment Operator     |  ^=  |               Performs Bitwise XOR on operands and assign the value to left operand               |  a ^= b   |
| Bitwise Right Shift Assignment Operator | >>=  |          Performs Bitwise right shift on operands and assign the result to left operand           |  a >>= b  |
| Bitwise Left Shift Assignment Operator  | <<=  |           Performs Bitwise left shift on operands and assign the result to left operand           |  a <<= b  |
|             Walrus Operator             |  :=  |                         Assign a value to a variable within an expression                         | a := exp  |

# Comparison Operators
Comparison operators are used to compare two values:

|    Sign     |                                     Description                                      |  Syntax   |
|:-----------:|:------------------------------------------------------------------------------------:|:---------:|
| Description |                                        Syntax                                        | c = a + b |
|     ==      |                      Equal to: True if both operands are equal                       |  a == b   |
|     !=      |                     Not equal to: True if operands are not equal                     |  a != b   |
|      >      |           Greater than: True if the left operand is greater than the right           |   a > b   |
|      <      |              Less than: True if the left operand is less than the right              |   a < b   |
|     >=      | Greater than or equal to: True if left operand is greater than or equal to the right |  a >= b   |
|     <=      |    Less than or equal to: True if left operand is less than or equal to the right    |  a <= b   |
|             |                      It Consist of mixture of above Operators.                       |           |
|     &=      |        Performs Bitwise AND on operands and assign the result to left operand        |  a &= b   |
|     \|=     |         Performs Bitwise OR on operands and assign the value to left operand         |  a \|= b  |
|     ^=      |        Performs Bitwise XOR on operands and assign the value to left operand         |  a ^= b   |
|     >>=     |    Performs Bitwise right shift on operands and assign the result to left operand    |  a >>= b  |
|     <<=     |    Performs Bitwise left shift on operands and assign the result to left operand     |  a <<= b  |
|     :=      |                  Assign a value to a variable within an expression                   | a := exp  |

# Logical Operators
Logical operators are used to combine conditional statements:

| Operator |                  Description                   | Syntax  |      Example       |
|:--------:|:----------------------------------------------:|:-------:|:------------------:|
|   and    |   Returns True if both the operands are true   | x and y |    x>7 and x>10    |
|    or    | Returns True if either of the operands is true | x or y  |    x<7 or x>15     |
|   not    |      Returns True if the operand is false      |  not x  | not(x>7 and x> 10) |

# Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
with the same memory location:

| Operator | Description                                            | Example    |
|----------|--------------------------------------------------------|------------|
| is       | Returns True if both variables are the same object     | x is y     |
| is not   | Returns True if both variables are not the same object | x is not y |

# Membership Operators
Membership operators are used to test if a sequence is presented in an object:

| Operator | Description                                                                      | Example    |
|----------|----------------------------------------------------------------------------------|------------|
| in       | Returns True if a sequence with the specified value is present in the object     | x in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

# Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

| Operator | Name                 | Description                                                                                             | Example |
|----------|----------------------|---------------------------------------------------------------------------------------------------------|---------|
| &        | AND                  | Sets each bit to 1 if both bits are 1                                                                   | x & y   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                                                              | x \| y  |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                         | x ^ y   |
| ~        | NOT                  | Inverts all the bits                                                                                    | ~x      |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        | x << 2  |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2  |