year_of_birth = int(input('Enter your birth year : '))
month_of_birth = int(input('Enter your birth month : '))
present_year = int(input('Enter present year : '))
present_month = int(input('Enter present month : '))
if (12 - month_of_birth + present_month)>12:
    print((present_year - year_of_birth - 0), 'years,', str(12 - month_of_birth + present_month-12), 'months')
else:
    print(((present_year - year_of_birth) - 1), 'years,', str(12 - month_of_birth + present_month), 'months')