import sqlite3

# 데이터베이스 연결 (데이터베이스 파일이 없으면 새로 생성)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_info (
    team_name TEXT,
    student_name TEXT,
    region TEXT,
    grade INTEGER
)
''')

# 데이터 삽입 예시
students_data = [
    ('Team A', 'John Doe', 'New York', 85),
    ('Team B', 'Jane Smith', 'Los Angeles', 90),
    ('Team C', 'Emily Davis', 'Chicago', 88),
    ('Team D', 'Michael Brown', 'Houston', 92)
]

cursor.executemany('''
INSERT INTO student_info (team_name, student_name, region, grade) 
VALUES (?, ?, ?, ?)
''', students_data)


# 변경사항 저장
conn.commit()

# 데이터 확인
cursor.execute('SELECT * FROM student_info')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 연결 종료
conn.close()
