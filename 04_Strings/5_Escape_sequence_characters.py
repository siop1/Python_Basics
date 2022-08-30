# Some of the Escape_sequence_characters and their use. 

# \n newline
# \t tab
# \\ backslash
# \' single quote
#\" double quote, etc.

print("hello man")
print("hello\nman") # prints hello and man separately in new line
print("\thello man") # adds tab before hello
print("Hello ma\n") # if you want to insert \ and used like this
# then it will treated it as \n newline escape character
print("Hello ma\\n") # if needed to insert \ character then use \\

# if you use single quote as outer quote and wanted to use single quote 
# as string or double quote as outer quote and wanted to
# use double quote as string then it will give error
# print('The film is named 'Bahubali'') --> gives error
# Instead you can use \' and it will print ' like this:
print('The film is named \'Bahubali\'') 

# print("The film is named "Bahubali"") --> gives error
# Instead you can use \" and it will print " like this:
print("The film is named \"Bahubali\"") 


# You may ask me Siop you previously told us to use "" inside '' or 
# use '' inside "" then why are you using \' character
# let me give you an example 
# What if you have to use both double quote and single quote inside string

# print("This book is named 'Brain power' and it is "awesome" ")
# In this case although you solved the problem with '' still problem 
# for "" is not solve so in this case you have to use \" or \' as per neccesity

print("This book is named 'Brain power' and it is \"awesome\" ") 
# or you can do this
print('This book is named \'Brain power\' and it is "awesome" ')







