cells = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
cells_len = len(cells)
cell_len = len(cells[0])
y_added = cells_len + 2
x_added = cell_len + 2

for index in range(y_added):
    new_list = []
    if index == 0:
        for i in range(x_added):
            new_list.append(0)
        cells.insert(0, new_list)
    elif index == y_added - 1:
        for i in range(x_added):
            new_list.append(0)
        cells.insert(index, new_list)
    else:
        cells[index].insert(0, 0)
        cells[index].append(0)

print(cells)
