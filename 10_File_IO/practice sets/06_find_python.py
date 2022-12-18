# WAP to mine a log file and find out whether it contains python.

with open('06_log.txt','r') as f:
    data=f.read()

if 'python' in data.lower():
    print("python is present")
else:
    print("python is not present")