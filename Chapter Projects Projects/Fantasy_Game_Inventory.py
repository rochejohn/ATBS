

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