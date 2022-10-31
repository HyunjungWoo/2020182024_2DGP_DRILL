class Star:
    name = 'Star' #클래스 변수
    x = 100 #클래스 변수

    def change():
        x = 200
        print('x is ' ,x)
print('x is',Star.x)#클래스 변수 엑세스
Star.change()#클래스 함수

#파이썬은 클래스를 객체 만들기 뿐만 아니라 함수나 변수를 그룹핑해서 사용할 수 있도록 한다.

star = Star() #생성자가 없는데 생성?? 

print(type(star))
print(star.x) #비록 객체 변수로 액세스 했으나 같은 이름의 클래스 변수가 우선.

star.change() #Star.change(star)와 동일하다.

