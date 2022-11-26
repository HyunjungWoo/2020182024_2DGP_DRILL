from pico2d import *

# 이벤트 정의
#RD, LD, RU, LU = 0, 1, 2, 3  # right down, left down, right up, left up
RD, LD, RU, LU ,AD,AU= range(6) #위와 의미는 동일

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,
    (SDL_KEYDOWN,SDLK_a):AD,
    (SDL_KEYUP,SDLK_a):AU
} # 단순화 맵핑? 키입력을 단일이벤트로 만들기 위해서


# 스테이트를 구현 - 클래스를 이용해서..
class IDLE:
    @staticmethod   # c++에서 클래스안에 스태틱선언한 것과 비슷(self생략)
    def enter(self,event):
        print('ENTER IDLE')
        self.dir =0

    @staticmethod
    def exit(self):
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame +1 )%8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame *100,300,100,100,self.x,self.y)
        else:
            self.image.clip_draw(self.frame*100,200,100,100,self.x,self.y)

class RUN:
    def enter(self,event):
        print('ENTER RUN')
        if event ==RD:
            self.dir +=1
        elif event ==LD:
            self.dir -=1
        elif event ==RU:
            self.dir -=1
        elif event ==LU:
            self.dir +=1


    def exit(self):
        print('ENTER RUN')
        self.face_dir =self.dir
        pass

    def do(self):
        self.frame =(self.frame +1)%8


        self.x += self.dir
        self.x =clamp(0,self.x,800)

        pass

    def draw(self):
        if self.dir ==-1:
            self.image.clip_draw(self.frame *100,0,100,100,self.x,self.y)
        elif self.dir ==1:
            self.image.clip_draw(self.frame *100,100,100,100,self.x,self.y)

class LOOP:
    def enter(self,event):
        print('ENTER LOOP')
        pass

    def exit(self):
        print('EXIT LOOP')
        self.face_dir = self.dir
        pass
    def do(self):

        if self.x>=0:
            self.x+=10
        elif self.x<=800:
            self.x-=10

    def draw(self):

        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

#상태변환 테이블
next_state = {
    IDLE : { RU: RUN, LU: RUN, RD: RUN, LD: RUN ,AD:LOOP,AU:LOOP},  #동시에 누를 때도 RUN
    RUN  : { RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE,AD:LOOP,AU:LOOP},
     LOOP:{ AD:IDLE,AU:IDLE,RU:RUN,RD:RUN,LD:RUN,LU:RUN}
}



class Boy:

    def handle_event(self, event): #event : 키 입력 이벤트
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) #ctrl + / 커맨드 아웃


    def add_event(self, event):
        self.q.insert(0, event)


    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []

        #초기 상태 설정과, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self,None)


    def update(self):
        self.cur_state.do(self)

        if self.q:  # 만약에 list q 에 뭔가 들어있으면
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
