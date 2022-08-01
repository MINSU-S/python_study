
# MySQL과 Python 연동하기 -------------------------------------------------------------------

import	pymysql
import	pandas	as	pd

# conn = 연결자
conn = pymysql.connect(host='localhost', user='root', password='206477',
db = 'sakila', charset='utf8')  # host = 'localhost'  or 127.0.0.1 or 연동 IP주소

cur = conn.cursor()  # 커서 객체 생성(데이터를 받아오기 위해)

cur.execute('select	* from language') 
rows = cur.fetchall()	# 모든 데이터를 가져옴
print(rows)

language_df = pd.DataFrame(rows)    # DataFrame 형태로 변환
print(language_df)

cur.close() # 커서 객체 닫기
conn.close() # DB 연결 닫기

# commit() 함수
# 데이터를 추가, 수정, 삭제 등의 작업을 수행한 다음에 실행
# -------------------------------------------------------------------------------------------

# 복잡한 쿼리문 실행 (inner join 내용)

import	pymysql

conn =	pymysql.connect(host='localhost', user='root', password='206477',
db = 'sakila', charset='utf8')

cur	=	conn.cursor()
query	=	"""
select c.email
from customer as c
inner join rental as r	
on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)"""

cur.execute(query,	('2005-06-14'))
rows = cur.fetchall()	#	모든 데이터를 가져옴
for	row	in	rows:
    print(row)

cur.close()
conn.close()

