# 1.6 Matplotlib

# # 1.6-1 단순 그래프 그리기
# import numpy as np
# import matplotlib.pyplot as plt

# # 데이터 준비
# x = np.arange(0, 6, 0.1)  # 0에서 6까지 0.1 간격으로 생성
# y = np.sin(x)  # sin() 그래프 생성

# # 그래프 그리기
# plt.plot(x, y)
# plt.show()  # 그린 그래프를 표시하는 함수

# # 1.6-2 pyplot의 기능
# import numpy as np
# import matplotlib.pyplot as plt

# # 데이터 준비
# x = np.arange(0, 6, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # 그래프 그리기
# plt.plot(x, y1, label="sin")                    # sin(x) 그래프
# plt.plot(x, y2, linestyle="--", label="cos")    # cos(x) 그래프를 점선으로
# plt.xlabel("x")     # x축 명칭은 x
# plt.ylabel("y")     # y축 명칭은 y
# plt.title(' sin & cos ')  # 그래프 제목
# plt.legend()        # 범례 표시
# plt.show()

# # 1.6-3 이미지 표시하기
# import matplotlib.pyplot as plt
# from matplotlib.image import imread

# img = imread('./photo.png')  # 이미지 읽어오기

# plt.imshow(img)
# plt.show()
