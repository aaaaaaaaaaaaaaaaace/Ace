m = int(input('Enter bigger integer: '))
n = int(input('Enter smaller integer: '))
factor = n-1

while True:
    a = m % factor
    b = n % factor
    
    if m < n:
        print('Enter the larger integer first')
        break
    
    elif a or b != 0:
        factor = factor - 1
        
    elif m % n == 0:
        print(n)
        break

    elif a == 0 and b == 0:
        print(factor)
        break
        
