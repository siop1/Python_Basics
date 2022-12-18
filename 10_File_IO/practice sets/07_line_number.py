# WAP to find out the line number where python is present from problem 6.
line=1
data=True
python_present=False
with open('06_log.txt','r') as f:
    while data:
        data=f.readline()
        if 'python' in data.lower():
            print(f"python is present in line no. {line}")
            python_present=True
        line=line+1

if python_present==False:
    print("python is not present")