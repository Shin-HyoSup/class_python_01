'''
    1. 오류 피하기
    try:
        ...
    except:
        pass
'''
try:
    f = open('error00.txt','r')
except FileNotFoundError:
    pass

print('file found')
'''
    2. 오류 발생하기
    - raise
'''
class MyFamily:
    def my_name(self):
        raise NotImplementedError
# NotImplementedError는 파이썬에 이미 정의되어 있는 오류로, 
# 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 발생시키기 위해 사용한다.

# 2-1
class FamilyInfo(MyFamily):
    pass

# my_family = FamilyInfo()
# my_family.my_name() # NotImplementedError 발생

# 2-2
class FamilyInfo2(MyFamily):
    def my_name(self):
        print("my name is shs")
        
my_family2 = FamilyInfo2()
my_family2.my_name()