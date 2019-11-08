
naam = input('geef naam: ')

aantal_klinkers = 0

for letter in naam:
    if letter in 'aeoui':
        aantal_klinkers += 1

print(aantal_klinkers, len(naam) - aantal_klinkers)

i = 1

for letter in naam:
    print(i * letter)
    i += 1


