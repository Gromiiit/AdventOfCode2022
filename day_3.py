def identical_items(str1, str2, str3=""):
    if str3 != "":
        return ''.join(set(str1).intersection(str2).intersection(str3))
    return ''.join(set(str1).intersection(str2))

def priority(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1
    elif ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27

if __name__ == "__main__":
    priority_counter = 0
    group = []

    with open("day_3_input.txt", 'r') as file:
        for line in file:
            # first_half = line[0:int(len(line)/2)]
            # second_half = line[int(len(line)/2):]
            # priority_counter += priority(identical_items(first_half, second_half))
            group.append(line[0:-1])

            if len(group) == 3:
                priority_counter += priority(identical_items(group[0], group[1], group[2]))
                group = []

    print(f"{priority_counter}")