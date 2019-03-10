number = 120
factor = 2
while number % factor == 0:
    number = number / factor
    print(factor)
    if number % factor != 0:
        factor = factor + 1
        while number % factor == 0:
            number = number / factor
            print(factor)
            if number % factor != 0:
                factor = factor + 2
                while number % factor == 0:
                    number = number / factor
                    print(factor)
                    if number % factor != 0:
                        factor = factor + 2
                        while number % factor == 0:
                            number = number / factor
                            print(factor)
                        if factor > number:
                            break
                        elif factor == number:
                            print(factor)
                        else:
                            break
