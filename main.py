from pygame import *
import os
import random


class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed,wight=55,height=55):
        super().__init__()
        self.img=transform.scale(
            image.load(img),
            (wight,height)
        )
        self.speed=speed
        self.rect=self.img.get_rect()
        self.rect.x=x
        self.rect.y=y

    def reset(self):
        window.blit(self.img,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self,part='left'):
        keys_data={
            'left':[K_UP,K_DOWN],
            'right':[K_w,K_s]

        }
        keys=key.get_pressed()
        if keys[keys_data[part][0]] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[keys_data[part][1]] and self.rect.y<win_h-80:
            self.rect.y+=self.speed

цвет_фона=(200,255,255)
win_w=600
win_h=500

window=display.set_mode((win_w,win_h))
window.fill(цвет_фона)

game=True
finish=False

clock=time.Clock()
FPS=60

speed_x, speed_y=3,3
path=os.getcwd()
ball=GameSprite(f"{path}\\ball.png",200,200,4,50,50)
rocket1=Player('kit.jpg',30,200,4,50,150)
rocket2=Player('kit.jpg',520,200,4,50,150)

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not finish:
        window.fill(цвет_фона)
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        rocket1.update('left')
        rocket2.update('right')


        if ball.rect.y>win_h-50 or ball.rect.y<0:
            speed_y*=-1

        if ball.rect.x<0 or ball.rect.x>win_w-50:
            speed_x*=-1
            цифра=random.randint(-1,1)
            if цифра!=0:
                speed_y*=цифра

        ball.reset()
        rocket1.reset()
        rocket2.reset()

    display.update()
    clock.tick(FPS)
