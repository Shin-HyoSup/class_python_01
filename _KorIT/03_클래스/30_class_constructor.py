'''
    1. 생성자(constructor)
    파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 된다.
'''
class FourCal():
    # step 2..
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
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
# step 1...
# 생성자 없이 호출하면 add 에서 오류가 발생
# cal1 = FourCal()
# cal1.add()

# step 2...
# 생성자를 생성하고 호출하면 오류 발생
# cal1 = FourCal()

# step 3...
cal1 = FourCal(4,2)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
