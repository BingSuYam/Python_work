# 문자열 처리 함수
import os
os.system ('cls')
pyton = "Python is Amazing"
print ("#################################")
print (pyton.lower()) #소문자로
print (pyton.upper()) #대문자로
print (pyton[0].isupper()) #  [] 안의 자릿수에 대문자인지를 확인 
print (len(pyton)) # 문자열 길이
print (pyton.replace("Python","Java")) # 문자열 길이
print ("#################################")


index = pyton.index("n") 
print (index) #n의 문자가 몇번째 자리숫에 위치하는지 
index = pyton.index("n",index+1) 
print (index) #n의 문자가 몇번째 자리숫에 위치하는지 
print ("#################################")
print (pyton.find("n"))
print (pyton.find("Java")) # 원하는값이 없으면 -1
print (pyton.index("Java")) # 찾는 문자가 없으면 에러코드
print ("#################################")
print (pyton.count("n"))
print ("#################################")