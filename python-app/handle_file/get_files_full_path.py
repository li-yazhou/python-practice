
import os

def get_files_full_path(path):
    full_path = []
    for filename in os.listdir(path):
    	file_full_path = os.path.join(path,filename)
    	full_path.append(file_full_path)
    retval = ";".join(full_path)
    return retval
  

def get_files_path(path):
    full_path = []
    for filename in os.listdir(path):
        dest_path = "%AXIS_HOME%\\WEB-INF\\lib\\" + str(filename)
        full_path.append(dest_path)
    retval = ";".join(full_path)
    return retval


if __name__ == '__main__':
    # path = r"E:\tomcat7\lib"
    # retval = get_files_full_path(path)
    path = r"E:\tomcat7\webapps\axis\WEB-INF\lib"
    path01 = r"D:\Program Files\apache-tomcat-7.0.68\lib"
    retval = get_files_path(path01)
    print(retval)

