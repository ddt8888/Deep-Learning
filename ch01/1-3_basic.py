# a = [1, 2, 3, 4, 5, 6]
# print(a)  # 리스트 a 출력
# print(len(a))   # 리스트 a의 길이 출력
# print(a[0])  # 리스트 a의 0번째(index 0)값 출력
# print(a[5])  # 6
# a[5] = 99   # 리스트 a의 5번째(index 5)값 99로 대입
# print(a[5])  # 99

# print(a)

# print(a[0:2])  # 리스트 a의 index 0 <= n < 2 값 출력
# print(a[1:])    # 리스트 a의 index 1 부터 값 출력
# print(a[:3])    # 리스트 a의 index 0 <= n < 3 값 출력
# print(a[:-1])   # 리스트 a의 가장 오른쪽에서 첫번째를 제외한 값 출력
# print(a[:-2])   # 리스트 a의 가장 오른쪽에서 두번째까지 제외한 값 출력

# # 딕셔너리
# me = {'height': 180}    # {'height': 180}이 들어간 딕셔너리 생성
# print(me['height'])     # 원소에 접근해서 출력
# me['weight'] = 70       # 새 원소 추가
# print(me)

# # bool(True or False / 참 or 거짓)
# hungry = True
# sleepy = False
# print(type(hungry))
# print(not hungry)  # 배고프지 않다(hungry가 True이기 때문에 not으로 인해 거짓이 됨)
# print(hungry and sleepy)    # hungry와 sleepy가 모두 True 여야 True 반환
# print(hungry or sleepy)     # hungry와 sleepy 둘중 하나만 True여도 True 반환

# # if 문
# # if에 조건문을 입력해 조건에 맞는 것만 출력
# # 조건문이 충족되지 않는다면 else에 작성한 출력문 출력
# hungry = True

# if hungry:
#     print("I'm hungry...")

# hungry = False

# if hungry:
#     print("I'm hungry")
# else:
#     print("I'm not hungry")
#     print("I'm sleepy")

# # for 문(반복문)
# for i in [1, 2, 3]:
#     # end가 있으면 한줄에 end조건에 맞게 표시 없으면 한줄에 하나씩
#     print(i, end=" ")

# # 함수(def)
# def hello():
#     print("Hello World")
# hello()
# def hello(object):
#     print("Hello " + object + "!")


# hello("kimsang")
