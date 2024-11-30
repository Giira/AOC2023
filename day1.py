with open("day1.txt") as f:
    data = [line.strip() for line in f.readlines()]



def text_to_int(data):
    for index, line in enumerate(data):
        line = line.replace("one", "on1e")
        line = line.replace("two", "tw2o")
        line = line.replace("three", "thr3ee")
        line = line.replace("four", "fo4ur")
        line = line.replace("five", "fi5ve")
        line = line.replace("six", "si6x")
        line = line.replace("seven", "sev7en")
        line = line.replace("eight", "eig8ht")
        line = line.replace("nine", "ni9ne")
        data[index] = line
    return data



def main(data):
    values = []

    for line in data:
        value = ""
        for character in line:
            if character.isnumeric():
                value += character
                break
        
        for character in line[::-1]:
            if character.isnumeric():
                value += character
                break
        
        values.append(value)

    print(sum(int(value) for value in values))


main(text_to_int(data))
