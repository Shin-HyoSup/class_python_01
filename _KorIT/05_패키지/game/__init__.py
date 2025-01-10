#   ==================================
#   2.about __init__.py
#   ==================================
from .graphic.render import render_test #.graphic 은 현재 폴더를 의미함.
from .sound.echo import echo_test

VERSION = 10.0

def print_version_info():
    print(f"The version of this game is {VERSION}.")
    
# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game :) ...")