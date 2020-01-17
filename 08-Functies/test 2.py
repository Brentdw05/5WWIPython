def welkom(naam):
    print('Welkom terug ' + naam)

welkom('Dominiek')
welkom(str(1))
welkom(str(True))
welkom(str(welkom('Dominiek')))

test = welkom('Dominiek')
print(test)
