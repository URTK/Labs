def shuffle(suit):
    counter = 0
    value = suit[0]
    for item in suit:
        if item == value:
            counter += 1
        else:
            counter = 0
            value = item
        if counter >= 3:
            return True
    return False


packOfCards = ['Черви','Черви','Черви']

print(shuffle(packOfCards))
