
rows = []


def read_rows():
    FILE_PATH = r"src_file.txt"
    counter = 0
    with open(FILE_PATH, 'r') as stat_file:
        for line in stat_file:
            # rows.append(line)
            counter += 1
            if counter == 1 or counter == 1000 or counter == 2000 or counter == 3000 or counter == 4000 or counter == 4924:
                print(counter, ", ", line)
    print("counter = ", counter)


def write_rows():
    DIST_PATH = r"dist_file.txt"
    with open(DIST_PATH, 'w') as file:
        file.writelines(rows)


if __name__ == '__main__':
    read_rows()