# WAP to detect double spaces in a string entered by user

# the logic for this question is that we have find() function which returns the index of character if such character is present
# if no such character is found then it will return -1 so we can detect using this simple approach

a=input("Enter a word or phrase: ")
b=a.find('  ')
print(b) # prints index of character


# Well we can make this program more interesting after learning if else so I am commenting it for now
# You can check this out
# if(b>=0):
#     print("Double spaces detect at index",b)
# else:
#     print("No double spaces detected")