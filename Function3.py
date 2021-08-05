#Function3.py
#정의되지 않은 인자 처리 (사전식)
def userURIBulider(server,port, **user):
    strURL = "http://"+server+":"+port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBulider("Bitcamp","80",id="kim",passwd="1234"))
print(userURIBulider("Bitcamp","80",id="kim",passwd="1234",
    name="mike", age = "30"))

#람다함수(이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

#제너레이터(값을 생성해서 추출하고 마지막에 리턴)
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
#호출
for char in reverse("gold"):
    print(char)

#단순한 예제
def abc():
    """이함수는 간단한 연습을 위해 만든 함수 입니다."""

    s = "abc"
    for char in s:
        return char
#호출
for char in abc():
    print(char)

print(help(abc))