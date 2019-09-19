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

""" 


