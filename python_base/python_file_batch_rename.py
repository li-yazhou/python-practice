
import os

def batch_rename(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if filename.find('.') > 0:
                new_filename = filename.replace('尚学堂_肖斌','')
                os.rename(os.path.join(path,filename), os.path.join(path, new_filename))

def batch_rename_foldername(path):
    for foldername in os.listdir(path):
        print(foldername)
        if foldername.find('云帆大数据_Hadoop从入门到上手企业开发') != -1:
            new_foldername = foldername.replace('云帆大数据_Hadoop从入门到上手企业开发','')
            os.rename(os.path.join(path,foldername),os.path.join(path, new_foldername))


def batch_rename_image(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if filename.find('.') != -1:
            	new_filename = "python_lang_" + filename
            	os.rename(os.path.join(path,filename), os.path.join(path, new_filename))

def batch_rename_image_02(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            idx = filename.find(".")
            if idx != -1:
            	new_filename = filename[:idx]
            	os.rename(os.path.join(path,filename), os.path.join(path, new_filename))

if __name__ == '__main__':
	path = r"/Users/liyazhou/Repo/self-repo/python-practice/python_base/lang"
	batch_rename_image(path)

	# path = r"F:\Graduate\MobilePhone\BGimages"
	# batch_rename_image(path)

    # path = 'D:\\BaiduYunDownload\\Hadoop\\尚学堂Hadoop\\video'
    # batch_rename(path)

    # path02 = 'D:\\BaiduYunDownload\\Hadoop\\全套Hadoop从入门到企业项目开发课程_云帆大数据学院'
    # batch_rename_foldername(path02)
