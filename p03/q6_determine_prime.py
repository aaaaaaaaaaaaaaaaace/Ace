def is_prime(n):
    check = True

    for i in range(2,n):
        if n == 2:
            break
        elif n % i == 0:
            check = False

    if check == True:
        print(n)
    

count=0
n=2
while count!=1000:
    if is_prime(n):
        if count%10==0:
            print()
        print(n,end=" ")
        count= count + 1
    n = n + 1
