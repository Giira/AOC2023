with open("day03.txt") as f:
    data = [line.strip() for line in f.readlines()]


def neighbours(coord):
    neighbours = []
    i = coord[0] - 1
    for a in range(3):
        j = coord[1] - 1
        for b in range(3):
            neighbours.append((i, j))
            j += 1
        i += 1
    return neighbours
        


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
            if x < 0 or x > i:
                continue
            y = symbol[1]-1
            for b in range(3):
                if y < 0 or y > j:
                    continue
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

    asterisks = []
    counts = {}
    for symbol in symbols_pos:
        if symbol[2] == "*":
            asterisks.append((symbol[0], symbol[1]))
    for asterisk in asterisks:
        counts[asterisk] = []
        
    for coords, number in positions_dic.items():
        for position in coords:
            for asterisk in asterisks:
                if position in neighbours(asterisk):
                    if number not in counts[asterisk]:
                        counts[asterisk].append(number)
                    
    total_2 = 0
    for asterisk, count in counts.items():
        if len(count) == 2:
            total_2 += int(count[0]) * int(count[1])


    
    print("======== Part 1 ========")
    print(total)

    print("======== Part 2 ========")
    print(total_2)


main()