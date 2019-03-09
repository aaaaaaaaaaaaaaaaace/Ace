n = 1
x = n**3

while x < 12000:
  n = n + 1
  x = n**3
  if x > 12000:
    break
    
n = n - 1
print('The largest integer n such that n^3 is less than 12000 is' , n)
