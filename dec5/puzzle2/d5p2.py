# Day 5 Puzzle 2
from textwrap import wrap


def ingestdata(data):
    score = 0
    chars_in_column = 4
    stacks_dict = {}
    move_list = []
    starting_stack_lines = []

    # Loop will parse rows split them into appropriate lists and
    # process column input data and create lists in stacks_dict for each column
    for line in data:
        if line == '\n':
            continue  # Skipping line if blank
        clean_line = line.strip('\n')  # Remove newline char from string
        if clean_line.startswith(' 1'):  # This is the column labels line
            stacks = line.split()
            for stack in stacks:  # This loop initializes stack_dict with column names
                stack_name = 'stack' + str(stack)
                stacks_dict[stack_name] = []
        elif clean_line.startswith('move'):
            move_list.append(clean_line)
        else:  # When here this line is a stack layer
            starting_stack_lines.insert(0, clean_line)


    # This loop will parse initial stack contents and place them into stack_dict to represent starting configuration
    for line in starting_stack_lines:
        if line == '\n':
            continue
        clean_line = line.strip('\n')  # Remove newline char from string
        stack_row_list = wrap(clean_line, chars_in_column, drop_whitespace=False)
        for index, crate in enumerate(stack_row_list):
            crate_stack_num = index + 1
            stack = stacks_dict['stack' + str(crate_stack_num)]
            stack.append(crate)
            stacks_dict['stack' + str(crate_stack_num)] = stack

    # This will loop over stacks_dict lists and remove empty placeholders from top of stacks
    for listname in stacks_dict:
        list = stacks_dict[listname]
        working_list = []
        for item in list:
            if item == '    ':
                continue
            else:
                working_list.append(item)
        stacks_dict[listname] = working_list

    for instruction in move_list:
        moving_stack = []
        num_of_moves = int(instruction.split()[1])
        source_column = instruction.split()[3]
        destination_column = instruction.split()[5]
        source_stack = stacks_dict['stack' + str(source_column)]
        dest_stack = stacks_dict['stack' + str(destination_column)]
        for move in range(0, num_of_moves):
            moving_crate = source_stack.pop()
            moving_stack.append(moving_crate)
        for item in range(0, num_of_moves):
            moving_crate = moving_stack.pop()
            dest_stack.append(moving_crate)

    return stacks_dict


if __name__ == '__main__':
    inputdata = open('input', 'r')
    ingested = ingestdata(inputdata)
    for listname in ingested:
        list = ingested[listname]
        print(list[len(list)-1])
