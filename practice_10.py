# 문자열 포맷
import os
os.system ('cls')
print ("#################################")
print ("a" + "b")
print ("a","b")
print ("#################################")
print ("나는 %d살 입니다." % 20)
print ("나는 %s를 좋아해요." % "파이썬")
print ("Apple 은 %c로 시작해요" % "A")
print ("나는 %s살 입니다." % 20)
print ("나는 %s색과 %s색을 좋아해요 " % ("파랑","빨간"))
print ("#################################")
print ("나는 {}살 입니다." .format(20))
print ("나는 {0}색과 {1}색을 좋아해요 " .format("파랑","빨간"))
print ("나는 {1}색과 {0}색을 좋아해요 " .format("파랑","빨간"))
print ("#################################")
print("나는 {age}살이며 무슨 {color}색을 좋아해요.".format(age=20,color ="빨간"))
print("나는 {color}색을 좋아하고 {age}살 이에요.".format(age=20,color ="빨간"))
print ("###############파이썬 (version.3.6 이상)##################")
age = 20
color = "빨간"
print (f"나는 {age}살이며 무슨 {color}색을 좋아해요.")
print ("#################################")


