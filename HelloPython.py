import numpy as np

# Install Numpy library
# 如果是使用 Anaconda 主導安裝的Python和VsCode 使用已下指令 , 安裝Library : numpy , scipy , matplotlib
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

# numpy100 練習題 https://github.com/rougier/numpy-100 
""" 
# Q2~4 . init size 10 empty with zero array.
arrayOf10 = np.zeros(10)
print(arrayOf10)
print( "%d bytes" %(arrayOf10.size))
arrayOfdouble10 = np.zeros((10,10))
print( "%d bytes" %(arrayOfdouble10.size*arrayOfdouble10.itemsize))

Hint: 全為1正列
temp = np.ones(10)
print(temp)

# Q6 . Create a null vector of size 10 but the fifth value which is 1
arrayA = np.zeros(10)
arrayA[4] = 1
print(arrayA)

# Q7. Create a vector with values ranging from 10 to 49
arrayB = np.arange(10,50)
print(arrayB)

#Q8 反轉正列
temp = np.arange(50)
temp = temp[::-1]
print(temp)

#Q9 創造3*3正列且 with values ranging from 0 to 8
temp = np.arange(9).reshape(3,3)
print(temp)

#Q10 非零正列位置
nz = np.nonzero([1,2,0,0,4,0])
print(nz)

#Q11 identity matrix 單位矩正
Z = np.eye(3)
print(Z)

#Q12
# 0 > 3*3*3
temp = np.zeros(27).reshape(3,3,3)
print(temp)
# random 3*3*3
Z = np.random.random((3,3,3))
print(Z)

#Q13
Z = np.random.random((10,10))
zMax = Z.max()
zMin = Z.min()
print( zMax , zMin)

#Q14 mean() 平均
Z = np.random.random(30)
print(Z.mean())

#Q15
Z = np.ones((10,10))
Z[1:9,1:9] = 0
Z[1:-1,1:-1] = 0
print(Z)


#Q16 How to add a border (filled with 0's) around an existing array?

# if exist 3*3 fill with 1~9
# 自己的做法
temp = np.arange(9).reshape(3,3)
temp2 = np.zeros(25).reshape(5,5)
print(temp)
print(temp2)
for i in range(0,3):
    for j in range(0,3):
        temp2[i+1][j+1] = temp[i][j]
print(temp2)

# 答案
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


#Q18
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

#Q19 
# [行的開始:行的結束:間距 , 列的開始:列的結束:間距] 
Z = np.zeros((8,8),dtype=int)
Z[0:7:2,1::2] = 1

print(Z)

""" 



print(np.unravel_index(99,(6,7,8)))