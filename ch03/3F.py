# 입력층(x, b1)에서 1층(a1)으로 신호 전달
import numpy as np

x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])

# print(x.shape)
# print(w1.shape)
# print(b1.shape)

a1 = np.dot(x, w1) + b1
print(a1)  # [0.3 0.7 1.1]

# 입력층(x, b1)에서 1층(a1)으로 신호 전달 - 활성화 함수의 처리


def sigmoid(x):
    return 1/(1+np.exp(-x))


z1 = sigmoid(a1)
print(z1)  # [0.57444252 0.66818777 0.75026011]

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

# print(z1.shape)  # (3,)
# print(w2.shape)  # (3, 2)
# print(b2.shape)  # (2,)

a2 = np.dot(z1, w2) + b2
print(a2)   # [0.51615984 1.21402696]
z2 = sigmoid(a2)
print(z2)   # [0.62624937 0.7710107 ]

# 2층 => 출력층
# point = 항등함수!!


def identify_function(x):
    return x


w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

a3 = np.dot(z2, w3) + b3
print(a3)   # [0.31682708 0.69627909]

y = identify_function(a3)
print(y)    # [0.31682708 0.69627909]
