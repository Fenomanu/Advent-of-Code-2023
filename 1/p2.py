def replace_numbers(value):
    return value.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")

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
            total += return_value(replace_numbers(line))

print(total)