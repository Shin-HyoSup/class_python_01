'''
    1) 함수란...
        - 입력값(인수,파라미터,매개변수)을 가지고 어떤일을 처리한 후에 리턴값(결과값,출력값)을 내놓는것(return)
    2) 사용하는 이유
        - 반복되는 코딩을 줄이기 위해서
        - 보기 좋게.. 가독성
    3) 기본구조
    def 함수_이름(매개변수):
        실행할_문장1
        실행할_문장2
        ...
    4)
    입력값 -> 함수(def) -> 리턴값
    - 입력값이 없는 함수 : OK
    - 리턴값이 없는 함수 : OK
'''
def add(a,b):
    return a+b
var_def = add(1,2)
print(var_def)
var_def = add(1,3)
print(var_def)
var_def = add(1,4)
print(var_def)
var_def = add(1,5)

def add_print(a,b):
    print('a+b:', a+b)
add_print(1,2)
add_print(2,3)

def say_hello():
    print('Hello~')
say_hello()

def sub(a,b):
    print('a-b:', a-b)
sub(b=1,a=10)
sub(10,1)
'''
    ㄱ) print() 도 함수다..
        - help(print)
        
'''
help(print)
'''
    ㄴ) about 함수
        - 빠져나올때는 return
'''
def nick_name(name):
    if name=='idot':
        return
    else:
        print('hello~ ', name)

nick_name('angel')
nick_name('idot')
'''
     ㄷ) 기본값 설정     
        - 기본값은 항상 뒤에.. 중간에 있으면 매칭이 불명확하다
'''
def nick_name(name, say_hello = 'how are you? :)'):
    if name=='idot':
        return
    else:
        print('hello~ ', name)
        print(say_hello)

nick_name('angel')
nick_name('angel', 'nice to see you')
'''
     ㄹ) 변수의 범위
'''
print('*'*30,'variable','*'*30)
a = 1
def add_a(a):
    a = a+10
add_a(a)
print(a) # 1

# def add_a(a):
#     a = a+10
# add_a(3)
# print(a) <- a 변수 선언이 없으므로 error

def add_a(a):
    a = a+100
    return a
add_b = add_a(0)
print('add_b :',add_b)

b = 0
def var_b():
    global b
    b = b+100
    
var_b()
print('global_b :',b)

'''
    ㅁ) 여러겨의 입력값을 받는 함수(입력값이 다양할 경우...)
    def 함수_이름(*입력값):
        실행할_문장1
        실행할_문장2
        ...
'''
def add_manay(*args): # arguments (tuple 로 처리된다)
    result = 0
    for i in args:
        result = result + i
    return result

var_result = add_manay(1,2,3)
print(var_result)
var_result = add_manay(1,2,3,4,5,6,7,8,9)
print(var_result)

def add_manay_result(result_text,*args): # arguments (tuple 로 처리된다)
    result = 0
    for i in args:
        result = result + i
    return result_text + str(result)

var_result = add_manay_result('result is ...', 1,2,3)
print(var_result)
var_result = add_manay_result('result is ...', 1,2,3,4,5,6,7,8,9)
print(var_result)
'''
    ㅂ) 키워드 매개변수(**kwargs) <= 딕셔너리
    def 함수_이름(**입력값):
        실행할_문장1
        실행할_문장2
        ...
'''
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='shs',age=29)
'''
    ㅅ) lambda(람다) 예약어
    함수_이름 = lambda 입력값1, 입력값2, ...: 실행할_문장
'''
add_1 = lambda a, b: a+b

def add_2(a,b):
    return a+b

var_add_1 = add_1(1,2)
print(var_add_1)

var_add_2 = add_2(1,2)
print(var_add_2)