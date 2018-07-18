
import os

def batch_rename(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if filename.find('.') > 0:
                new_filename = filename.replace('传智播客汤阳光Hibernate教程__','')
                os.rename(os.path.join(path,filename), os.path.join(path, new_filename))

if __name__ == '__main__':
    path_01 = r"D:\BaiduYunDownload\Database\Hibernate\Hibernate——汤阳光（精）\video"
    path_02 = r"D:\BaiduYunDownload\Database\Hibernate\Hibernate——汤阳光（精）\video\已看"
    batch_rename(path_02)