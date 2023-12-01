from classes import Monkey
def turn_into_monkey(id : int, objs : str, operation: str, test : int , m_t : int, m_f : int):
    obj_list = [int(i.strip()) for i in objs.split(",") if i != ""]
    opers = [i for i in operation.split(" ") if i != ""]
    if opers[0] == "old": opers[0] = 0
    if opers[2] == "old": opers[2] = 0
    if opers[1] == "+": opers[1] = 0
    else: opers[1] = 1
    return Monkey(id, obj_list,int(opers[0]), opers[1],int(opers[2]),test, m_t, m_f)

with open("input.txt", "r") as file:
    monkey_list = []
    linecounter = 0
    id = 0
    objs = ""
    operation = ""
    test = 0
    m_true = 0
    m_false = 0
    for line in file.readlines():
        line = line.strip()
        if line == "":
            monkey_list.append(turn_into_monkey(id, objs, operation, test, m_true, m_false))
            linecounter = 0
        else:
            linecounter += 1
            if linecounter == 1:
                pointspos = line.find(":")
                id = int(line[pointspos-2:pointspos].strip())
            elif linecounter == 2:
                objs = line[line.find(":")+1:]
            elif linecounter == 3:
                operation = line[line.find("=")+1:]
            elif linecounter == 4:
                test = int(line[line.find("y")+1:].strip())
            elif linecounter == 5:
                m_true = int(line[line.find("y")+1:].strip())
            elif linecounter == 6:
                m_false = int(line[line.find("y")+1:].strip())
    monkey_list.append(turn_into_monkey(id, objs, operation, test, m_true, m_false))

    # Phases   
    for m in monkey_list:
        objs = len(m.objects)
        for index in range(objs):
            obj = objs.
            #phase 1: Inspection
            
            #phase 2:
            #phase 3:

    for i in monkey_list: print(i.to_string())
