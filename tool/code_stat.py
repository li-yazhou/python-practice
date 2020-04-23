# coding=utf-8

import os
# import time
import re

# basedir = '/Users/liyazhou1/self-repo/python-practice'
# filepath = '/Users/liyazhou1/self-repo/python-practice/tool/code_stat.py'
# desttype = 'python'

basedir = '/Users/liyazhou/Repo/open-repo/kafka'
desttype = 'java'


file_types = {'java':['.java', '.scala'], 'python': ['.py']}
re_py_comment = re.compile('[(#)]')
re_java_comment = re.compile('[(//)(/*)(*)(*/)]')
comment_types = {'java': re_java_comment, 'python': re_py_comment}

file_nums = 0
max_file = ''
filepath_list = []

total_lines = 0
code_lines = 0
blank_lines = 0
comment_lines = 0


def is_python_file(filename):
    return os.path.splitext(filename)[1] == '.py'


def check_file(filepath):
    valid_types = file_types[desttype]
    for valid_type in valid_types:
        if os.path.splitext(filepath)[1] == valid_type:
            global file_nums
            file_nums += 1
            return True
    return False


def stat_file(filepath):
    valid_file = check_file(filepath)
    if not valid_file:
        return False, 0, 0, 0, 0

    file_lines = file_code_lines = file_comment_lines = file_blank_lines = 0
    with open(filepath, 'r') as f:
        f.seek(0)
        for line in f:
            file_lines += 1
            line = line.strip()
            if line == '':
                file_blank_lines += 1
            else:
                if (desttype == 'python' and re_py_comment.match(line)) or (desttype == 'java' and re_java_comment.match(line)):
                    file_comment_lines += 1
                else:
                    file_code_lines += 1
    result = (True, file_lines, file_code_lines, file_comment_lines, file_blank_lines)
    global filepath_list
    filepath_list.append({filepath: result})
    return result


def stat_dir(basedir):
    global total_lines, code_lines, comment_lines, blank_lines
    for parent, dirnames, filenames in os.walk(basedir):
        for filename in filenames:
            filepath = os.path.join(parent, filename)
            success, file_lines, file_code_lines, file_comment_lines, file_blank_lines = stat_file(filepath)
            if success:
                total_lines += file_lines
                code_lines += file_code_lines
                comment_lines += file_comment_lines
                blank_lines += file_blank_lines


def dir_stat_result():
    print("total file num: ", file_nums)
    print("file list: ")
    for result in filepath_list:
        for filepath, filestat in result.items():
            print(filepath, ',', filestat, end='\n')
    print("total lines: ", total_lines)
    print("code lines: ", code_lines)
    print("comment lines: ", comment_lines)
    print("blank lines: ", blank_lines)


def file_stat_result(result_tuple):
    print("total lines: ", result_tuple[1])
    print("code lines: ", result_tuple[2])
    print("comment lines: ", result_tuple[3])
    print("blank lines: ", result_tuple[4])


def stat_one_dir(basedir):
    stat_dir(basedir)
    dir_stat_result()


def stat_one_file(filepath):
    result = stat_file(filepath)
    file_stat_result(result)


if __name__ == '__main__':
    # stat_one_file(filepath)
    print('------------------')
    stat_one_dir(basedir)