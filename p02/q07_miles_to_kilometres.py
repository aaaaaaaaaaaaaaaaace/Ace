def miles_to_kilometers(max_kilo):
    print('{:<6}{:<12}{:<6}{:<12}'.format('Miles', 'Kilometers'))
    for miles in range(1, max_kilo+1):
        print('{:<6}{:<12}{:<6}{:<12}'.format(miles, miles*1.609, miles*5+15, (miles*5+15)*1.609))
        

miles_to_kilometers(10)
