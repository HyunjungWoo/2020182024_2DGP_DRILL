from pico2d import *
import game_framework
import game_world
px,py = 0,0

MORPH_FRAMES_PER_ACTION = 42 # 프레임 장수(사진 갯수)
MORPH_TIME_PER_ACTION   = 5 #속도 조절
MORPH_ACTION_PER_TIME   = 1.0 / MORPH_TIME_PER_ACTION

DEATH_FRAMES_PER_ACTION = 19 # 프레임 장수(사진 갯수)
DEATH_TIME_PER_ACTION   = 7 #속도 조절
DEATH_ACTION_PER_TIME   = 1.0 /DEATH_TIME_PER_ACTION

JUMP_F_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
JUMP_F_TIME_PER_ACTION   = 10.0 #속도 조절
JUMP_F_ACTION_PER_TIME   = 1.0 / JUMP_F_TIME_PER_ACTION

Idle_FRAMES_PER_ACTION = 9 # 프레임 장수(사진 갯수)
Idle_TIME_PER_ACTION   = 3.0 #속도 조절
Idle_ACTION_PER_TIME   = 1.0 / Idle_TIME_PER_ACTION

PUNCH_FRAMES_PER_ACTION = 16 # 프레임 장수(사진 갯수)
PUNCH_TIME_PER_ACTION   = 2.5 #속도 조절
PUNCH_ACTION_PER_TIME   = 1.0 / PUNCH_TIME_PER_ACTION



state = { 'Idle':1, 'Punch':2 ,'JUMP_D':3, 'JUMP_U':4,'Morph':5, 'Death':6, 'Tomb':7}
class Boss_Goopy:
    jump_F =[]
    Punch = []
    jump_D = []
    jump_U = []
    Morph = []
    Death = []
    Tomb = []
    def load_images(self):
        for i in range(9): #Idle 제자리점프  이미지 리소스
            a = load_image('monster/Goopy/Phase 1/Jump/slime_jump_%d.png' % i)
            Boss_Goopy.jump_F.append(a)
        for i in range(3): #jump_D 아래로 떨어지는 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Air Down/air_down(%d).png' % i)
            Boss_Goopy.jump_D.append(a)
        for i in range(3):#jump_U 위로 올라가는 이미지 리소스
            a = load_image('monster/Goopy/Phase 1/Air UP/air_up(%d).png' % i)
            Boss_Goopy.jump_U.append(a)
        for i in range(16):#punch 펀치 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Punch/slime_punch(%d).png' % i)
            Boss_Goopy.Punch.append(a)
        for i in range(44):#morph 2페이즈 변신 이미지 리소스 
            a = load_image('monster/Goopy/Phase 1/Transition To ph2/slime_morph(%d).png' % i)
            Boss_Goopy.Morph.append(a)
        for i in range(20): #death 2페이즈 사망 이미지 리소스 
            a = load_image('monster/Goopy/Phase 2/Death/lg_slime_death(%d).png' % i)
            Boss_Goopy.Death.append(a)
    def __init__(self):
        self.hp = 503 #phase 1 = 336 , phase 2= 560 phase 3= 504 full.hp = 1400 
        self.state = state['Idle']
        self.sort = 'monster'
        self.frame = 0
        self.image_num = 0
        self.x,self.y = 600,100
        self.dir,self.diry = 1,0 #오른쪽
        self.jumpheight,self.mass = 4,3 #무게
        self.jumpcount = 3
        self.phase = 2
        self.load_images()
        self.change_morph = False
        self.change_death  = False

    def update(self):
        print(self.phase)
        if self.state == state['Idle']:
            jump_F_update(self)
        elif self.state == state['Punch']:
            punch_update(self)
        elif self.state == state['JUMP_D']:
            jump_D_update(self)
        elif self.state == state['JUMP_U']:
            jump_U_update(self)  
        elif self.state == state['Morph']:
            morph_update(self)       
        elif self.state == state['Death']:
            death_update(self)  
        
        if self.jumpcount <3:
            self.Jump_Goopy()
        else:
            if 504<=self.hp <1000 and self.change_morph == False:
                self.jumpcount = 3
                self.state = state['Morph']
            elif self.hp < 504 and self. change_death == False:
                self.jumpcount = 3
                self.state = state['Death']
                
            elif self.phase == 1:
                self.state = state['Punch']
            elif self.change_morph == True and self.phase == 2:
                self.state = state['Punch']
            
        self.y += self.diry*1 

    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.state == state['Idle']:
            jump_F_draw(self)
        elif self.state == state['Punch']:
            if self.phase == 1:
                punch_draw_phase1(self)
            elif self.phase == 2:
                punch_draw_phase2(self)
        elif self.state == state['JUMP_D']:
            jump_D_draw(self)
        elif self.state == state['JUMP_U']:
            jump_U_draw(self)  
        elif self.state == state['Morph']:
            morph_draw(self)
        elif self.state == state['Death']:
            death_draw(self)

    def get_bb(self):
        if self.phase ==1:
            return self.x -50 ,self.y-50, self.x+50,self.y +50 
        elif self.phase == 2:
            return self.x -100,self.y -100,self.x + 100,self.y +100
        elif self.state == ['Death']:
            return self.x -100,self.y -50,self.x +100,self.y +50
    
    def handle_collision(self,other,group):
       
        if other.sort == 'floor':
            if self.phase ==1:
                self.y = 101
            else: self.y = 150
            self.jumpheight = 4
            if self.jumpcount <3:
                self.state = state['Idle']
            self.jumpcount += 1 
            print(self.jumpcount)
        
            
    
            
    def Jump_Goopy(self):

        if self.jumpheight > 0:
            self.state = state['JUMP_U']
            F = (0.5* self.mass * (self.jumpheight**2)) 
        else:
            self.state = state['JUMP_D']
            F = -(0.5 * self.mass * (self.jumpheight**2))
        self.diry = round(F)
        self.jumpheight -= 0.1
        
        if self.x < 0: 
            self.dir = 1

        elif self.x > 1280:
            self.dir = -1

        if self.dir ==1:
            if self.phase ==2:
                self.x += 7
            else:self.x += 5
        else:
            if self.phase == 2:
                self.x -= 7
            else: self.x -= 5

