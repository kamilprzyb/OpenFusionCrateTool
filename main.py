import xlrd
import json

path = "input.xlsx"
book = xlrd.open_workbook(path)
tables = {}

for sheet in book.sheets():
    colls = []
    objects = []
    for i in range(sheet.ncols):
        # define collumns
        # if collumn name starts with '/' ignore it
        if sheet.cell_value(0, i)[0] != '/':
            # if collumn name ends with '+' mark it as list
            coll_type = 0
            if sheet.cell_value(0, i)[-1] == '+':
                coll_type = 1
            elif sheet.cell_value(0, i)[-1] == '-':
                coll_type = 2
            coll_name = sheet.cell_value(0, i) if coll_type == 0 else sheet.cell_value(0, i)[0:-1]
            collumn = (i, coll_name, coll_type)
            colls.append(collumn)
    # with collumns defined
    # read all rows
    for i in range(1, sheet.nrows):
        add_object = {}
        for j in colls:
            # if array
            if j[2] == 1:
                add_object[j[1]] = str(sheet.cell_value(i, j[0])).split(";")
                # this fixes a weird quirk with single numbers
                if len(add_object[j[1]]) == 1:
                    add_object[j[1]] = [int(sheet.cell_value(i, j[0]))]
                else:
                    add_object[j[1]] = list(map(int, add_object[j[1]]))
            # if string
            elif j[2] == 2:
                add_object[j[1]] = str(sheet.cell_value(i, j[0]))
            else:
                add_object[j[1]] = int(sheet.cell_value(i, j[0]))
        objects.append(add_object)
    tables[sheet.name] = objects
save = open("drops.json", "w")
save.write(json.dumps(tables))
print("Success. Press Enter to close")
whatever = input()
