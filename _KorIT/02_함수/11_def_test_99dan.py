'''
    1) 구구단을 함수로 이용해서 만들어보자
    def gugu_dan(num)
        ...
    gugu_dan(2)
    gugu_dan(3)
    gugu_dan(4)
    
    2) 위에 만든 구구단을 for 문이나 while 문으로 한번에 실행
    for i in ...
        gugu_dan(i)
    
    var_i = ...    
    while loop_cnt ....
        gugu_dan(loop_cnt)
        gugu_dan(var_i)
'''
# 구구단 함수 예 for 문
def print_multiplication_table(start, end):
    for n in range(start, end + 1):
        print(f"== {n}단 ==")
        for i in range(1, 10):
            print(f"{n} x {i} = {n * i}")
        print()  # 단 사이 빈 줄 출력

# 사용 예시
print_multiplication_table(2, 4)  # 2단부터 4단까지 출력

# 2단에서 9단까지 출력
def print_all_multiplication_for():
    for n in range(2, 10):       # 2부터 9까지 반복
        print(f"== {n}단 ==")
        for i in range(1, 10):   # 1부터 9까지 곱하기
            print(f"{n} x {i} = {n * i}")
        print()  # 단 사이 빈 줄 출력

# 사용 예시
print_all_multiplication_for()

# while 문으로..
def print_all_multiplication_while():
    n = 2    # 시작 단수
    while n <= 9:    # 9단까지 반복
        print(f"== {n}단 ==")
        
        i = 1    # 각 단의 시작 수
        while i <= 9:    # 9까지 곱하기
            print(f"{n} x {i} = {n * i}")
            i += 1    # 곱하는 수 증가
            
        print()    # 단 사이 빈 줄 출력
        n += 1    # 다음 단으로 넘어가기

# 사용 예시
print_all_multiplication_while()