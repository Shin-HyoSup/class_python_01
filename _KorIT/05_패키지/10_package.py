'''
    1. package
    - 모듈의 집합(파이썬에서 모듈은 하나의 .py 파일이다.)
    2. __init__.py 의 용도
    - __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려 주는 역할을 한다. 
    - python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420). 
      하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.
    
    * __pycache__ 폴더
    - 처음 import 하면 자동 생성됨(python 3.2 부터)
    - py 파일을 컴파일한 결과 파일 pyc
    - 다음 실행시 변경된 사항이 없으면 compile 하지 않고 pyc 파일을 사용
      (컴파일을 하지 않으므로 로딩 시간을 단축)
      
    3. __all__
'''
# ===============================================
# 1. package
# ===============================================
import sys
# print(sys.path)
sys.path.append('C:\\DreamHyo\\_KorIT')

""" # import 하는 방법 1
import game.sound.echo
game.sound.echo.echo_test()

# import 하는 방법 2
from game.sound import echo
echo.echo_test()

# import 하는 방법 3
from game.sound.echo import echo_test
echo_test() 

# 아래처럼 import 하면 오류 발생(__init__.py 가 빈파일일 경우)
import game
game.sound.echo.echo_test() # Error : AttributeError: module 'game' has no attribute 'sound'
# import game을 수행하면 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.

# import game.sound.echo.echo_test # import 의 마지막 항목은 모듈 or 패키지이어야 함.. 함수 X 
"""
# ===============================================
# 2. __init__.py 의 용도
# - __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
# ===============================================
import game
# 2-1.
print(game.VERSION)
game.print_version_info()
# 2-2.
game.render_test() 

# ===============================================
# 3. __all__ : import *
# - __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
# ===============================================
from game.sound import *

# echo.echo_test() #Error : NameError: name 'echo' is not defined
# -> sound/__init__.py 에 __all__ 로 지정해주면 오류 안남

echo.echo_test()
melody.melody_test()

from game.graphic import *
render.render_test()
render.render_echo_test()