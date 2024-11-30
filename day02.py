with open("day02.txt") as f:
    data = [line.lstrip("Game ").strip() for line in f.readlines()]


def main():
    total = 0
    power_sum = 0

    for line in data:
        value = int(line.split(":")[0])
        sub_sets = line.split(":")[1].split(";")
        counted = True
        red_h = 1
        green_h = 1
        blue_h = 1

        for sub_sub_set in sub_sets:
            cubes = sub_sub_set.split(",")

            for cube in cubes:
                cube = cube.strip(" ")
                cube_tuple = (int(cube.split(" ")[0]), cube.split(" ")[1])
                
                match cube_tuple[1]:
                    case "red":
                        if cube_tuple[0] > 12:
                            counted = False
                        if cube_tuple[0] > red_h:
                            red_h = cube_tuple[0]
                    case "green":
                        if cube_tuple[0] > 13:
                            counted = False
                        if cube_tuple[0] > green_h:
                            green_h = cube_tuple[0]
                    case "blue":
                        if cube_tuple[0] > 14:
                            counted = False
                        if cube_tuple[0] > blue_h:
                            blue_h = cube_tuple[0]

        if counted:
            total += value 
        power = red_h * blue_h * green_h
        power_sum += power

    print("======== Part 1 ========")
    print(total)
    print("======== Part 2 ========")
    print(power_sum)


main()
