if __name__ == "__main__":
    calories, highest_calories = 0, [0, 0, 0]

    with open("day_1_input.txt", 'r') as file:
        for line in file:
            if line != '\n':
                calories += int(line)
            else:
                highest_calories.sort()
                for i, hc in enumerate(highest_calories):
                    if(hc > calories):
                        break
                    highest_calories[i] = calories
                    break

                calories = 0

    print(f"{highest_calories} => {sum(highest_calories)}")