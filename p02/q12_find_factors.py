 def getNextFactor(factor):
    factor=factor+1
    while True:
        for i in range(2,factor):
            if factor % i == 0:
                #print ( factor,"is divisble by",i)
                factor = factor+1
                break
        else:
            #print (factor, "is a prime")
            break
    return factor        


def getAllFactors(number):
    factor = 2
    while True:

              if (number % factor == 0):
                print(factor)
                number = number / factor
              else:
                factor=getNextFactor(factor)

              if factor > number:
                break
            
number = int(input('Enter number:'))
getAllFactors(number) 
