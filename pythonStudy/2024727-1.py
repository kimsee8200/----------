# string1 = "Hello"
# string2 = "World"

# print(string1 + string2)
# print(string1+" "+string2)
# print(string1 * 10)
# print((string1 + " ")*10)

# test = 10
# print(test+10)

# test = "10"
# print(test + 10)

# test1 = 10
# test2 = "10"
# test3 = 10.01

# type(test1)
# type(test2)
# type(test3)
# type(int(test2))
# type(int(test2) + 10)

# na = ["이준철",34,"seoul"]

# print(na)
# print(na[0])
# print(na[1])
# print(na[2])

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# print(s1 & s2)
# print(s1 | s2)
# print(s1 - s2)
# print(s2 - s1)
# a = 30

# if a <= -10:
#   print("이거 냉동이여유")
# elif a>=30 or a<=-30:
#   print("사장님 폐업하셔유!")
# else:
#   print("이거 실온에 놔뒀어유?")

# test = ["a","b","c"]

# print("a" in test)
# print("1967" in test)
# print("1967" not in test)

# for i in test:
#   print(i)

# for i in range(0, 10, 2):
#   print(i)
#   if i>=6:
#     print("사장님 음식 탔어!!")


number = 10
while True:
  number = number - 1
  print("워매 냉동이여유 %d" %number)
  if(number == 0):
    break