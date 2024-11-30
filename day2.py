with open("day2.txt") as f:
    data = [line.lstrip("Game ").strip() for line in f.readlines()]


def main():
    total = 0
    for line in data:
        value = int(line.split(":")[0])
        sub_sets = line.split(":")[1].split(";")
        counted = True

        for sub_sub_set in sub_sets:
            cubes = sub_sub_set.split(",")

            for cube in cubes:
                cube = cube.strip(" ")
                cube_tuple = (int(cube.split(" ")[0]), cube.split(" ")[1])
                
                match cube_tuple[1]:
                    case "red":
                        if cube_tuple[0] > 12:
                            counted = False
                    case "green":
                        if cube_tuple[0] > 13:
                            counted = False
                    case "blue":
                        if cube_tuple[0] > 14:
                            counted = False

        if counted:
            total += value 
    print("======== Part 1 ========")
    print(total)


main()
