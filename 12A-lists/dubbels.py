
def dubbels(list):
    res = []

    for element in list:
        # als element 2 x voorkomt in lijst en element nog niet voorkomt in res
        if list.count(element) > 1 and element not in res:
            res.append(element)

    return res
