import pygame
from random import randint as rnd
import time
pygame.font.init()

#задание размера экрана
size = (1600,900)
screen = pygame.display.set_mode(size)
score=0
BLUE = (0,169,157)
BBLUE = (100,100,255)
BLACK_COLOR= (0,0,0)
clock = pygame.time.Clock()
done = False
df=550
#file_address=os.path.join("200h","a")
car=pygame.image.load("a.png")
car2=pygame.image.load("b.png")
CB=pygame.image.load("c.png")

class Car():
    def __init__(self):
        a=rnd(0,2)
        if a==0:
            print(a)
            self.x = -400
            self.speed=rnd(30,80)
        else:
            self.x = 2000
            self.speed=-rnd(30,80)
        self.y = df

    def move(self):
        if self.x>2100:
            self.x = -rnd(150,400)
        elif self.x<-500:
            self.x = rnd(1800,2000)
        self.x+=self.speed
        if self.y==550 and  self.x-800<75 and self.x-800>-75:
            pygame.quit()


    def jumpUp(self):
        self.y += 225
        if self.y<-125:
            self.y = 1000
        if self.y>1000:
            self.y = -125
        
    def jumpDown(self):
        self.y -= 225
        if self.y>1000:
            self.y = -125
        
       
    def draw(self):
        self.move()
        print(self.y, self.x)
        #pygame.draw.circle(screen, BLUE, [self.x, self.y], 100)
        #pygame.draw.rect(screen, BLUE, (self.x-150, self.y-100, 300, 200))
        if self.speed<0:
            screen.blit(car,(self.x-100, self.y-100))
        else:
            screen.blit(car2,(self.x-100, self.y-100))
cars=[]
for  all in range(0,5):
    cars.append(Car())
    df-=225

while not done:
    #скорость обновления экрана
    clock.tick(10)
    
    #очищение экрана
    screen.fill((100, 100, 100))
    #анализ действий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
   
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            time.sleep(0.2)
            for all in cars:
                all.jumpUp()
            score+=1
        elif event.key==pygame.K_DOWN:
            time.sleep(0.2)
            for all in cars:
                all.jumpDown()
            score-=1
        
    for all in cars:
        all.draw()
    font = pygame.font.SysFont('comicsans', 75)
    if score>=0:
        Aegon_Targaryen=str(score)
    else:
        Aegon_Targaryen="0"
    text = font.render(Aegon_Targaryen, 1, (0,0,0))
    screen.blit(text, (50, 50))
    #pygame.draw.circle(screen, BBLUE,[800,550] , 75)   
    screen.blit(CB,(753,475))
    pygame.display.flip()
pygame.quit()
