
print("helloWorld");

# getting information from the user....!

country = "india";
print("i love my " + country);

#datatypes 
print(type("a"));
print(type(2));
print(type(2.5))

# the process of storing a value inside the variable is called 'assignment'.
#implicit conversion - converting one datatype into another (it happens internally here computer sorts the things.)
#explicit conversion - converting one datatype (here manually need to be done)

print(7 + 7.8) #IMPLICIT CONVERSION
print("hello this is " + str(8)) #Explicit Conversion

# Functions :
 # 'def' keyword is used to define a function. and then function name and colon
def greeting(name):
   print ("welcome, " + name)

greeting("bhavish")

def greeting(name, department):
    print("welcome," + name)
    print("so you are in "+ department)

greeting("bhavish", "cce")

#return function returns the value from the function

def area_triangle(base, height):
    return (base*height)/2;
areaof1sttraingle = area_triangle(2,5)
areaof2ndttraingle = area_triangle(7,3)
sum = areaof1sttraingle + areaof2ndttraingle

print("The sum of both areas is: "+ str(sum))

name = "kay"
number = len(name) * 9
print(number)

# area of circle

def area_circle(r):
    pi= 3.14;
    area = (pi*(r**2))
    return area;

area1 = area_circle(6)
print(area1);

### good problem
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller ,bigger = order_numbers(100, 99)
print(smaller, bigger)

### conditionals
print(10>1)

## boolean : true or false.
print("cat"=="cat")

##cannot check between a number and a string because python cannot know whether it is a string or a number
# if(condition):
#    print()/ or what ever operation
# else:
#     print("whatever statement")/what ever statement

