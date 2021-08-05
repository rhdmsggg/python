#람다함수.py
#람다함수 : 파이썬에서는 이름이 없고 함수 객체만 존재하는 익명함수를 만들 수 
# 있다. 간단한 함수라면 람다를 사용하는 것이 편리할 때가 있다.
#def를 사용할 수 없는 곳에 주로 쓰인다.
add = lambda a,b : a+b
result = add(3,4)
print(result)

#두 개의 인수를 받아 더한 값을 돌려 주는 람다함수
def add(a,b):
    return a+b
result = add(3,4)
print(result)

#pass : 아무일도 하지 않는 코드를 작성 할 때 사용
#아무것도하지않는 함수, 클래스를 만들 때 사용
while True:
    pass
KeyboardInterrupt

class Temp:
    pass