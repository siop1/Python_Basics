# Give today day and date and it will calculate which date is which day within a month

days_list=['sun','mon','tue','wed','thur','fri','sat']
date1=int(input("Enter current date :"))
day1=input("Enter current day :")
date2=int(input('Enter date for which you want day: '))

for i in range(0,len(days_list)):
    if days_list[i]==day1:
        index=i

if date2>=date1:
    diff=date2-date1
    day2=days_list[index+(diff%7)]
else:
    diff=date1-date2
    day2=days_list[index-(diff%7)]



print(day2)