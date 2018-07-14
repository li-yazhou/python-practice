class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]  # 列表推导式
        self.count = {}.fromkeys(range(len(self.values)), 0) # 下标作为关键字的字典

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]
