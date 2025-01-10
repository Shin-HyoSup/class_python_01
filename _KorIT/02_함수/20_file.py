'''
    1) 파일 읽고 쓰기
        - 파일_객체 = open(파일_이름,파일_열기_모드)
        - 파일_열기_모드
        r : 읽기모드
        w : 쓰기모드(해당 파일이  존재할 경우 원래 있던 내용이 모두 사라지고, 
                    해당 파일이 존재하지 않으면 새로운 파일이 생성)
        a : 추가모드(마지막라인에 추가)
'''
file_url = "C:\\DreamHyo\\_KorIT\\새파일.txt"
# 1. 파일 열기, 만들기
f = open(file_url,'w')  #command 창의 현재 디렉토리에 파일 생성
f.close()

# f = open('c:/test.txt','w')
# f = open('c:\\test2.txt','w') # c:\newfile.txt 하면 \n 때문에 오류

# 파일쓰기
f = open(file_url, 'w')
for i in range(1, 11):
    data = "%d st line.\n" % i
    f.write(data)
f.close()

# 파일읽기 : 첫줄
f = open(file_url, 'r')
line = f.readline()
print(line)
f.close()

# 전체 읽기
f = open(file_url, 'r')
var_cnt = 0
while True:
    var_cnt += 1
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()
print(var_cnt)

# 전체읽기 readlines()
f = open(file_url, 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # strip : \n 제거..
    print(line)
f.close()

# 전체읽기 read()
print('='*50)
f = open(file_url, 'r')
data = f.read()
print(data)
f.close()

# 전체읽기 : 파일객체를 for 문과 같이 사용
f = open(file_url, 'r')
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가 open(file_url,'a')
f = open(file_url,'a')
for i in range(11, 20):
    data = "%d  st line.\n" % i
    f.write(data)
f.close()

# open, write, close 를 같이 해줌 -> with
f = open(file_url, 'a')
f.write('life is short\n')
f.close()

with open(file_url,'a') as f:
    f.write('you need python')