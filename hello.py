import random


print('hello world')
print('짜장면이냐 짬뽕이냐?')

# 만약에 짜장과 짬뽕 둘중에 하나 추천
# 내가 짜장이나 짬뽕을 적으면 짜장이나 짬뽕중에서 추천
# 아니면 둘다(짬짜?)
a = input('먹고 싶은거 입력:')
menu = '짜장', '짬뽕'
print(f'인공지능이 추천해주는 메뉴: {a}')

m = random.choice(menu)

if a == '짜장' or a == '짬뽕': 
    print(f"{m} 먹어!!") #참일떄만
    #여기에서 짜장과 짬뽕중에 
    #인공지능이 추천 해주는 결과는?
else:
    print("짬짜면 먹어!!")



