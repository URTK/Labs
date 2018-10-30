packofCards = ['Трефы', 'Черви', 'Черви', 'Черви']

# Если нужно найти последовательность из 3х карт любой масти.

def shuffle(pack):
    counter = 0
    for i in range(1, len(pack)):
        if pack[i] == pack[i - 1]:
            counter += 1
            if counter == 2:
                return pack[i]
        else:
            counter = 0
    return 'Нет трех идущих подряд карт одной масти'

print(shuffle(packofCards))



# Если нужно найти последовательность карт  определенной масти.

sought_val = 'Черви'


def shuffle(pack, val):
    counter = 0
    for i in range(len(pack)):
        if pack[i] == val:
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


print(shuffle(packofCards, sought_val))

packofCards = ['Черви','Черви','Черви']
value = packofCards[0]

def shuffle(packofCards):
    counter = 0
    for index, item in enumerate(packofCards):
        if item == value:
            value = item
            counter += 1
            if counter >=3:
                return 0
            else:
                return 'Нет трех идущих подряд карт одной масти'

print(shuffle(packofCards))
