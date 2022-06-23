# AI 컴퓨터가 홀인지 짝인지 문제를 낸다
# 우리가 홀 인지 짝인지 입력한다
# 내가 입력한 값과 컴퓨터가 문제를 낸 값과
# 비교를 해서 맞으면 맞다 틀리면 틀렸다를 출력
# 5번 게임을 반복 한다
import random

holjjak = '홀', '짝'
# 여기서 반복
n = input('몇번 게임을 할거냐?')
for i in range(int(n)):  # 숫자로 바꿔서
    print(f'{i+1} / {n} 게임')
    com = random.choice(holjjak)
    # print(f'컴이낸 낸 문제: {com}')
    user = input('홀 인지 짝인지 입력: ')
    # 만약에 com과 user가 같으면 맞다
    if com == user:
        print('맞다')
    # 아니면 틀렸다
    else:
        print('틀렸다')