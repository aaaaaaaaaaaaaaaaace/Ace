s1 = int(input('Side 1: '))
s2 = int(input('Side 2: '))
s3 =int(input('Side 3: '))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
  print('The perimeter of the triangle is ' + str(s1 + s2 + s3))
else:
  print('Invalid triangle.')
