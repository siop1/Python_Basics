# WAP using sequence escape characters to format below string:

# message="Hello programmers,Our daily habit is EAT,SLEEP,CODE and REPEAT.Happy learning"
# Output should look like this:
'''
Hello programmers,
    Our daily habit is
'EAT',"SLEEP",CODE and REPEAT
Happy lear\ning!!
'''
# Seems a little tricy huh, Lets solve this using what we had previously learned
message="Hello programmers,\n\tOur daily habit is\n'EAT',\"SLEEP\",CODE and REPEAT.\nHappy lear\\ning "
print(message)