def reverseStr(number):
    i = len(number)

    while i != 0:
        print(number[i-1], end ="")
        i = i - 1
    
reverseStr(str(input("Enter number:")))
