from classes import Monkey
import sys
rounds = 20
n = len(sys.argv)
if n > 1:
    rounds = int(sys.argv[1])
    print("{0} Rounds".format(sys.argv[1]))

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
    for i in range(rounds):
        for m in monkey_list:
            objs_len = len(m.objects)
            for index in range(objs_len):
                #phase 1: Inspection
                obj = m.inspect()
                obj = m.chill(obj)
                #phase 2:
                monkey_list[m.throw_obj(obj)].objects.append(obj)
                #phase 3:


    # Monkey Business
    monkey_list.sort(key=lambda x: x.inspected, reverse=True)
    monkey_business = monkey_list[0].inspected * monkey_list[1].inspected
    for i in monkey_list: print(i.to_string())
    print(monkey_business)
