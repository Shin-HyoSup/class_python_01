'''
    1. class 란?
    - 함수의 상위버젼 느낌?
    - 계산기를 예로 들어서 설명...
    - 계산기는 항상 이전에 대한 결과값을 가지고 있다.
    
    2. 객체와 인스턴스의 차이
    - 클래스로 만든 객체를 ‘인스턴스’라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까? 
      이렇게 생각해 보자. 
      a = Cookie()로 만든 a는 객체이다. 
      그리고 a 객체는 Cookie의 인스턴스이다. 
      즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. 
      ‘a는 인스턴스’보다 ‘a는 객체’라는 표현이 어울리며 
      ‘a는 Cookie의 객체’보다 ‘a는 Cookie의 인스턴스’라는 표현이 훨씬 잘 어울린다.
'''
# calculator
# 클래스 개념을 계산기로 설명
# - 100개의 계산기를 함수로 만들려면 100개의 함수가 필요..
# - 클래스를 사용하면 하나의 클래스를 만들고 100개의 객체를 만들면 됨
# - 함수로 누적된 계산을 실행할려면 global 변수가 필요함
result = 0
#print('1.',id(result))
def add(num):
    #global result => global 키워드의 이해
    global result
    #result = 0
    result += num
    print('2.',id(result))
    return result

print(add(10))
print(add(50))
print('='*50)

# 2개의 계산기가 필요하면?
result1 = 0
result2 = 0

def add1(num):
    #global result => global 키워드의 이해
    global result1
    result1 += num
    return result1

def add2(num):
    #global result => global 키워드의 이해
    global result2
    result2 += num
    return result2

print(add1(10))
print(add1(50))

print(add2(100))
print(add2(500))
print('='*50)
# class 를 사용하면?
# Calculater 라는 과자틀을 만들고 동일한 과자를 무한대로 찍어낼수 있다.
# - 과자틀 -> 클래스
# - 과자 -> 객체
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    # subtraction(빼기)
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(10))
print(cal1.add(50))
print(cal2.add(100))
print(cal2.add(500))