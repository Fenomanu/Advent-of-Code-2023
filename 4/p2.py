total_sum = 0
lines = 0
with open("input.txt") as file:
    lines = len(file.readlines())

repetitions = [1 for i in range(lines * 2)]

with open("input.txt") as file:
    id = 0
    for line in file.readlines():
        id += 1
        line = line.strip()
        left, right = line[line.find(":")+1:line.find("|")],line[line.find("|")+1:]
        print([i for i in left.split(" ") if len(i) > 0])
        print([i for i in right.split(" ") if len(i) > 0])
        res = set([i for i in left.split(" ") if len(i) > 0]).intersection([i for i in right.split(" ") if len(i) > 0])
        print(res)
        if len(res) > 0: 
            for i in range(len(res)):
                repetitions[(id) + i] += 1 * repetitions[id-1]
    print(repetitions)

print(sum(repetitions[:lines]))
