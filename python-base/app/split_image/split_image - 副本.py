import __future__
import os
from PIL import Image


def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('begin')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]  //文件所在目录
        fn = s[1].split('.')
        basename = fn[0]  //文件名
        ext = fn[-1]      //后缀

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                # ext是文件的后缀，也是文件类型
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('finished, %s small images.' % num)
    else:
        print('number is invalid!')

# src = input('请输入图片文件路径：')
# if os.path.isfile(src):
#     dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
#     if (dstpath == '') or os.path.exists(dstpath):
#         row = int(input('请输入切割行数：'))
#         col = int(input('请输入切割列数：'))
#         if row > 0 and col > 0:
#             splitimage(src, row, col, dstpath)
#         else:
#             print('无效的行列切割参数！')
#     else:
#         print('图片输出目录 %s 不存在！' % dstpath)
# else:
#     print('图片文件 %s 不存在！' % src)

if __name__ == '__main__':
    srcpath = r"E:\Codes\PyCodes\Python3x\image\square.JPEG"
    distpath = r"E:\Codes\PyCodes\Python3x\image\distpath04"
    splitimage(srcpath,3,3,distpath);    