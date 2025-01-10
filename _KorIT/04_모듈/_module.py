'''
    * module
    - 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
    
    1. step 1...
    - def add , sub 정의
    2. step 2...
    - print 추가
    - if __name__=="__main__":
    3 __name__ 변수란..
    - 직접 실행할 경우에는 __name__ 변수에 "__main__" 값이 저장된다.
      __name__ = "__main__"
    - 다른 모듈에서 import 할 경우에는 __name__ 변수에 모듈명(파일이름)이 저장된다.
      __name__ = "_module"
'''

def add(first, second):
    return first + second

def sub(first, second):
    return first - second

if __name__=="__main__":
    print(add(100, 200))
    print(sub(100, 200))

# 상수    
PI = 3.14
# 클래스
class FourCalc():
    def class_add(self, first, second):
        return first + second