def vlag(richting, kleur):
    uitvoer = ''
    if richting == 'verticaal':
        for i in kleur:
            uitvoer += i + '|'

    else:
        pass

    return uitvoer


print(vlag('verticaal',('zwart', 'geel', 'rood')))
