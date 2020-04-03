class Student(object):
    def __init__(self):
        pass
    
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if not isinstance(score, int):
            raise ValueError('parameter must be a int number')
        if score > 100 or score < 0:
            raise ValueError('parameter must in 1~100')
        self._score = score

        
