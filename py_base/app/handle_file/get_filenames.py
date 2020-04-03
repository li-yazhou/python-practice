
import os

def get_filenames(path):
    simple_names = []
    names = []
    suffixs = ["pdf", "caj"]
    for filename in os.listdir(path):
        # include subfolders and subfiles, filter subfolders
        if not os.path.isfile(os.path.join(path,filename)):
            continue
        # print(filename)
    	# if filename.find('.') > 0:
        # if filename.endswith(".pdf") or filename.endswith(".caj"):
        # suffix = filename[-3:]
        suffix = filename[filename.find('.')+1:]
        if suffix in suffixs:
    	    simple_names.append(filename[filename.rfind("_")+1 : -4])
    	    names.append(filename)
    return simple_names + names
  
def save_filenams(distpath,names):
    with open(distpath,'w') as distfile:
        for name in names:
            distfile.write(name + "\n")
  	    
if __name__ == '__main__':
    path = r"F:\Paper_160621\20160701_道路行程时间预测"
    distpath = r"F:\Paper_160621\20160701_道路行程时间预测\filenames.txt"
    names = get_filenames(path)
    save_filenams(distpath, names)
    for filename in names:
        print(filename)

