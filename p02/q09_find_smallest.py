n = 1
x = n*n

while x < 12000:
  n = n+1
  x = n*n
  if x > 12000:
    break

print('The smallest integer n such that n^2 is greater than 12,000 is',n)
