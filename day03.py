with open("day03.txt") as f:
    data = [line.strip() for line in f.readlines()]


def main():
    positions_dic = {}
    symbols_pos = []
    for i in range(len(data)):
        number = ""
        positions = []
        for j in range(len(data[0])):
            if data[i][j] == ".":
                if number != "":
                    positions_dic[tuple(positions)] = number
                    number = ""
                    positions = []
            elif data[i][j].isnumeric():
                number += data[i][j]
                positions.append((i, j))
            else:
                if number != "":
                    positions_dic[tuple(positions)] = number
                    number = ""
                    positions = []
                symbols_pos.append((i, j, data[i][j]))
        if number != "":
            positions_dic[tuple(positions)] = number
    
    search_coords = []
    for symbol in symbols_pos:
        x = symbol[0]-1
        for a in range(3):
            # if x < 0 or x > i:
            #     continue
            y = symbol[1]-1
            for b in range(3):
                # if y < 0 or y > j:
                #     continue
                if (x, y) not in search_coords:
                    search_coords.append((x, y))
                y += 1
            x += 1
    
    total = 0
    for coords, number in positions_dic.items():
        for position in coords:
            if position in search_coords:
                total += int(number)
                break
    
    print("======== Part 1 ========")
    print(total)


main()