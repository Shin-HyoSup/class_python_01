'''
    다른 디렉토리에 있는 파일을 import 해보자...
    - sys.. 란?
    sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. 
    이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.
'''
import sys
print(sys.path)

# import _module2 # Error : ModuleNotFoundError: No module named '_module2'

# sys path 에 본인 경로를 추가한다...
sys.path.append("C:\\DreamHyo\\_KorIT")

import _module2
print(_module2.add2(11,22))
print(_module2.PI2)