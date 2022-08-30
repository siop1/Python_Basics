# WAP to add two numbers

a=input("Enter first number: ")
b=input("Enter second number: ")
# the input function always output a string even a number is entered so to convert into integer
# we use typecasting for ex: int(a)

result=int(a)+int(b)
print("Sum of " + a +" and "+ b+ " is " + str(result)) # i have used + sign so only str + str concatenation
# is possible so i have converted result which was int into string

# we can also use comma operator and we donot need to typecast into string like this:
print("Sum of " + a +" and "+ b+ " is " , result)

# or we can also use
print("Sum of",a,"and",b,"is",result)