'''
    1) input 사용해서 연산 해보기(계산기)
    - 연산자 정보를 받고(1,2,4 가 아니면 다시 입력)
    - 숫자를 받아서 계산
'''    
number = 0
prompt = '''
1. +
2. -
4. Quit
'''
result_num = 0
while number != 4:
    print(prompt)
    calc = int(input('연산 기준을 선택주세요 : '))
    if calc in [1,2,4]:
        pass
    else:
        continue
    
    if calc == 4: break
    
    number = int(input('숫자를 입력해주세요 : '))
    if calc == 1:
        result_num = result_num + number
    elif calc == 2:
        result_num = result_num - number
    print('result_num:',result_num)

'''
    2) 메일 항목 조회
    - 결과물
    Name : BTS, Subject : helo~, Date : 2025-01-11
    Name : newjins, Subject : hello~, Date : 2025-01-10
    Name : hani, Subject : hello~, Date : 2025-01-09
    Name : iu, Subject : hello~, Date : 2025-01-08
'''    
var_mail_list=[
    ['BTS','helo~','2025-01-11'],
    ['newjins','hello~','2025-01-10'],
    ['hani','hello~','2025-01-09'],
    ['iu','hello~','2025-01-08'],
]
loop_count = len(var_mail_list)
i = 0
while loop_count > 0:
    var_list = var_mail_list[i]
    print('Name : {0}, Subject : {1}, Date : {2}'.format(var_list[0], var_list[1], var_list[2]))
    loop_count = loop_count - 1
    i = i + 1 
    
