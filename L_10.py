import random

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
            return 0
    return 'Колода не содержит 3 карты одной масти подряд'


packofCards = ['Крести','Крести','Крести','Крести','Крести','Крести','Крести','Крести','Крести','Пики','Пики','Пики','Пики','Пики','Пики','Пики','Пики','Пики','Черви','Черви','Черви','Черви','Черви','Черви','Черви','Черви','Черви','Буби','Буби','Буби','Буби','Буби','Буби','Буби','Буби','Буби']
random.shuffle(packofCards)

print(packofCards, end = '\n\n')
print('return function shuffle:',shuffle(packofCards))
