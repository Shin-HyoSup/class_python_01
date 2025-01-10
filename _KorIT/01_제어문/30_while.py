'''
    ㄱ) while 문의 기본구조
    While 조건문:
        실행할_문장1
        실행할_문장2
        실행할_문장3
        ...
'''
loop_cont = 0
while loop_cont < 10:
    print(loop_cont)
    loop_cont = loop_cont+1 #loop_cont += 1

'''
    ㄴ) input 사용해서 +,- 해보기
'''    
number = 0
prompt = '''
1. +10
2. -10
4. Quit
'''
result_num = 0
while number != 4:
    print(prompt)
    number = int(input('번호를 눌러주세요 : '))
    if number == 1:
        result_num = result_num + 10
    elif number == 2:
        result_num = result_num - 10
print('result_num:',result_num)

'''
    ㄷ) break 문으로 빠져나오기
'''   
print('='*30,'break','='*30)
loop_bool = True 
loop_count = 5
while loop_bool:
    loop_count = loop_count - 1
    print(loop_count)
    if loop_count == 0:
        break
print('end')

'''
    ㄹ) continue 
'''   
print('='*30,'continue','='*30)

a = 0
while a < 10:
    #a += 1 => 무한루프 빠져나가기 : [ctrl+C]
    if a % 2 == 1:
        continue
    print(a)