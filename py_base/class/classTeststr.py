class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id + self.name

if __name__ == '__main__':
    user = User('10001','zhouzhou')
    print(user)
