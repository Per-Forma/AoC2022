# Day 5 Puzzle 1
import sys
from textwrap import wrap
from collections import Counter


def ingestdata(data):
    start_of_unique_buffer = 0
    chars_in_buffer = 4

    # Problem only requires processing a single line
    line = data.readline()
    clean_line = line.strip('\n')  # Remove newline char from string
    char_bytes = [*clean_line]  # Converts string into list of individual characters
    buffer_selection = []
    for count in range(0, (chars_in_buffer - 1)):
        single_char = char_bytes.pop(0)
        buffer_selection.append(single_char)
    for index, char in enumerate(char_bytes):
        buffer_selection.append(char)
        if len(buffer_selection) > 4:
            buffer_selection.pop(0)
        count_of_uniques = Counter(buffer_selection)

        if len(count_of_uniques) < 4:
            continue
        # To calculate winner, we need to add 4 to index to calculate how many characters were processed.
        # Three for the initialization loop, and one for the start from 0 index
        start_of_unique_buffer = index + 4
        break
    return start_of_unique_buffer


if __name__ == '__main__':
    inputdata = open('../input', 'r')
    ingested = ingestdata(inputdata)
    print(ingested)
