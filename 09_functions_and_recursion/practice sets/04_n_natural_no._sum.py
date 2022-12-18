# Write a recursive function to calculate sum of first n natural numbers.
def first_n_natural_no_sum(n):
    if n==1:
        return 1
        
    return n + first_n_natural_no_sum(n-1)


try:
    n=int(input('Number: '))
except:
    print("not a natural number")
    exit()
if n>0:
    pass
else:
    print("not a natural number")
    exit()
sum=first_n_natural_no_sum(n)
print(f"Sum of first {n} natural numbers is {sum} ")
 