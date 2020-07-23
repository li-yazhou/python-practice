
def test01():
    str_content = "partition:0,offset:47256,key:null,value:{name:zz, age:22"
    idx = str_content.index("{")
    print(idx)
    print(str_content[idx:])


if __name__ == '__main__':
    test01()