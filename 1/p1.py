def return_value(value):
    res = ""
    for i in value:
        if i.isnumeric():
            res += i
            break
    for i in value[::-1]:
        if i.isnumeric():
            res += i
            break
    return int(res)

content = ""
total = 0
with open("input_1.txt") as file:
    for line in file.readlines():
        if line != "":
            line.strip()
            total += return_value(line)

print(total)