red = 12
green = 13
blue = 14


def line_pow(dict):
    return colorDict["red"] * colorDict["green"] * colorDict["blue"]

with open("input.txt") as file:
    id = 0
    total = 0
    for line in file.readlines():
        line = line[line.find(":")+1:]
        id+=1
        colorDict = {"red": 0, "green": 0, "blue": 0}
        # Get max color cubes from bag for each game
        tries = line.split(";")
        for a_try in tries:
            cubes = a_try.split(",")
            for cube_n in cubes:
                print(cube_n.strip().split(" "))
                (number, color) = cube_n.strip().split(" ")
                if int(number) > colorDict[color]: colorDict[color] = int(number)

        total += line_pow(colorDict)
    
    print(total)
