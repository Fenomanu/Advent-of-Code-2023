total_sum = 0

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        left, right = line[line.find(":")+1:line.find("|")],line[line.find("|")+1:]
        print([i for i in left.split(" ") if len(i) > 0])
        print([i for i in right.split(" ") if len(i) > 0])
        res = set([i for i in left.split(" ") if len(i) > 0]).intersection([i for i in right.split(" ") if len(i) > 0])
        print(res)
        if len(res) > 0: total_sum += pow(2, len(res)-1)

print(int(total_sum))