month = int(input('Enter month:'))
year = int(input('Enter year:'))

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
  print('February' + ' ' + str(year) + ' has 29 days.')
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  print(months[month-1] + ' has 31 days')
elif month == 4 or month == 6 or month == 9 or month == 11:
  print_months[month-1] + ' has 30 days')
elif month == 2 and year % 4 != 0:
  print('February' + ' ' + str(year) + ' has 28 days.')
else:
  print('Invalid month')
