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
                    positions_dic[number] = positions
                    number = ""
                    positions = []
            elif data[i][j].isnumeric():
                number += data[i][j]
                positions.append((i, j))
            else:
                if number != "":
                    positions_dic[number] = positions
                    number = ""
                    positions = []
                symbols_pos.append((i, j, data[i][j]))
    
    print(symbols_pos)
    print(positions_dic)


main()