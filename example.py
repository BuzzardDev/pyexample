# print
print("Hello, World") #well print the text Hello, World to the console/terminal

print(6) # this will print the number 6 to the console/terminal as a integer

print(45.2) # this will print the number 45.2 to the console/terminal as a float

print(True) # this will print True to the console/terminal as a boolean

name = "Damian"
print("Hello, "+ name) # this will print Hello, Damian to the console/terminal. Name will vary on the string you pass into the variable. This is called concatination



# Variables

x = 356 # this is a integer (a whole number)

y = 231.8 # this is a float (non whole numbers)

name = "Bob" # this is a String (text)

goOutToEat = False # this is a boolean (True or False)
# see I capitalized every first letter of a word except for the first one? This is called Camel Case
# Camel Case is used as visualizer to make variables easier to read

animalsList = ["Dog", "Cat", "Elk", "Zebra", "Chicken"] # this is a list is defined using [] and is using for storing mass variables under one name



# Operators

add = 4+3 # returns 7 uses plus sign for addition

sub = 4-3 # returns 1 uses a minus sign for subtraction

multiply = 4*3 # returns 12 uses a astrisks for multiplcation

divide = 4/3 # returns 1.3333333333333333 uses a forward slash for division

powers = 4**3 # returns 64 uses double astriks for the power in Python, previously ^ in SNAP

mod = 4%3 # returns 1 uses percent sign for a modulo, this returns the remainder of a division problem

round = round(4.3) # returns 4 uses the round() function in python to round

greaterThan = 4 > 3 # returns True uses greater than sign

lessThan = 4 < 3 # returns False uses less than sign



# Loops

# this is a while loop this is like the repeat until block in SNAP this will repeat until the variable "jobless" is equal to False 
# (Note: we use double equal signs to check if something is equal to something else and just one equal sign for setting a value)
while jobless == True: 
    print("Go Get a Job!")
# However currently this will run forever because we never CHANGE the variable state

# We saw if statements in SNAP this is doing the same thing as the above while loop, however it is only being ran ONCE and ONLY IF jobless is indeed True
# This prints go get a job
if jobless == True:
    print("Go Get a Job!")
# Note we use colons in python to define the start of a loop

# This is a elif basically you go to the next if statement if the previous is not True
# In this case jobless is False so it will print nice now pay your bills
if jobless == True:
    print("Go Get a Job!")
elif jobless == False:
    print("Nice now pay your bills!")

# This is if else, just like in SNAP if the if condition is not met then it will run the else. In this case we are using Boolean so we are golden here
# In this case jobless is True so it will print get a job
if jobless == True:
    print("Go Get a Job!")
else:
    print("Nice now pay your bills!")

# This is a for loop what this is doing is itterating through a list and printing every value in the list
# the for loop has made a new var to store temporarily store each index value 
# This returns everything in the list on its own line
jobSearch = ["Microsoft", "Safeway", "Apple", "PUD"]
for jobs in jobSearch:
    print(jobs)