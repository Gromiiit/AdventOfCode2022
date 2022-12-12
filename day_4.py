def cleaning_range(pair):
    arr = []

    for p in pair.split('-'):
        arr.append(int(p))

    return range(arr[0], arr[1] + 1) 


if __name__ == "__main__":
    fully_contained = 0
    overlaps = 0
    
    with open("day_4_input.txt", 'r') as file:
        for line in file:
            pairs = line[0:-1].split(',')
            first_range = cleaning_range(pairs[0])
            second_range = cleaning_range(pairs[1])

            if first_range.start >= second_range.stop:
                continue
            elif second_range.start >= first_range.stop:
                continue
            
            # if first_range.start <= second_range.start and first_range.stop >= second_range.stop:
            #     fully_contained += 1
            # elif first_range.start >= second_range.start and first_range.stop <= second_range.stop:
            #     fully_contained += 1

            overlaps += 1

    print(f"{overlaps}")