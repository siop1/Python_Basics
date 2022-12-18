'''
WAP to generate multiplication table from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old boy.
'''
for i in range(2,21):
    with open(f'03_multiplication_table/table_of_{i}.txt','w') as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")
