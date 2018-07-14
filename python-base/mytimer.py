import time as t

class Mytimer(object):
    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        # 当Mytimer对象调用了start()后直接输入或者打印对象
        self.prompt = '提示：请先调用stop()停止计时'
        print('开始计时....')


    def stop(self):
        if not self.begin:
            self.prompt = '提示：请先调用start()停止计时！'
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束！')


    # 内部方法
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了 '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + str(self.unit[index]))

    # 覆写__add__()函数
    def __add__(self, other):
        prompt = '总共运行时间是：'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + str(self.unit[index]))
        return prompt
            




















            
