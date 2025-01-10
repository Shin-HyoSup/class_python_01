'''
    1. Error 예제
'''
# print(4/0) # Error -> ZeroDivisionError: division by zero

#var_list = [1,2,3]
#print(var_list[3]) # Error -> IndexError: list index out of range

#f = open('error.txt', 'r') # Error -> FileNotFoundError: [Errno 2] No such file or directory: 'error.txt'

'''
    2. try-except 문
    ex 1) 기본 구문
    try:
        ...
    except [발생오류 [as 발생변수]]: # [] 구문은 생략가능
        ...
        
    try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 
    하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.
'''
try:
    4/0
except ZeroDivisionError as e: #  오류 변수 e
    print(e)
print('1','=' * 50)    
exit()
'''
    ex 2) finally 처리
    try:
        ...
    except [발생오류 [as 발생변수]]: # [] 구문은 생략가능
        ...
        
    finally: # 항상 실행
        ...
'''
try:
    f = open('./error.txt', 'w')
    4/0
except Exception as e:
    print(e)
    print('exception')
finally:
    f.close()
    print('file close')
print('2','=' * 50)      
'''
    ex 3) 여러 개의 오류 처리
    try:
        ...
    except [발생오류1 [as 발생변수1]]: # [] 구문은 생략가능
        ...
    except [발생오류2 [as 발생변수2]]: # [] 구문은 생략가능
        ...
'''
try:
    a = [1,2,3]
    #print(a[3])
    4/0
except ZeroDivisionError as e:
    print('Division Error')
    print(e)
except IndexError as e:        
    print('indexing Error')
    print(e)
    
try:
    a = [1,2,3]
    #print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
print('3','=' * 50)  
'''
    ex 4) 여러 개의 오류 처리
    try:
        ...
    except [발생오류 [as 발생변수]]: # [] 구문은 생략가능
        ...
    else: # 오류가 없을때 수행
        ...
''' 
# 1
try:
    age=int(input('what is your age?'))
except Exception as e:
    print(e)
    print('입력값이 정확하지 않습니다.')
    # exit() 실행 중단 or import sys; sys.exit()
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")    
# 2. 1번을 else 없는 if 문으로..    
try:
    age=int(input('what is your age?'))
except Exception as e:
    print(e)
    print('입력값이 정확하지 않습니다.')
    exit()

if age <= 18:
    print("미성년자는 출입금지입니다.")
else:
    print("환영합니다.")  