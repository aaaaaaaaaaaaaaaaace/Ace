def miles_to_kilometers(max_kilo):
    miles = 0
    print("miles" + "\t\t" + "kilometers", "\t", 'kilometers', '\t\t', 'miles')
    for miles in range(max_kilo):
        miles = miles + 1
        kilometers = miles * 1.609
        print(miles , "\t\t" , "{0:.3f}".format(kilometers), "\t\t", (miles * 5 + 15), '\t\t', "{0:.3f}".format(((kilometers * 5 + 15) /1.609)))
        

miles_to_kilometers(10)
