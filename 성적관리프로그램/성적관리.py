import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 엑셀파일 불러오기
def load_excel():
    global student_file, grade_assignment, grade_final, grade_middle, grade_attendance
    # 학번 오름차순으로 정렬해서 저장 null값이 있으면 0점으로 치환
    student_file = pd.read_excel('Entity/학생.xlsx').sort_values(by = '학번').fillna(0)
    grade_assignment = pd.read_excel('Entity/성적_과제.xlsx').sort_values(by = '학번').fillna(0)
    grade_final = pd.read_excel('Entity/성적_기말.xlsx').sort_values(by = '학번').fillna(0)
    grade_middle = pd.read_excel('Entity/성적_중간.xlsx').sort_values(by = '학번').fillna(0)
    grade_attendance = pd.read_excel('Entity/성적_출석.xlsx').sort_values(by = '학번').fillna(0)
# 파일 행 수 추출
def excel_row_count():
    # 엑셀 파일에 오타가 없다고 가정
    # 행의 수가 다른 엑셀 파일이 있으면 종료
    if len(student_file) != len(grade_assignment) or len(student_file) != len(grade_final) or len(student_file) != len(grade_middle) or len(student_file) != len(grade_attendance):
        print("파일의 학생 수가 일치하지 않습니다.")
        exit()
    # 학생 수 반환
    # 40명이 넘으면 40명까지만 처리
    if len(student_file) > 40:
        return 40
    return len(student_file)

# 평점 계산
def get_rate(attendance, grade):
    if attendance < 60: 
        rate = 'F'
        app = "(출석미달)" # 비고
    else:
        app = " "
        if grade >= 90:
            rate = 'A'
        elif grade >= 80:
            rate = 'B'
        elif grade >= 70:
            rate = 'C'
        elif grade >= 60:
            rate = 'D'
        else:
            rate = 'F'
    return app, rate

rating = [] # 평점을 저장할 리스트
load_excel() #엑셀파일 호출
student_rows = excel_row_count() #파일의 행 개수 계산
result_file = student_file #최종 결과를 저장할 df
# 데이터프레임에 컬럼 및 값 추가
result_file['총점'] = ((grade_middle['성적'] + grade_final['성적']) * 0.3 + 
                      (grade_attendance['성적'] + grade_assignment['과제1'] + grade_assignment['과제3'] + grade_assignment['과제2'] + grade_assignment['과제4']) * 0.2 )
# 한줄씩 불러와서 평점 계산 후 rating에 저장
for index in range(student_rows):
    attendance = int(grade_attendance.loc[index, '성적'])
    grade = int(result_file.loc[index, '총점'])
    app, rate = get_rate(attendance, grade)
    rating.append([rate, app])
# 평점, 비고 컬림 최종 결과에 추가
df = pd.DataFrame(rating, columns=['rate', '비고'])
result_file['평점'], result_file['비고'] = df['rate'], df['비고']
# 이름기준 오름차순 정렬
result_file = result_file.sort_values(by = ['이름'])
print(result_file.reset_index(drop = True))
# 엑셀파일로 저장
result_file.to_excel("Entity/최종 성적.xlsx", index = False)

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/gulim.ttc'  # 사용할 폰트 경로
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.title('최종성적', fontproperties=font_prop)
plt.xlabel('평점', fontproperties=font_prop)
# A부터 오름차순으로 차트 출력
sns.countplot(x='평점', data=result_file, order=['A', 'B', 'C', 'D', 'F'])
plt.show()




    

    

