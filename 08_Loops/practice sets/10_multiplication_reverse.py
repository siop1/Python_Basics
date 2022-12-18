# WAP to print multiplication table of a given number using for loop in reverse order
num=int(input('Number: '))
for i in range(1,11):
    # print(num ,'*', 11-i,'=',num*(11-i))
    print(f"{num} * {11-i} = {num*(11-i)} ")
