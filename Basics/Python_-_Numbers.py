
#I will only be covering basic number data types in this code - IK there's more
#We're going to be starting off the Number types by using Integers -> Whole Numbers
integer = 69
#Now We're going to print the Integer to make sure that it's correctly Declared
print(integer)

#Now We're going to use Float point numbers -> Decimal Numbers
floatpoint = 6.9
#Now Lets Print The Float Point
print(floatpoint)

#Now We're going to use Float Point + Integer and Add them together
floatint = 69 + 6.9
#This will create an equation for python to solve, Lets print and see
print(floatint) #The answer should respond with 75.9 which now sets the data type to a floatpoint
#The Reason the data type changes is due to the decimal extension when the equation is solved

#Now instead of using numbers, We're going to use text in our value
numbstr = "Sixty Nine"
#This now sets the data type to string, Lets print and see
print(numbstr)

#Now We're going to add all of our variables together besides the string
#Python will return an error as the numerical values cannot summarise with strings
total = integer + floatpoint + floatint
#Now We're going to print the total value of the Numerical values
print(total)

#Now We're going to create a subtraction Sequence using the Integer and Floatpoint
subtr = integer - floatpoint
#This should now minus 6.9 from 69
print(subtr)

#Now Lets Create A Division using the Above Variables
divis = integer / floatpoint
#We use the / to divide in python as it doesn't understand other 
print(divis)

#Now We're going to create a multiplication equation with the Same variables
multip = integer * floatpoint
#We use the * as the multiplication symbol
print(multip)

#Lets continue our journey, We have finished covering Basic number Data types