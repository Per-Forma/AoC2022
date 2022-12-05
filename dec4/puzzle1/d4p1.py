# Day 4 Puzzle 1


def ingestdata(data):
    score = 0
    for line in data:
        if line == '\n':
            continue  # Skipping line if blank
        sites = line.strip('\n')  # Remove newline char from string
        seperate_sites = sites.split(',')
        elf1sitesrange = seperate_sites[0].split('-')
        elf2sitesrange = seperate_sites[1].split('-')
        elf1sites = list(range(int(elf1sitesrange[0]), int(elf1sitesrange[1])+1))
        elf2sites = list(range(int(elf2sitesrange[0]), int(elf2sitesrange[1])+1))
        if all(item in elf1sites for item in elf2sites) or all(item in elf2sites for item in elf1sites):
            score += 1
    return score

if __name__ == '__main__':
    inputdata = open('input', 'r')
    ingested = ingestdata(inputdata)
    print(ingested)
