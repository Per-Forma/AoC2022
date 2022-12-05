# Day 3 Puzzle 1
import sys
import string


def ingestdata(data):
    total_rucksack_points = 0
    point_dict = {}
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    matches_list = []
    rs_group = []
    for index, letter in enumerate(lowercase):
        point_dict[letter] = index+1
    for index, letter in enumerate(uppercase):
        point_dict[letter] = index+27

    for index, rs_contents in enumerate(data):
        if rs_contents == '\n':
            continue  # Skipping line if blank
        rs_contents = rs_contents.strip('\n')  # Remove newline char from string

        rs_count = index + 1
        rs_group.append([*rs_contents])
        if (rs_count % 3) is 0:
            intersection12 = set(rs_group[0]).intersection(set(rs_group[1]))
            commonitem = intersection12.intersection(set(rs_group[2]))
            matches_list.append(commonitem)
            rs_group = []  # Clear to prepare for next rucksack group processing series

    for item in matches_list:
        item = list(item)[0]  # Extract string from item set
        item_score = point_dict[item]  # Calculate points of item
        total_rucksack_points += item_score  # Add item points to running total
    return total_rucksack_points


if __name__ == '__main__':
    inputdata = open('input', 'r')
    ingested = ingestdata(inputdata)
    print(ingested)
