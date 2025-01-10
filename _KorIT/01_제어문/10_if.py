'''
ㄱ. if 문 기본구조

if 조건문:
    True 문장1  
    True 문장2  
    ...  
else:
    False 문장1  
    False 문장2  
    ...
'''
var_bool = False

if var_bool:
    print('aaaaa')
    #    print('b') -> Error : indentation -> 들여쓰기
print('ccccc')
    #print('c') -> Error
    
'''
ㄴ. 연산자
1. 비교 연산자  
- <, >, <=, >=, ==, !=  
2. 논리 연산자  
- and, or, not  
3. in, not in  
'''
var_bool = True
if var_bool:
    print('01.',True)

if 'a' in 'abc':
    print('02.',True)

# if 'a' not in ['abc','b','c']:
# if 'a' in ['abc','b','c']:
if 'a' in ['abc','b','c']:
    print('03.',True)
else:
    print('03.',False)

# if 1==1: pass <- 한줄로
if 1==1:
    pass
else:
    print('04.',False)
    
# ㄷ. if 조건문1: ... elif 조건문2: ... else: 조건문3...
jumsu = 89

if jumsu >= 90:
    print('01.','A')
else:
    if jumsu >= 80:
        print('02.', 'B')
    else:
        if jumsu >= 70:
            print('03.', 'C')
        else:
            if jumsu >= 60:
                print('04.', 'D')

if jumsu >= 90:
    print('01.','A')
elif jumsu >= 80:
    print('02.', 'B')
elif jumsu >= 70:
    print('03.', 'C')
elif jumsu >= 60:
    print('04.', 'D')
    
var_a = True if jumsu > 80 else False
print('var_a', var_a)