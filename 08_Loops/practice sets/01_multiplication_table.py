# WAP to print multiplication table of a given number using for loop
num=int(input('Number: '))
for i in range(1,11):
    # print(num ,'*', i,'=',num*i)
    print(f"{num} * {i} = {num*i} ")
