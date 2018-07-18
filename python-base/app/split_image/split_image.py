import __future__
import os
from PIL import Image

def splitimage(src, rownum, colnum, distpath):
    img = Image.open(src)
    width, height = img.size
    if rownum <= height and colnum <= width:
        print('Original image info: %sx%s, %s, %s' % (width, height, img.format, img.mode))
        print('begin')

        filename = os.path.split(src)[1]
        parts = filename.split('.')
        basename, ext = parts[0], parts[-1]

        rowheight = height // rownum
        colwidth = width // colnum
        num = 0
        for row in range(rownum):
            for col in range(colnum):
                box = (col * colwidth, row * rowheight, (col + 1) * colwidth, (row + 1) * rowheight)
                img.crop(box).save(os.path.join(distpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1
        print('finished, %s small images.' % num)
    else:
        print('number is invalid!')

if __name__ == '__main__':
    path = r'E:\Code\PyCode\Python3x\image\distpath06-拉链'
    srcpath = os.path.join(path, "拉链.jpeg")
    distpath = path
    splitimage(srcpath, 3, 3,distpath)


