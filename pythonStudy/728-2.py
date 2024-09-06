import numpy as np

a = np.array([1,2,3])
print(a)

b = np.zeros((2,3))
print(b)

c = np.ones((3,3))
print(c)

d = np.arange(10)
print(d)

e = d.reshape(2,5)
print(e)

f = np.add(a,[1,1,1]) # 더하기
print(f)

g = np.subtract(a, [2,2,2]) # 빼기
print(g)

h = np.multiply(a, [1,2,3]) # 곱하기
print(h)

i = np.divide(a,2) # 나누기
print(i)