def punch_update(self):
    self.frame  = (self.frame + PUNCH_FRAMES_PER_ACTION * PUNCH_ACTION_PER_TIME * game_framework.frame_time) % 16
def punch_draw_phase1(self):
    global px,py
    if int(self.frame) <0:
        px,py = 0,0
    elif int(self.frame) == 1:
        px ,py = -20,55
    elif int(self.frame) == 2:
        px,py = -45,0
    elif int(self.frame) == 3:
        px,py = 50,-5
    elif int(self.frame) == 4:
        px,py = 55,-10
    elif int(self.frame) == 5:
        px,py = 60,30     
    elif int(self.frame) == 6:
        px,py = 60,-20
    elif int(self.frame) == 7:
        px,py = 60,35
    elif int(self.frame) == 8:
        px,py = 0,55
    elif int(self.frame) == 9 or int(self.frame) == 10:
        px,py = -190,50
    elif int(self.frame) == 11:
        px,py = -100,40
    elif int(self.frame) == 12:
        px,py = -60,25
    elif int(self.frame) == 13:
        px,py = -30,5
    elif int(self.frame) == 14:
        px,py = -10,-5
    elif int(self.frame) == 15:
        px,py = -5,-10
        self.jumpcount = 0
        self.frame = 0
    if self.dir ==1: #오른쪽 
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    else:
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'n', self.x+px, self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0

