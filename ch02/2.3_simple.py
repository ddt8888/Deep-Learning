# # 2.3-1 간단한 수식 구현
# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1*w1 + x2*w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1


# print(AND(0, 0))
# print(AND(1, 0))
# print(AND(0, 1))
# print(AND(1, 1))

# # 2.3-2 세타를 편향으로 치환한 수식 구현
# import numpy as np
# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7

# print(x*w)
# print(np.sum(w*x))
# print(np.sum(x*w) + b)
# # 대략 -0.2로 0보다 작기 때문에 0 출력

# # 2.3-3 '가중치와 편향을 도입'한 AND 게이트 구현
# import numpy as np


# def AND(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([0.5, 0.5])
#     b = -0.7
#     tmp = np.sum(w*x) + b
#     if tmp <= 0:
#         return 0
#     else:
#         return 1

# NAND / OR 게이트
import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # AND게이트와는 가중치(w, b)만 다르다
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# XOR 게이트 구현


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))
