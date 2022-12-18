'''
A spam comment is defined as text containing following keywords:
"make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams.

'''

comment=input("Enter your comment: \n")
blacklist=["make a lot of money","buy now","subscribe this","click this"]

# approach for programmer unknown of loop

# if "make a lot of money" in comment.lower() or "buy now" in comment.lower() or "subscribe this" in comment.lower() or "click this" in comment.lower():
#     print("This may be spam comment")
# else:
#     print("No spam comment detected")

# approach to solve this who knows loop
blacklist=["make a lot of money","buy now","subscribe this","click this"]
for i in blacklist:
    if i in comment:
        print("This may be spam comment")
        break
else:
    print("not spam")