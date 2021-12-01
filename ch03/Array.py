# # 1차원 배열
# import numpy as np

# a = np.array([1, 2, 3, 4])
# print(a)
# print(np.ndim(a))   # 배열의 차원수를 구하는 ndim()함수
# print(a.shape)      # 배열의 형상을 반환하는 shape
# print(a.shape[0])

# # 2차원 배열
# import numpy as np

# a = np.array([[1, 2], [3, 4], [5, 6]])

# print(a)
# print(np.ndim(a))   # 배열의 차원수를 구하는 ndim()함수
# print(a.shape)      # 배열의 형상을 반환하는 shape

# # 행렬의 곱 (1)
# import numpy as np

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# print(a.shape)
# print(b.shape)
# # 행렬의 곱을 np.dot() 함수로 계산
# print(np.dot(a, b))

# # 행렬의 곱 (2)
# import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.shape)
# b = np.array([[1, 2], [3, 4], [5, 6]])
# print(b.shape)
# print(np.dot(a, b))

# # 행렬의 곱 (3) ((3x2), (2x4)) => (3x4)
# import numpy as np

# a = np.array([[1, 2], [3, 4], [4, 5]])
# print(a.shape)
# b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(b.shape)

# print(np.dot(a, b))

# 신경망에서 행렬 곱
import numpy as np

x = np.array([1, 2])
print(x.shape)  # 1x2

w = np.array([[1, 3, 5], [2, 4, 6]])
print(w)
print(w.shape)  # 2x3

y = np.dot(x, w)
print(y)
print(y.shape)  # 1x3
