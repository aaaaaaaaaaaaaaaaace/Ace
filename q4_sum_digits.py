number = int(input('What is your number?' ))

ones_digit = number%10

first_two_digits = number//10

tens_digit = first_two_digits%10

hundreds_digit = number//100

sum = ones_digit + tens_digit + hundreds_digit

print('The sum of the integers in the number is ' + str(sum))
