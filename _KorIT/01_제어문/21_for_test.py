'''
    1) var_list = [0,1,2,3,4,5,6,7,8,9]
    1. 짝수만 출력..
    2. 홀수만 출력..
'''
var_list = [0,1,2,3,4,5,6,7,8,9]
for i in var_list:
    if i % 2 == 0:
        print(i)

print('*'*50)
'''
    2) 구구단을 출력
    2 * 1 = 2
    2 * 2 = 4
    ...
    3 * 1 = 3
    3 * 2 = 3
    ...
'''
for i in range(2,4):
    for j in range(1,10):
        print(str(i) + '*' + str(j) + '=' + str(i*j))
        #print(f"{i} * {j} = {i*j}")
        #print("{0} * {1} = {2}".format(i, j, i*j))
        #print("{num1} * {num2} = {num3}".format(num1=i, num2=j, num3=i*j))
        
'''
    1) 번을 리스트 컴프리헨션으로..
'''
var_a = [1,2,3,4]
var_b = [num * 3 for num in var_a]
print(var_b)
var_list_2 = [num for num in var_a if num % 2 == 0]
print(var_list_2)