def jump_D_update(self):
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_D_draw(self):
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_D[int(self.frame)].clip_composite_draw(0, 0, self.jump_D[int(self.frame)].w, Boss_Goopy.jump_D[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_D[int(self.frame)].w//1.5, Boss_Goopy.jump_D[int(self.frame)].h//1.5)
def jump_U_update(self):
    self.frame  = (self.frame + JUMP_F_FRAMES_PER_ACTION * JUMP_F_ACTION_PER_TIME * game_framework.frame_time) % 3
def jump_U_draw(self):
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_U[int(self.frame)].clip_composite_draw(0, 0, self.jump_U[int(self.frame)].w, Boss_Goopy.jump_U[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_U[int(self.frame)].w//1.5, Boss_Goopy.jump_U[int(self.frame)].h//1.5)   
def jump_F_update(self): #제자리 점프 프레임 설정 
    if self.phase == 1: 
        self.frame= (self.frame + Idle_FRAMES_PER_ACTION * Idle_ACTION_PER_TIME  * game_framework.frame_time) % 9
    elif self.phase == 2:
        self.frame= (self.frame + Idle_FRAMES_PER_ACTION * Idle_ACTION_PER_TIME  * game_framework.frame_time) % 8

def jump_F_draw(self): #제자리 점프 그리기
    if self.dir == 1:#오른쪽
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5,Boss_Goopy.jump_F[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.jump_F[int(self.frame)].clip_composite_draw(0, 0, self.jump_F[int(self.frame)].w, Boss_Goopy.jump_F[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.jump_F[int(self.frame)].w//1.5, Boss_Goopy.jump_F[int(self.frame)].h//1.5)
def clear_list_and_upload_ph2(self): #리스트 안에 있는거 다 지우고  phase2 upload
    Boss_Goopy.jump_F.clear()
    Boss_Goopy.Punch.clear()
    Boss_Goopy.jump_D.clear()
    Boss_Goopy.jump_U.clear()
    for i in range(8): #Idle 제자리점프  이미지 리소스
        a = load_image('monster/Goopy/Phase 2/Jump/lg_slime_jump(%d).png' % i)
        Boss_Goopy.jump_F.append(a)
    for i in range(5): #jump_D 아래로 떨어지는 이미지 리소스 
        a = load_image('monster/Goopy/Phase 2/Air Down/lg_slime_air_down(%d).png' % i)
        Boss_Goopy.jump_D.append(a)
    for i in range(4):#jump_U 위로 올라가는 이미지 리소스
        a = load_image('monster/Goopy/Phase 2/Air UP/lg_slime_air_up(%d).png' % i)
        Boss_Goopy.jump_U.append(a)
    for i in range(19):#punch 펀치 이미지 리소스 
        a = load_image('monster/Goopy/Phase 2/Punch/lg_slime_punch(%d).png' % i)
        Boss_Goopy.Punch.append(a)
def morph_update(self):
    self.frame  = (self.frame + MORPH_FRAMES_PER_ACTION * MORPH_ACTION_PER_TIME * game_framework.frame_time) % 42
def morph_draw(self):
    global px,py
    if int(self.frame) == 0: px,py = 0,0
    elif int(self.frame) == 1:  px,py  = -20,0 
    elif int(self.frame) == 2:  px,py  = -30,5
    elif int(self.frame) == 3:  px,py  = -40,5
    elif int(self.frame) == 4:  px,py  = -50,5
    elif 5<=int(self.frame)<9:  px,py  = -50,0
    elif int(self.frame) == 9:  px,py  = -50,40
    elif int(self.frame) == 10: px,py = -50,85
    elif int(self.frame) == 11: px,py = -50,110
    elif 11<int(self.frame)<17: px,py = -50,120
    elif int(self.frame) == 17: px,py = -50,110
    elif int(self.frame) == 18: px,py = -50,85
    elif int(self.frame) == 19: px,py = -50,45
    elif int(self.frame) == 20: px,py = -50,35
    elif int(self.frame) == 21: px,py = -40,28
    elif int(self.frame) == 22: px,py = -20,10
    elif 22<int(self.frame)<25: px,py = -10,0
    elif 25<=int(self.frame)<31: px,py = -50,110
    elif int(self.frame) == 31: px,py = 0,50
    elif int(self.frame) == 32: px,py = 0,60 
    elif int(self.frame) == 33: px,py = 0,80
    elif int(self.frame) == 34: px,py = 0,90
    elif int(self.frame) == 35: px,py = 0,90
    elif int(self.frame) == 36: px,py = 0,90
    elif int(self.frame) == 37: px,py = 0,90
    elif int(self.frame) == 38: px,py = 0,85
    elif int(self.frame) == 39: px,py = 0,85
    elif int(self.frame) == 40:px,py = 0,60
    elif int(self.frame) == 41:
        px,py = 0,60 
        clear_list_and_upload_ph2(self)
        self.jumpcount = 0
        self.change = True
        self.phase = 2
    if self.dir == 1: #RIGHT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'h', self.x+(-1*px), self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
        
    else: #LEFT
        Boss_Goopy.Morph[int(self.frame)].clip_composite_draw(0, 0, self.Morph[int(self.frame)].w, Boss_Goopy.Morph[int(self.frame)].h, 0,'n', self.x+px, self.y+py,Boss_Goopy.Morph[int(self.frame)].w//1.5, Boss_Goopy.Morph[int(self.frame)].h//1.5)
def punch_draw_phase2(self):
    global px,py
    if int(self.frame) == 5: px ,py = -30,-2
    elif int(self.frame) == 6: px,py = 22,-5
    elif int(self.frame) == 9: px,py = 27,0
    elif int(self.frame) == 10: px,py = 27,0
    elif int(self.frame) == 11: px,py = 27,0 
    elif int(self.frame) == 12: px,py = -70,7
    elif int(self.frame) == 13: px,py = -70,7
    elif int(self.frame) == 14: px,py = -105,-7
    elif int(self.frame) == 15:
        px,py = -110,-7
        self.jumpcount = 0
        self.frame = 0
    if self.dir ==1: #오른쪽 
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'h', self.x+(-1*px), self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    else:
        Boss_Goopy.Punch[int(self.frame)].clip_composite_draw(0, 0, Boss_Goopy.Punch[int(self.frame)].w, Boss_Goopy.Punch[int(self.frame)].h, 0, 'n', self.x+px, self.y+py,Boss_Goopy.Punch[int(self.frame)].w/1.5, Boss_Goopy.Punch[int(self.frame)].h/1.5)
    px,py = 0,0
def death_update(self):
    self.frame  = (self.frame + DEATH_FRAMES_PER_ACTION *DEATH_ACTION_PER_TIME * game_framework.frame_time) % 20
def death_draw(self):
    if int(self.frame)== 19 and self.change_death == False:
        phase3_monster = Fall_Tomb(self)
        game_world.add_object(phase3_monster,1)
        game_world.add_collision_pairs(game_world.objects[1][1],phase3_monster,'Boss:Tomb')
        game_world.add_collision_pairs(phase3_monster,game_world.objects[0][0],'Tomb:background') 
        self.change_death =True
        
    if self.dir == 1:#오른쪽
        Boss_Goopy.Death[int(self.frame)].clip_composite_draw(0, 0, self.Death[int(self.frame)].w, Boss_Goopy.Death[int(self.frame)].h, 0,'h', self.x, self.y,Boss_Goopy.Death[int(self.frame)].w//1.5,Boss_Goopy.Death[int(self.frame)].h//1.5)
    else:
        Boss_Goopy.Death[int(self.frame)].clip_composite_draw(0, 0, self.Death[int(self.frame)].w, Boss_Goopy.Death[int(self.frame)].h, 0,'n', self.x, self.y,Boss_Goopy.Death[int(self.frame)].w//1.5, Boss_Goopy.Death[int(self.frame)].h//1.5)

INTRO_FRAMES_PER_ACTION = 10 # 프레임 장수(사진 갯수)
INTRO_TIME_PER_ACTION   = 1.0 #속도 조절
INTRO_ACTION_PER_TIME   = 1.0 /INTRO_TIME_PER_ACTION

MOVE_FRAMES_PER_ACTION = 7 # 프레임 장수(사진 갯수)
MOVE_TIME_PER_ACTION   = 1.0 #속도 조절
MOVE_ACTION_PER_TIME   = 1.0 /MOVE_TIME_PER_ACTION

TombState = {'Intro':1 ,'Move':2}
class Fall_Tomb:
    image = None
    Intro = []
    Move = []
    def __init__(Tomb,boss):
        Tomb.sort = 'Tomb'
        if Fall_Tomb.image == None:
            Fall_Tomb.image = load_image('monster/Goopy/Phase 3/Intro/slime_tomb_fall_0001.png')
        Tomb.x = boss.x
        Tomb.y = 900
        Tomb.diry = 1
        Tomb.dir = boss.dir 
        Tomb.frame = 0
        Tomb.state = None
        for i in range(10): #death 3 비석 이미지 
            a = load_image('monster/Goopy/Phase 3/Intro/slime_tomb_fall(%d).png' % i)
            Fall_Tomb.Intro.append(a)
        for i in range(7): #death 3 비석 움직임 이미지 
            a = load_image('monster/Goopy/Phase 3/Move/Left/slime_tomb_move(%d).png' % i)
            Fall_Tomb.Move.append(a)
    def update(Tomb):
        print(Tomb.y)
        if Tomb.diry != 0:
            Tomb.y -= Tomb.diry *1
            
        if Tomb.state == TombState['Intro']:
            Intro_update(Tomb)
        elif Tomb.state == TombState['Move']:
            move_update(Tomb)
    
    def draw(Tomb):
        #draw_rectangle(*self.get_bb())
        if Tomb.state == TombState['Intro']:
            Intro_draw(Tomb) 
        elif Tomb.state == TombState['Move']:
            move_draw(Tomb)
        else:
            Tomb.image.draw(Tomb.x, Tomb.y, Tomb.image.w//1.5, Tomb.image.h//1.5)
        
    def get_bb(Tomb): 
        return Tomb.x -200, Tomb.y-200 ,Tomb.x +200 ,Tomb.y +200
   
    def handle_collision(Tomb,other,group):
        if other.sort =='monster':
            game_world.remove_object(other)
        elif other.sort =='floor':
            print('충돌')
            Tomb.state = TombState['Intro']
            Tomb.diry = 0

def Intro_update(Tomb):
    Tomb.frame = (Tomb.frame +INTRO_FRAMES_PER_ACTION * INTRO_ACTION_PER_TIME*game_framework.frame_time )%10
    
def Intro_draw(Tomb):
    if int(Tomb.frame) == 9:        
        Tomb.state = TombState ['Move']
        Tomb.frame = 0
    if Tomb.dir == 1:#오른쪽
        Fall_Tomb.Intro[int(Tomb.frame)].clip_composite_draw(0, 0,Fall_Tomb.Intro[int(Tomb.frame)].w,Fall_Tomb.Intro[int(Tomb.frame)].h, 0,'h', Tomb.x, Tomb.y,Fall_Tomb.Intro[int(Tomb.frame)].w//1.5,Fall_Tomb.Intro[int(Tomb.frame)].h//1.5)
    else:
        Fall_Tomb.Intro[int(Tomb.frame)].clip_composite_draw(0, 0, Fall_Tomb.Intro[int(Tomb.frame)].w, Fall_Tomb.Intro[int(Tomb.frame)].h, 0,'n', Tomb.x, Tomb.y,Fall_Tomb.Intro[int(Tomb.frame)].w//1.5, Fall_Tomb.Intro[int(Tomb.frame)].h//1.5)

def move_update(Tomb):
    Tomb.frame = (Tomb.frame +MOVE_FRAMES_PER_ACTION * MOVE_ACTION_PER_TIME*game_framework.frame_time ) % 7
def move_draw(Tomb):
    if Tomb.dir == 1:#오른쪽
        Fall_Tomb.Move[int(Tomb.frame)].clip_composite_draw(0, 0,Fall_Tomb.Move[int(Tomb.frame)].w,Fall_Tomb.Move[int(Tomb.frame)].h, 0,'h', Tomb.x, Tomb.y,Fall_Tomb.Move[int(Tomb.frame)].w//1.5,Fall_Tomb.Move[int(Tomb.frame)].h//1.5)
    else:
        Fall_Tomb.Move[int(Tomb.frame)].clip_composite_draw(0, 0, Fall_Tomb.Move[int(Tomb.frame)].w, Fall_Tomb.Move[int(Tomb.frame)].h, 0,'n', Tomb.x, Tomb.y,Fall_Tomb.Move[int(Tomb.frame)].w//1.5, Fall_Tomb.Move[int(Tomb.frame)].h//1.5)
         