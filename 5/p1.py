seeds = ""
text = []

with open("input.txt") as file:
    seeds = file.readline()
    seeds = [i for i in seeds[seeds.find(":")+1:].split() if len(i) > 0]
    for line in file.readlines():
        line = line.strip()
        if line != "":
            text.append(line)
        
print(seeds)
print(text[0])