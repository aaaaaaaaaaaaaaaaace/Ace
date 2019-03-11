def pattern(n):
    n = int(input('Enter number: '))
    for i in range(1,n + 1):
        n = i

        print('')
        while n != 0:
            print(n, end=' ')
            n = n - 1
        

pattern(n)
