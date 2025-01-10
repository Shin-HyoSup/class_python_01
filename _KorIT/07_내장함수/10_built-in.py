# 1. abs() : 절대값
print(abs(3)) # 3
print(abs(-3)) # 3
print('1.','='*50)

# 2. all(x) : [and] 반복 가능한 데이터 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False
# - 반복 가능한 데이터란 for 문에서 사용할 수 있는 자료형을 의미한다. 
# - 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
print(all([1,2,3])) # True
print(all([1,2,3,0])) # False
print(all([])) # True, false 인 인수를 찾을수 없다..
print(all([[]])) # False, [] = false

a = []
if a:
    print(True)
else:
    print(False)
# -> False 임

def my_all(args):
    for arg in args:
        if not arg:
            return False
    return True
print('2.','='*50)

# 3. any(X) : [or] all 의 반대. 하나라도 참이면 True
print(any([1,2,3,0])) # True
print(any([0, '', [], (), {}])) # False

print('3.','='*50)
# 4. dir() : 객체가 지닌 변수나 함수를 보여 주는 함수
# 리스트의 함수
print(dir([1,2]))
# 딕셔너리의 함수
print(dir({'name':'shs'}))

print('4.','='*50)
# 5. eval(express) : 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수
print(eval('1+2')) # 3
print(eval("'1'+'2'")) # 12

print('5.','='*50)
# 6. filter(함수, 반복가능한 데이터(리스트,딕셔너리 등))
# 리스트를 입력값으로 넘겨서 리스트로 결과값을 받아옴
def positive_list(var_list):
    result=[]
    for i in var_list:
        if i > 0:
            result.append(i)
    return result
print(positive_list([1,2,-4,-1,0]))
# filter 를 사용하면
def positive(x):
    return x > 0
print(list(filter(positive, [1,2,-4,-1,0])))
# lambda 함수로 변경하면? 람다는 패쓰 ㅋㅋ
print(list(filter(lambda x : x > 0, [1,2,-4,-1,0])))

# 7. id(object) : 객쳉의 고유 주소값을 리턴
a = 10; b=20
print(id(a), id(b))

# 8. input([prompt])
# a = input('your name?')
# print('Your name is',a)

# 9. int() : 문자나 실수를 정수로 리턴
print(int(1.2))

# 10. str(): 숫자형을 문자열로 리턴
print('1'+str(2))

# 11. list
a = list('python')
print('a',type(a),a)
b = list((1,2,3))
print('b',b)

# 11. tuple
a = tuple('python')
print('a',type(a),a)
b = tuple([1,2,3])
print('b',b)

# 12. max(iterable)
print(max([1,20,3]))
print(max([(1,2),(20,3),(3,40)]))

# 13. min(iterable)
print(min([1,20,3]))
print(min([(1,2),(20,-3),(3,40)]))

# 14. open(파일명, 'w') : 'w':쓰기모드, 'r':읽기모드, 'a':추가모드
f = open("open_file.txt", 'w')