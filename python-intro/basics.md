Basic Python Cheat Scheet
===============
![A short Python Introduction](pictures/python-into.png)

Every objects name can reference one of any other things at any time, a single object can be different things at different points. One object name can reference may different thing through out the objects life. It still remains the same object. 

Strongly typed language.
In certain case you can convert between types, a string an float or a string and an int if and only if you have proper formating for the object from the begging. you can even convert true to a bool. but not always.

##Variables
variables store pieces of data and give it an specific name
return type is bool.
```python
carolina = 10
```
###Booleans
Booleans are a data type and they can only be true or false, for example:

```python
a = True
b = False
```
###To reassign variables
Like in other languages you just have to set it equal to different value. In Python = (:=, assignation) and == ( = equality)
###Whitespace
In Python white space has a meaning because there are no ends in functions like in Ruby.
###Single Line comments
Same as in Ruby #
###Multiline Comments
Triple quotation marks:
```python
"""
A multi-line comment
"""
```
###Math
```python
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
exponentiation = 2 ** 3
modulo = 3 % 2
```
###Format in print
The code below formats a numeric variable
```python
variable = 1.456
print("%.2f", variable)
```
##Strings and Console Output
###String methods
A string is just a collection of characters
String methods allow you to perform specific tasks for your strings:
*len() : to check the length
```python
random_string = "Check the length of this string"
print len(random_string)
```
*lower() : to get rid of capitalization
```python
string = "LaLaLaLaLala"
print string.lower
```
*upper()
```python
string = "LaLaLaLaLala"
print string.upper()
```
*str(): Turns none string in to strings
```python
age = 28
str(age)
```
###Dot notation
The methods that work exclusively for string use dot notation, len works for other types so you pass on the string and you don't call the method on the string. That is the difference.

###Printing Variables
You can concatenate string to print them, but it's better to use the operator after the string with variables. The operator % will replace the %s in the string with the string variable that comes after it.

```python
string_1 = "Me llamo"
string_2 = "Carolina"
print "Hola! %s %s." % (string_1, string_2)
```
###Formating a Variable

"format string" helps show variables in a more human friendly way. 

Formatters: %s, %r , %d
###Lists



