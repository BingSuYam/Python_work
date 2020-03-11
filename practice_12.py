# 리스트 []

#지하철 칸별로 10명, 20명, 30명
import os
os.system ('cls')

subway1 = 10
subway2 = 20
subway3 = 30
print ("#################################")
subway = [subway1, subway2, subway3] 
subway = ["유재석","조세호","박명수"]
print (subway)
print ("조세호가 몇번째 칸에 있는지 ? >>> " + str(subway.index("조세호")))
subway.append("하하")
print ("하하가 몇번째 칸에 있는지 ? >>> " + str(subway.index("하하")))
subway.insert(1,"정형돈")
# print ("--------------------탑승자 명단---------------------------- \n\t"+ str(subway) + "\n-------------------------------------------------------------")
# print ("정형돈가 몇번째 칸에 있는지 ? >>> " + str(subway.index("정형돈")))
# print ("한명이 하차 했습니다.\n" + str(subway.pop()))
# print ("--------------------탑승자 명단---------------------------- \n\t"+ str(subway) + "\n-------------------------------------------------------------")
# print ("한명이 하차 했습니다.\n" + str(subway.pop()))
# print ("한명이 하차 했습니다.\n" + str(subway.pop()))
# print ("--------------------탑승자 명단---------------------------- \n\t"+ str(subway) + "\n-------------------------------------------------------------")
#동일인물 몇명 탑승
subway.append("유재석")
print ("--------------------탑승자 명단---------------------------- \n\t"+ str(subway) + "\n-------------------------------------------------------------")
print ("현재 유재석씨는 몇명 이 탔나요 ?? >>>>   "+ str(subway.count("유재석")))
print ("#################################")
#정렬
num_list  = [5,2,4,3,1]
num_list.sort()
print (num_list)
#순서뒤집기
num_list.reverse()
print (num_list)
# 모두 지우기
num_list.clear()
print (num_list)
print ("#################################")
# 다양한 자료형 함께 사용
mix_list = ["조세호",20 ,True]
print (mix_list)
print ("#################################")
#리스트 확장
num_list  = [5,2,4,3,1]
num_list.extend(mix_list)
print (num_list)

print ("#################################")


