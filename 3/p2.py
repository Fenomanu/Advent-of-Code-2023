data_matrix = []
gear_dict = {} # (key = (x,y) : Value = [numbers])

def is_symbol(c):
    #if (not c.isdigit()) and c != ".": print(c)
    return c == "*"

def check_arround(row, col):
    if col > 0:
        if row > 0:
            #Check izq_arriba
            if is_symbol(data_matrix[row-1][col-1]): 
                return (row-1,col-1)
        if row < len(data_matrix)-1:
            #Check dch_arriba
            if is_symbol(data_matrix[row+1][col-1]): 
                return (row+1,col-1)
        #Check arriba
        if is_symbol(data_matrix[row][col-1]): 
            return (row,col-1)
    if col < len(data_matrix[0])-1:
        if row > 0:
            #Check izq_abajo
            if is_symbol(data_matrix[row-1][col+1]): 
                return (row-1,col+1)
        if row < len(data_matrix)-1:
            #Check dch_abajo
            if is_symbol(data_matrix[row+1][col+1]): 
                return (row+1,col+1)
        #Check abajo
        if is_symbol(data_matrix[row][col+1]): 
            return (row,col+1)
    
    if row > 0:
        #Check izq
        if is_symbol(data_matrix[row-1][col]): 
            return (row-1,col)
    if row < len(data_matrix)-1:
        #Check dch
        if is_symbol(data_matrix[row+1][col]): 
            return (row+1,col)
    return (-1,-1)


with open("input.txt") as file:
    for line in file.readlines():
        if line != "":
            line = line.strip()
            row = list(line)
            data_matrix.append(row)

    total_sum = 0


    for row in range(len(data_matrix)):
        #print(data_matrix[row])
        number_to_add = []
        star_coord = (-1,-1)
        flush = False
        for cell in range(len(data_matrix[0])):
            if data_matrix[row][cell].isdigit():
                #print(data_matrix[row][cell])
                number_to_add.append(data_matrix[row][cell])
                #print(number_to_add)
                (x, y) = check_arround(row, cell)
                    #print("Found symbol in {0}".format(data_matrix[row][cell]))
                if (x,y) != (-1, -1):
                    star_coord = (x,y)
                    gear_dict.setdefault((x,y),[])
                    flush = True
                if cell == len(data_matrix[0])-1:
                    if flush:
                        str1 = ""
                        val = int(str1.join(number_to_add))
                        gear_dict[star_coord].append(val)
                        #total_sum += val
                        #print(val)
                    number_to_add = []
                    flush = False
            else:
                #print(data_matrix[row][cell])
                if flush:
                    str1 = ""
                    val = int(str1.join(number_to_add))
                    gear_dict[star_coord].append(val)
                    #total_sum += val
                    #print(val)
                number_to_add = []
                flush = False

    print(gear_dict)
    for v in gear_dict.values():
        if len(v) == 2:
            total_sum += v[0] * v[1]



print(total_sum)