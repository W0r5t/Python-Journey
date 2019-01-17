
#Now We're going to create a list called "pythonlist" and set 4 items in the list
pythonlist = []
pythonlist.append(69) #Sets first item value in the list as 69
pythonlist.append(420) #Sets first item value in the list as 420
pythonlist.append(911) #Sets first item value in the list as 911
pythonlist.append(1337) #Sets first item value in the list as 1337, Cos we're all L33T
#Python always reads the beginning item, First item as number 0
print(pythonlist[0]) #Prints First item in the list
print(pythonlist[1]) #Prints Second item in the list
print(pythonlist[2]) #Prints Third item in the list
print(pythonlist[3]) #Prints Fourth item in the list

#Now We're going to use a For statement to Display the whole contents of the list
for all in pythonlist: #Sets For statement and the corresponding condition for the list
    print(all) #Prints all items in list

#Now We're going to create a list that stores Multiple Data Types
Integers = [] #Creates the list Integers
Strings = [] #Creates the list Strings
MainAlias = ["Fortue"] #Creates the list MainAlias with the String Fortue Stored
Users = [] #Creates the list Users

Integers.append(69) #Sets the first value in the Integers List to the number 69
Integers.append(123) #Sets the second value in the Integers List to the number 123
Integers.append(420) #Sets the third value in the Integers List to the number 420
Integers.append(1337) #Sets the fourth value in the Integers List to the number 1337

Strings.append("Python") #Sets the first value in the Strings List as Python
Strings.append("Is") #Sets the second value in the Strings List as Is
Strings.append("Kinda") #Sets the third value in the Strings List as Kinda
Strings.append("Gay") #Sets the fourth value in the Strings List as Gay

Users.append("W0r5t") #Sets the first Value in the Users List as W0r5t
Users.append("Trvpped") #Sets the first Value in the Users List as W0r5t

print("The Alias the Coder is %s" % MainAlias) #Prints all the values from the MainAlias list -> "Fortue"
print("The Coders Other Aliases are %s" % Users) #Prints all the values from the Users list -> "W0r5t, Trvpped"
print("Don't forget about all our Important Numbers and Strings! %s" % Integers, Strings) #Prints all values from both Lists, Integers and Strings
