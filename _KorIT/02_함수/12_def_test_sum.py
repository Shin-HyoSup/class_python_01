'''
    - 숫자 범위의 합계를 계산하는 함수
    
    학습 포인트:

    함수 매개변수 사용
    반복문 (for, while) 활용
    조건문 활용 (입력 값 검증, 특정 조건의 숫자만 계산)
    변수 활용 (합계 누적)
    return 문의 이해

    학생들에게 추가로 제시할 수 있는 과제:

    입력받은 범위 내의 모든 숫자 곱하기
    특정 숫자의 배수의 합 구하기 (사용자가 배수를 지정)
    홀수의 합과 짝수의 합을 따로 구하기
'''
# 기본 for문
def sum_range(start, end):
    # 시작 값이 끝 값보다 큰 경우 처리
    if start > end:
        print("시작 값이 끝 값보다 클 수 없습니다!")
        return None # = return, pass : 동일하게 None 를 return
    
    total = 0
    for num in range(start, end + 1):   # end + 1을 해야 end까지 포함됨
        total += num
    return total

# 사용 예시
result = sum_range(15, 10)  # 1부터 10까지의 합: 55
print(result)

# while 문으로
def sum_range_while(start, end):
    total = 0
    current = start
    while current <= end:
        total += current
        current += 1
    return total

# 사용 예시
result = sum_range_while(1, 10)  # 55
print(result)

# 추가 문제
# 짝수의 합만 구하기
def sum_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:    # 짝수인 경우만
            total += num
    return total

# 3의 배수만 더하기
def sum_multiples_of_three(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 3 == 0:    # 3의 배수인 경우만
            total += num
    return total

def new_func():
    print('a')
    print('a')
new_func()