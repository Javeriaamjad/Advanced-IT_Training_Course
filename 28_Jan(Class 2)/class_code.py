#indentation
if True:
  print("This is my second class of Python language")

#comments
# if True: clt + /
# print("This is my second class of Python language")



#variables and constants
name = 'Umair' #both single and double quotes is fine
age = 26
PI = 3.14159 #contsant
print("My name is", name)
print("My age is", age)
print(PI)

#input and output fnctions
name = input("Enter your name: ")  #input function
print("My name is", name)  #output function
print(type(name))


#Primitive Data type
x = 10 #integer
y = 10.01
z = 4 + 3j
print("Real number is,", z.real)
print("Imaginary number", z.imag)


#string
sentence = "This is my second class of Python language"
print("Firs letter:", sentence[0])
print("Here is", sentence[-15])
greeting = "Python " + "language"
print(greeting)
repeat = "Python" * 3
print(repeat)
print("Sliced string:", sentence[0:4])
print("Sliced string:", sentence[0:23])
print("Lower case", sentence.lower())
print("Upper case", sentence.upper())
print("replace", sentence.replace("Python", "C++"))



#Collect data Types

#List
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
#List slicing
numbers[:3]  #0,1,2 indices


#tuples
numbers = (1,2,3,4,5)
print(numbers)


#Sets
numbers = {1,2,3,4,5}
numbers.add(5)
print(numbers)


#Dictionary
student = {"name": "Umair"}  #key value pair
student['name'] = "Talha"
print(student)
student['age'] = 26
print(student)

#Implicit conversion
num1 = 10
num2 = 10.01
result  = num1 + num2
print(result)
print(type(result))

#Explicit conversion
age = "26"
integer = 10
age = int(age)
# integer = str(integer)
# float(age)
print(type(age))
result = age + integer
print(result)



#Comparison Operation

num1 = 10
num2 = 4

print("Equal", num1 == num2)
print("Not Equal", num1 != num2)
print("Greater than", num1 > num2)
print("Less than", num1 < num2)
print("Floor Division", num1 // num2)
print("Modulus", num1 % num2)
print("Exponent", num1 ** num2)


#Assignment Operators
a=10
a+=5 
a-=5 
a*=5
a/=5 
print(a)

#random function
import random
print(random.randint(1,10))
print(random.random())
print(random.randint(1,10))
items = ['Apple', "Bananas"]
print(random.choice(items))
