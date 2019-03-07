def kilograms_to_pounds(max_kilo):
    kilograms = 0
    print("kilograms" + "\t" + "pounds")
    for kilograms in range(max_kilo):
        kilograms = kilograms + 1
        pounds = kilograms * 2.2
        print((kilograms , "\t\t" , pounds)


kilograms_to_pounds(10)
