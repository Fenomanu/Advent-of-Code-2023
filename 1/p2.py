numbers = ["one","two","three","four","five","six","seven","eight","nine"]
numbersdict = {"one":-1, "two":-1, "three":-1, "four":-1, "five":-1, "six":-1, "seven":-1, "eight":-1, "nine":-1}
numbersvalue = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def clear_dict():
    for i in numbers:
        numbersdict[i] = -1

def replace_string_for_number(value : str):
    clear_dict()
    for number in numbers:
        numbersdict[number] = value.find(number)
    
    sorted_positions = [i for i in sorted(numbersdict.items(), key=lambda x:x[1]) if i[1] >= 0]

    if len(sorted_positions) > 0:
        (firstnumber, firstpos) = sorted_positions[0]
        (lastnumber, lastpos) = sorted_positions[len(sorted_positions)-1]
        if lastpos < firstpos + len(firstnumber):
            value = value[:firstpos] + numbersvalue[firstnumber] + value[firstpos + len(firstnumber):]
        else: value = value[:firstpos] + numbersvalue[firstnumber] + value[firstpos + len(firstnumber):lastpos] + numbersvalue[lastnumber] + value[lastpos + len(lastnumber):]

    #value = value[:lastpos] + numbersvalue[lastnumber] + value[len(lastnumber):]

    #value[firstpos:len(firstnumber)] = numbersvalue[firstnumber]
    #value[lastpos:len(lastnumber)] = numbersvalue[lastnumber]
    print(value)
    return value

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