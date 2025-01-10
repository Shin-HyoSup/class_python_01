'''
    4칙연산을 하는 class 를 만들어보자.

class FourCal():
    pass

cal = FourCal()
print(type(cal))

# cal.setdata(2,4)
# cal.add() -addition
# cal.mul() -multiplication
# cal.sub() -subtraction
# cal.div() -division
'''
class FourCal():
    # pass
    # step 1. 메서드(method)
    def setdata(self, first, second):
        self.first = first
        self.second = second
    # step 1-1. skip 가능
    def __str__(self):
        return 'first='+str(self.first)+', second='+str(self.second)
    # step 2..
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# step 1.    
# self 는 class 객체가 self 로 넘어온다
# cal.setdata(2,4)
# def setdata(self=cal,first=2,second=4)

# 1. cal.setdata('10','20')
# 2. cal.first = '10'
#    cal.second = '20' 이라는 변수가 생성 -> 객체변수 or '속성'!
cal = FourCal()
cal.setdata(10,20) # 잘 안쓰지만.. FourCal.setdata(cal, '10', '20') 도 가능
print(cal.first)
print(cal.second)

# step 1-1.
# print(cal.__str__())

a = FourCal()
a.setdata(2,5)
b = FourCal()
b.setdata(20,50)

print(a.first, id(a.first))
print(b.first, id(b.first))
# a 의 first 와 b 의 first 다른 공간에 저장된다.

# step 2..
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())