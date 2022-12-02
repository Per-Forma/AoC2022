def ingestdata(data):
    ingesteddata = {}
    elf_number = 0
    calories_carried = 0
    for line in data:
        if line == '\n':  # End of current elf due to blank line
            # Save elf number and calorie amount to ingesteddata dict
            ingesteddata['elf_' + str(elf_number)] = calories_carried
            # Reset calorie count
            calories_carried = 0
            # Increment elf
            elf_number += 1
            # Here we need to increment to next line to avoid processing blank line as a calorie counting item
            continue
        clean_line = line.strip('\n')  # Remove newline char from input line
        line_calories = int(clean_line)  # Convert clean_line to integer
        calories_carried += line_calories
    return ingesteddata


if __name__ == '__main__':
    inputdata = open('input', 'r')
    ingested = ingestdata(inputdata)
    calorie_list = []
    for elf in ingested:
        calorie_total = ingested.get(elf)
        calorie_list.append(calorie_total)
    calorie_list.sort(reverse=True)
    print(calorie_list[0])
