#랜덤 숫자 맞추기
import random

print(">>숫자 맞추기 게임<<")

choice = random.randrange(100)

while True:
    #사용자에게 숫자 입력 요청 후 점수로 타입 변환
    user_choice = int(input('점수를 입력하세요 : '))

    #컴퓨터가 선택한 숫자와 입력받은 숫자가 맞으면 무한 루프 탈출
    if choice == user_choice:
        break
    
    #입력 숫자와 컴퓨터 선택 숫자 비교 및 정보 제공
    if choice <user_choice:
        print("너무 높아요")
    else:
        print('너무 낮아요')

print("정답입니다. 프로그램을 종료합니다.")

