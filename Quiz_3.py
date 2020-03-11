# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com

# 규칙 1: http:// 부분은 제외 => naver.com
# 규칙 2: 처음 마나는 점(.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#              (nav)                 (5)              (1)           (!)
import os
os.system ('cls')

url = "http://naver.com"
url = "http://google.com"
url = "http://youtube.com"
str_1 = url.replace("http://","")
str_2 = str_1[:str_1.index(".")]
password = str_1[:3] + str(len(str_2)) + str(str_1.count("e")) + "!"
print("규칙 1 : " ,str_1)
print("규칙 2 : " ,str_2)
print("규칙 3 : " ,password)
print(f"{url} 의 비밀번호는 {password} 입니다.")