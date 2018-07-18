
class Car:  #类默认继承于object，等价于class Car(object):
    def info(self):
        print("i am a new car...")

class Student1:  #类默认继承于object，等价于class Car(object):
    def show(self):
        print("I am a student...")

class Person1:
    count = 0
    """构造方法"""
    def __init__(self,name='周周',age=22,gender='male'):
        Person.count += 1
        self.__ID = Person.count 
        self.__name = name
        self.__age = age
        self.__gender = gender
        

    """展示个人信息"""
    def tostring(self):
        info = 'ID是' + str(self.__ID) + '\n' + \
               'name是' + self.__name + '\n' + \
               'age是' + str(self.__age) + '\n' + \
               'gender是' + self.__gender
        return info


class TestAttr:
    def __init__(self,ID):
        self.__ID = ID

    @property
    def ID(self): #只读，无法修改__ID属性值
        return self.__ID

    def __get(self):    #是私有的getter方法
        return self.__ID

    def __set(self,id):
        self.__ID = id

    def __del(self):
        del self.__ID

    ID = property(__get,__set,__del)  #该“只读属性”既可以读取也可以修改，但不可以删除

class Person(object):
    def __init__(self, name = '', age = 22, gender = 'male'):
        self.setName(name)
        self.setAge(age)
        self.setGender(gender)

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setGender(self, gender):
        self.__gender = gender

    def tostring(self):
        info = '姓名是：' + self.__name + '\n' + \
               '年龄是：' + str(self.__age) + '\n' + \
               '性别是：' + self.__gender
        print(info)

        
class Student(Person): #继承Person类
    def __init__(self, name = '', age = 22, gender = 'male', department = 'sesc'):
        #使用super()调用父类的构造方法，来初始化成员变量
        super(Student, self).__init__(name, age, gender)
        #Person.__init__(self,name,age,gender)
        self.setDepartment(department)

    def setDepartment(self, department):
        self.__department = department

    def tostring(self): #覆盖父类的tostring方法
        super(Student,self).tostring()
        print('学院是：'+self.__department)

if __name__ == '__main__':
    """测试父类Person"""
    per = Person('小周')
    per.tostring()

    print('---------------------------')
    """"测试子类Student"""
    stu = Student("周周同学")
    stu.tostring()
        
