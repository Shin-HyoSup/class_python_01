'''
ㄱ. for 문의 기본구조

for 변수 in 리스트(or 튜플,문자열):
    실행할_문장1
    실행할_문장2
    ...
'''
# 기본 for문
var_list = [1,2,3]
for i in var_list:
    print(i)
    
print('='*10, 'tuple', '='*10)   
# tuple 인경우
var_tuple = [(1,'one'),(2,'two'),(3,'three')]
for (num,num_str) in var_tuple:
    print(num, num_str)
    
# for + if 문.. 점수 받아서 학점 출력
my_grade = [90, 50, 78, 95]
for i in my_grade:
    if i >= 90:
        print('grade is A')
    elif i >= 80:
        print('grade is B')
    elif i >= 70:
        print('grade is C')
    else:
        print('grade is F')
        
# grade 에 순서 넣어주기
number = 0
for i in my_grade:
    number=number+1
    if i >= 90:
        print(str(number) + 'st grade is A')
    elif i >= 80:
        print(str(number) + 'st grade is B')
    elif i >= 70:
        print(str(number) + 'st grade is C')
    else:
        print(str(number) + 'st grade is F')
        
print('='*10, 'continue', '='*10)        
# continue 문
# 70점 이상만 출력력
# my_grade = [90, 50, 78, 95]
for i in my_grade:
    if i >=70:
        print('over 70:',str(i))
    else:
        continue
    print('order is',str(i))
    
print('='*10, 'range', '='*10)
var_range = range(5)
print(var_range)
for i in var_range:
    print(i)

add = 0    
for i in range(1,11):
    add = add+i
print(add)

print('='*10, '중복 for문', '='*10)  
# kr : first, kr : second, kr : third
var_code = ['kr','en','ja']
var_nation = ['first', 'second', 'third']

for i in var_code:
    for j in var_nation:
        print(i + ':' + j)