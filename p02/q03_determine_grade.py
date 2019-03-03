score = int(input('Score:'))
if 70 <= score <= 100:
  print('You got an A!')
elif 60 <= score <= 69:
  print('You got a B!')
elif 55 <= score <= 59:
  print('You got a C!')
elif 50 <= score <= 54:
  print('You got a D!')
elif 45 <= score <= 49:
  print('You got an E!')
elif 35 <= score <= 44:
  print('You got an S!')
elif 0 <= score <= 34:
  print('You got a U!')
else:
  print('Invalid score.')
