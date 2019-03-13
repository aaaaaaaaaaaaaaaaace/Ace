m = int(input('Enter bigger integer: '))
n = int(input('Enter smaller integer: '))
factor = n-1
if m % n == 0:
    print(n)

while True:
    if m % factor != 0 and n % factor != 0:
        factor = factor - 1 # what i should be aiming for is when the 'if' thing becomes false, print factor. continue later.
