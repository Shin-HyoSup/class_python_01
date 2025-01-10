# 1. 기본 점수 - 학점 변환
#   - input
#   점수 ex)calculate_grade(85)
#   - output
#   학점 : B
def calculate_grade(score):
    grade_dict = {
        'A': range(90, 101),
        'B': range(80, 90),
        'C': range(70, 80),
        'D': range(60, 70),
        'F': range(0, 60)
    }
    
    for grade, score_range in grade_dict.items():
        if score in score_range:
            return grade
    
    return "잘못된 점수입니다"

# 사용 예시
print('1. 학점 :',calculate_grade(85))  # 'B' 출력
print('*'*50)
# 2. 여러 과목 처리 + 딕셔너리
#   - input
#   scores = {
#     '국어': 85,
#     '영어': 92,
#     '수학': 78
#   }
#   - output
#   {'국어': 'B', '영어': 'A', '수학': 'C'}
def process_grades(student_scores):
    # student_scores는 {'과목명': 점수} 형태의 딕셔너리
    result = {}
    
    for subject, score in student_scores.items():
        if 90 <= score <= 100:
            grade = 'A'
        elif 80 <= score < 90:
            grade = 'B'
        elif 70 <= score < 80:
            grade = 'C'
        elif 60 <= score < 70:
            grade = 'D'
        else:
            grade = 'F'
        
        result[subject] = grade
    
    return result

# 사용 예시
scores = {
    '국어': 85,
    '영어': 92,
    '수학': 78
}
print('2.',process_grades(scores))  # {'국어': 'B', '영어': 'A', '수학': 'C'}
print('*'*50)
# 3. 심화버전(평균,최고/최저 점수 과목 등..)
#   - input
#   student_scores = {
#     '국어': 85,
#     '영어': 92,
#     '수학': 78,
#     '과학': 63,
#     '사회': 95
#   }
#   - output
#   과목별 성적: {'국어': 'B', '영어': 'A', '수학': 'C', '과학': 'D', '사회': 'A'}
#   평균 점수: 82.6
#   최고 점수 과목: 사회
#   최저 점수 과목: 과학
#   Pass/Fail 결과: {'국어': 'Pass', '영어': 'Pass', '수학': 'Pass', '과학': 'Pass', '사회': 'Pass'}

def analyze_grades(student_scores):
    # ************** 결과를 저장할 딕셔너리 ******************
    analysis = {
        'grades': {},        # 과목별 학점
        'average': 0,        # 평균 점수
        'highest': '',       # 최고 점수 과목
        'lowest': '',        # 최저 점수 과목
        'pass_fail': {}      # 과목별 Pass/Fail
    }
    
    # 최고/최저 점수 초기화
    max_score = float('-inf')   # python 에서 제공하는 가장 작은 수(마이너스 무한대),infinite
    min_score = float('inf')    # python 에서 제공하는 가장 큰 수(플러스 무한대)
    
    # 점수 합계 계산을 위한 변수
    total_score = 0
    
    # 각 과목 처리
    for subject, score in student_scores.items():
        # 학점 계산
        if 90 <= score <= 100:
            grade = 'A'
        elif 80 <= score < 90:
            grade = 'B'
        elif 70 <= score < 80:
            grade = 'C'
        elif 60 <= score < 70:
            grade = 'D'
        else:
            grade = 'F'
        
        # 결과 저장
        analysis['grades'][subject] = grade
        analysis['pass_fail'][subject] = 'Pass' if score >= 60 else 'Fail'
        
        # 최고/최저 점수 과목 확인
        if score > max_score:
            max_score = score
            analysis['highest'] = subject
        if score < min_score:
            min_score = score
            analysis['lowest'] = subject
            
        total_score += score
    
    # 평균 계산
    analysis['average'] = total_score / len(student_scores)
    
    return analysis

# 사용 예시
student_scores = {
    '국어': 85,
    '영어': 92,
    '수학': 78,
    '과학': 63,
    '사회': 95
}

result = analyze_grades(student_scores)
print("3. 과목별 성적:", result['grades'])
print(f"평균 점수: {result['average']:.1f}")
print("최고 점수 과목:", result['highest'])
print("최저 점수 과목:", result['lowest'])
print("Pass/Fail 결과:", result['pass_fail'])