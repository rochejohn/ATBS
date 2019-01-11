
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def table_printer(bag):
    colWidths = [0] * len(bag)
    for outlist in range(len(bag)):
        mx = 0
        for innerlist in range(len(bag[outlist])):
            if len(bag[outlist][innerlist]) > mx:
                mx = len(bag[outlist][innerlist])
        colWidths[outlist] = mx



    for i in range(len(bag[0])):


        for o in range(len(bag)):


            print(bag[o][i].rjust(colWidths[o]), end=" ")

        print("")


table_printer(tableData)