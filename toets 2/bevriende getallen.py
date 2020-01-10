#invoer

a = int(input('geef een getal a: '))
b = int(input('geef een getal b: '))
som_delers_a = 0
som_delers_b = 0

#berekening

for i in range(1, a + 1):
    if a % i == 0 and i != a:
        som_delers_a += i
    else:
        som_delers_a += 0

for i in range(1, b + 1):
    if b % i == 0 and i != b:
        som_delers_b += i
    else:
        som_delers_b += 0

if som_delers_a == b and som_delers_b == a:
    uitvoer = '{} en {} zijn bevriende getallen'
else:
    uitvoer = '{} en {} zijn geen bevriende getallen'

#uitvoer

print(uitvoer.format(a, b))
