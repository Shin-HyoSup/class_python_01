'''
    본인 폴더에 my_family.txt 파일을 생성하고,
    한줄씩 가족 소개를 넣는다..
    이름,관계,나이,직업,가족소개
'''
father = {
        'name':'father_name',
        'relatioin':'father',
        'age':50,
        'job':'gage',
        'desc':'i love you~ father',
    }
mother = {
    'name':'mother_name',
    'relatioin':'mother',
    'age':46,
    'job':'house',
    'desc':'i love you~ mother',
}
sister = {
    'name':'sister_name',
    'relatioin':'sister',
    'age':20,
    'job':'studient',
    'desc':'i love you~ father',
}

file_url = 'C:\\DreamHyo\\_KorIT\\my_family.txt'

file_family = open('C:\\DreamHyo\\_KorIT\\my_family.txt','w')
file_family.close()

file_family = open(file_url,'w')
# data = father['name'] + ','+father['relatioin']+','+str(father['age'])+','+father['job']+','+father['desc']+'\n'
data = father['name'] + ','+father['relatioin']+','+str(father['age'])+','+father['job']+','+father['desc']+'\n'
file_family.write(data)

file_family = open(file_url,'a')
data = mother['name'] + ','+mother['relatioin']+','+str(mother['age'])+','+mother['job']+','+mother['desc']+'\n'
file_family.write(data)

data = sister['name'] + ','+sister['relatioin']+','+str(sister['age'])+','+sister['job']+','+sister['desc']+'\n'
file_family.write(data)
file_family.close()
# 파일 읽기
read_file = open(file_url, 'r')
file_lines = read_file.readlines()
for line in file_lines:
    print(line.replace('\n',''))