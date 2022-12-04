# Day 3 Puzzle 1
import sys
import string


def ingestdata(data):
    total_rucksack_points = 0
    point_dict = {}
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    matches_list = []
    for index, letter in enumerate(lowercase):
        point_dict[letter] = index+1
    for index, letter in enumerate(uppercase):
        point_dict[letter] = index+27
    for rs_contents in data:
        if rs_contents == '\n':
            continue  # Skipping line if blank
        rs_contents = rs_contents.strip('\n')  # Remove newline char from string
        item_count = len(rs_contents)  # Get length of rucksack contents
        if (item_count % 2) != 0:
            sys.exit("Not an even number of items in sack")
        rs_compartment_1 = rs_contents[:int(item_count/2)]
        rs_compartment_2 = rs_contents[int(item_count/2):]
        for item in rs_compartment_1:
            if item in rs_compartment_2:
                if item in matches_list:
                    continue
                else:
                    matches_list.append(item)
    for item in matches_list:
        item_score = point_dict[item]
        total_rucksack_points += item_score
    return total_rucksack_points


if __name__ == '__main__':
    inputdata = open('input2', 'r')
    ingested = ingestdata(inputdata)
    print(ingested)
