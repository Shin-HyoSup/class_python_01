'''
    1. class 상속(Inheritance)
    - 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다. 
    ‘클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?’라는 
    의문이 들 수도 있다. 
    하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다
    2. 강의 순서
    - 기존 FourCal() 복사
    - 상속개념 이해 
      class MoreFourCal(FourCal):
        pass
      -> FourCal 과 동일하게 사용할 수 있다.
      -> calc_more 함수 추가
    - overriding 개념이해
      0으로 나눌시 발생하는 오류 개선..
      동일한 함수를 정의하면 overriding 된 함수를 사용한다.      
'''
class FourCal():
    # pass
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
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

# step 1... 상속 개념이해 
class MoreFourCal(FourCal):
    def calc_more(self):
        return self.first + self.second * 10
    # step 2... overriding
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(10,20)
print(a.add())
print(a.calc_more())

# step 2... overriding
b = MoreFourCal(10,2)
print(b.add())
#print(b.div()) # Error : ZeroDivisionError: division by zero
print(b.div())

'''
    2. class 변수
    - class 내에 선언된 변수는 모든 객체에 동일한 값은 리턴해준다
    - 클래스 변수 변경시 모두 변경됨
    - 객체에서 변경되면 해당 객체로 변수가 새롭게 생성된다. 클래스 변수는 변함없음
'''
class Family:
    lastname = 'lee'
    
print(Family.lastname)
a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = 'choi'
print(a.lastname)
print(b.lastname)

a.lastname = 'park'
print(a.lastname)
print(Family.lastname)
print(b.lastname)