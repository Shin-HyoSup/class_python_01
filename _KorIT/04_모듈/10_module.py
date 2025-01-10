'''
    1. import module
    - import 모듈_이름
    - from 모듈_이름 import 모듈_함수
    
    2. _module.py 에 print 문 추가하면
        import 할때 _module.py 의 print 문이 출력된다.
        _module.py 에 if __name__ == "__main__": 함수 추가
        
'''
import _module # 같은 폴더에 있는 _module.py 파일 import
print(_module.__name__) # _module(모듈명 = 파일명)
print(_module.add(3,4))

from _module import add, sub
# = from _module import *
print(add(10,20))

# 상수 import
print(_module.PI)

# class import
a = _module.FourCalc()
print(a.class_add(10, 222))

# 다른 디렉토리에 있는 파일을 import 하면??
#import _module2 # Error : ModuleNotFoundError: No module named '_module2'
# go -> 20_other_dir_module.py
