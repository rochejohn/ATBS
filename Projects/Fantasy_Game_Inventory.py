'''Part One'''

bagpack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):

    print('\nInventory:\n')

    num_items_count = 0

    for k,v in inventory.items():
        if v > 1:
            print(str(v) + ' ' + str(k) +'\'s' )
            num_items_count += v

        else:
            print(str(v) + ' ' + str(k))
            num_items_count += v

    print('\nTotal number of Items: ' + str(num_items_count))


displayInventory(bagpack)

'''
Part 2

Add a fallen dragons list of items to your bagpack
'''

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1

addToInventory(bagpack,dragonLoot)

displayInventory(bagpack)











