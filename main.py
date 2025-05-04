from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed,wight=55,height=55):
        super().__init__()
        self.img=transform.scale(
            image.load(img),
            (wight,height)
        )
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def reset(self):
        window.blit(self.img,(self.rect.x,self.rect.y))

цвет_фона=(200,255,255)
win_w=600
win_h=500

window=display.set_mode((win_w,win_h))
window.fill(цвет_фона)

game=True
finish=True

clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not finish:
        window.fill(цвет_фона)
    
    display.update()
    clock.tick(FPS)
