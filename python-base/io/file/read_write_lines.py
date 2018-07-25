
FILE_PATH = r"D:\work_material\project-document\RTDGW-实时数据网关\生产环境topic提数\jdqDataExtract_2018072412-2018072512.txt"

rows = []
with open(FILE_PATH, 'r') as stat_file:
    counter = 0
    for line in stat_file:
        rows.append(line)
        counter += 1
        if counter == 10:
            break

DIST_PATH = r"D:\work_material\project-document\RTDGW-实时数据网关\生产环境topic提数\jdqDataExtract_2018072412-2018072512_head10.txt"
with open(DIST_PATH, 'w') as file:
    file.writelines(rows)