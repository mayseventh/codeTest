
####################################################### 사전

dic1 = {3:"dic1_first", 100:"dic1_second"}
dic2 = {"A":"dic1_first", "B":"dic2_second"}

#출력
print("dic1 is : {0}".format(dic1[3]))
print(dic1.keys())
print(dic1.values())


####################################################### 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])

name, age, hobby = "김종욱", 20, "코딩"
print(name, age, hobby)

(name, age, hobby) = "김종욱", 20, "코딩"
print(name, age, hobby)

####################################################### 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java&python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# set 추가
python.add("김태호")
print(java&python)
print(java | python)
print(java - python)

python.remove("박명수")
print(java&python)
print(java | python)
print(java - python)


