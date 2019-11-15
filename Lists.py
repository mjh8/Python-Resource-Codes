import numpy as np
from numpy.random import randn



N = 10000000
counter = 0
for i in randn(N):
    if(i < 1 and i > -1):
        counter = counter + 1
answer = counter / N
print(answer)        



MyFirstList = [2, 3, 4, 5]

MyFirstList

range(15)
list(range(15))

y = list(range(8))
y

w = list(range(100,111,5))
w