# # np.array() 배열 출력해보기
# import numpy as np

# x = np.array([1.0, 2.0, 3.0])
# print(x)
# print(type(x))

# # np.array() 의 배열들로 사칙연산 해보기
# import numpy as np

# x = np.array([1.0, 2.0, 3.0])
# y = np.array([2.0, 4.0, 6.0])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x % y)

# # numpy N차원 배열
# import numpy as np

# a = np.array([[1, 2], [3, 4]])
# # # 행렬의 형상을 반환하는 shape( n행 , m열 )
# # print(a.shape)  # (2, 2)출력
# # # 행렬에 담긴 원소의 자료형을 반환하는 dtype
# # print(a.dtype)  # int32 출력

# b = np.array([[3, 0], [0, 6]])
# print(a+b)
# print(a*b)
# print(a)
# print(a*10)

# # Broadcast : 어떤 행렬이라고 스칼라값을 가진 정수와 사칙연산 가능
# import numpy as np
# a = np.array([[1, 2], [3, 4]])
# b = np.array([10, 20])
# print(a*b)

# # 원소 접근
# # 원소의 index는 0부터 시작!!!
# import numpy as np

# x = np.array([[51, 55], [14, 19], [0, 4]])  # 값이 들어간 배열 생성
# # print(x)
# # print(x[0])         # x배열의 0번째 index 값 출력
# # print(x[0][1])      # x배열의 0번째 index 배열 안의 1번 index 값 출력

# x = x.flatten()       # x를 1차원 배열로 변환(=> 평탄화)
# print(x)
# print(x[np.array([0, 2, 4])])  # x 배열에서 index가 0,2,4인 원소 얻기

# print(x > 15)           # 조건에 부합한지 bool값으로 출력
# print(x[x > 15])        # 조건에 맞는 값들을 추출해 그 값들을 출력
