# 슬라이싱
import os
os.system ('cls')

jumin = "990120-1234567"

print("성별 : ",jumin[7])
print("년도 : ",jumin[0:2]) # 0~2 직전까지 의 자리수 가져오기
print("월 : " ,jumin[2:4]) # 2~4 직전까지 의 자리수 가져오기
print("일 : " ,jumin[4:6]) # 4~6 직전까지 의 자리수 가져오기

print("생년월일 : " ,jumin[:6]) # 처음부터 ~6 직전까지 의 자리수 가져오기
print("뒷자리 : " ,jumin[7:]) # 7 ~ 마지막 직전까지 의 자리수 가져오기
print ("#################뒤에서부터 자리수 뽑아내기################")
print ("뒤 7자리 : " , jumin[-7:])#맨뒤에서 7번째부터 끝까지