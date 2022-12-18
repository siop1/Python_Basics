# WAP to print following star pattern.
'''
  *
 ***        
*****       for n=3
'''
# first approach
# n=3
# s=-1
# for i in range(0,n):
#     n=n-1
#     s=s+2
#     print(" "* (n),"*"* (s))

# second approach
n=3
for i in range(0,n):
    print(" "*(n-i-1),'*'*(2*i+1))
    
    