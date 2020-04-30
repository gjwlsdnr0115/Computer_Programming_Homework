import datetime

month_birth_1 = int(input('Person 1: Enter month born (1-12): '))
day_birth_1 = int(input('Person 1: Enter day born (1-31): '))
year_birth_1 = int(input('Person 1: Enter year born (4-digit): '))

month_birth_2 = int(input('Person 2: Enter month born (1-12): '))
day_birth_2 = int(input('Person 2: Enter day born (1-31): '))
year_birth_2 = int(input('Person 2: Enter year born (4-digit): '))

current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

numsecs_1900_today = ((current_year - 1900) * avg_numsecs_year) + ((current_month - 1) * avg_numsecs_month) + (current_day * numsecs_day)
numsecs_1900_p1 = ((year_birth_1 - 1900) * avg_numsecs_year) + ((month_birth_1 - 1) * avg_numsecs_month) + (day_birth_1 * numsecs_day)
numsecs_1900_p2 = ((year_birth_2 - 1900) * avg_numsecs_year) + ((month_birth_2 - 1) * avg_numsecs_month) + (day_birth_2 * numsecs_day)

age_in_secs_p1 = numsecs_1900_today - numsecs_1900_p1
age_in_secs_p2 = numsecs_1900_today - numsecs_1900_p2

result = abs(age_in_secs_p1 - age_in_secs_p2)

print('Age difference in seconds: {}'.format(result))