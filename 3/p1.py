data_matrix = []

def is_symbol(c):
    #if (not c.isdigit()) and c != ".": print(c)
    return (not c.isdigit()) and c != "."

def check_arround(row, col):
    if col > 0:
        if row > 0:
            #Check izq_arriba
            if is_symbol(data_matrix[row-1][col-1]): 
                return True
        if row < len(data_matrix)-1:
            #Check dch_arriba
            if is_symbol(data_matrix[row+1][col-1]): 
                return True
        #Check arriba
        if is_symbol(data_matrix[row][col-1]): 
            return True
    if col < len(data_matrix[0])-1:
        if row > 0:
            #Check izq_abajo
            if is_symbol(data_matrix[row-1][col+1]): 
                return True
        if row < len(data_matrix)-1:
            #Check dch_abajo
            if is_symbol(data_matrix[row+1][col+1]): 
                return True
        #Check abajo
        if is_symbol(data_matrix[row][col+1]): 
            return True
    
    if row > 0:
        #Check izq
        if is_symbol(data_matrix[row-1][col]): 
            return True
    if row < len(data_matrix)-1:
        #Check dch
        if is_symbol(data_matrix[row+1][col]): 
            return True


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
        flush = False
        for cell in range(len(data_matrix[0])):
            if data_matrix[row][cell].isdigit():
                #print(data_matrix[row][cell])
                number_to_add.append(data_matrix[row][cell])
                #print(number_to_add)
                if check_arround(row, cell):
                    #print("Found symbol in {0}".format(data_matrix[row][cell]))

                    flush = True
                if cell == len(data_matrix[0])-1:
                    if flush:
                        str1 = ""
                        val = int(str1.join(number_to_add))
                        total_sum += val
                        #print(val)
                    number_to_add = []
                    flush = False
            else:
                #print(data_matrix[row][cell])
                if flush:
                    str1 = ""
                    val = int(str1.join(number_to_add))
                    total_sum += val
                    #print(val)
                number_to_add = []
                flush = False




print(total_sum)