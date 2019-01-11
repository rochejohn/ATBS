
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def table_printer(lst):
    colWidths = [0] * len(tableData)
    for outlist in range(len(tableData)):
        mx = 0
        for innerlist in range(len(tableData[outlist])):
            if len(tableData[outlist][innerlist]) > mx:
                mx = len(tableData[outlist][innerlist])
        colWidths[outlist] = mx
    return colWidths

print(table_printer(tableData))

