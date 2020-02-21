
def hoogtemeters(list):
     verschil = []
     for i in range(0, len(list)-1):
         verschil.append(list[i + 1] - list[i])

     return verschil



def dalen_en_stijgen(list):
    dalen = 0
    stijgen = 0
    for element in list:
        if element < 0:
            dalen += -(element)
        else:
            stijgen += element

    return(dalen, stijgen)



print(dalen_en_stijgen([-761, 286, -113, 649, -547]))

