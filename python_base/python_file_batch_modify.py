
import os
import shutil


def batch_move(path):
    for foldername in os.listdir(path):
        path_01 = os.path.join(path, foldername)    # child file(dir)
        if os.path.isfile(path_01):  # if child file is a dir, continue
            continue
        print(foldername)
        for filename in os.listdir(path_01):
            # tmp_path = "\\" + foldername + "\\" + filename
            path_02 = os.path.join(path_01, filename)
            print(path_02)
            if os.path.isfile(path_02) and filename.endswith(".avi"):
                shutil.move(path_02, path)


def batch_remove(path):
    for foldername in os.listdir(path):
        child_path = os.path.join(path, foldername)
        if os.path.isdir(child_path):
            # os.remove(child_path)    # only delete empty dir
            shutil.rmtree(child_path)  # delete empty dir or not empty dir


def batch_rename(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if filename.find('.') > 0:
                new_filename = filename.replace("xxxxx",'')
                os.rename(os.path.join(path,filename), os.path.join(path, new_filename))


if __name__ == '__main__':
    path = r"/path"
    # batch_move(path)
    # batch_remove(path)
    batch_rename(path)
