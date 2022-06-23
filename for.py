import random
for i in range(5):
    # print(i)
    print(f'{i+1}. hello world')

    print('짜장면이냐 짬뽕이냐?')
    a = input('먹고 싶은거 입력:')
    print(f'니가 입력한 값: {a}')
    menu = '짜장', '짬뽕'
    if a == 'a' or a == 'b':
        print('인공지능이 추천 해주는 결과는?')
        m = random.choice(menu)
        print(f"{m} 먹어!!")
    else:
        print("짬짜면 먹어!!")

# print('1. hello world')
# print('2. hello world')
# print('3. hello world')
# print('4. hello world') 