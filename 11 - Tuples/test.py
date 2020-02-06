singles = (('roos', 9), ('annelies', 7), ('mieke', 10))
uitvoer = '{} is een lekker {}-tje'



for single in singles:
    print(uitvoer.format(single[0], single[1]))
