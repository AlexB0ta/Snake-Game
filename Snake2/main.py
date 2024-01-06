import pygame,random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body=[Vector2(9,10),Vector2(9,11),Vector2(10,11)]
        self.food_f=False

    def draw_body(self):
        for each_body_part in self.body:
            body_part=pygame.Rect(each_body_part.x*cell_size,each_body_part.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(0,255,0),body_part)

    def move_body(self,dir):
        if self.food_f==False:
            if dir == 'left':
                self.body.insert(0,self.body[0]+Vector2(-1,0))
            if dir == 'right':
                self.body.insert(0,self.body[0]+Vector2(1,0))
            if dir == 'up':
                self.body.insert(0,self.body[0]+Vector2(0,-1))
            if dir == 'down':
                self.body.insert(0,self.body[0]+Vector2(0,1))
            self.body.pop()
        else:
            if dir == 'left':
                self.body.insert(0,self.body[0]+Vector2(-1,0))
            if dir == 'right':
                self.body.insert(0,self.body[0]+Vector2(1,0))
            if dir == 'up':
                self.body.insert(0,self.body[0]+Vector2(0,-1))
            if dir == 'down':
                self.body.insert(0,self.body[0]+Vector2(0,1))
            self.food_f=False

    def add_body(self):
        self.food_f=True

    def check_colision(self):
        head=self.body[0]
        aux_body=self.body[1:]
        if head in aux_body:
            return True
        else:
            return False


class Food:
    def __init__(self):
        self.x=random.randint(0,19)
        self.y=random.randint(0,19)
        self.food=Vector2(self.x,self.y)

    def place_food(self):
        mancare_rec=pygame.Rect(self.x*cell_size,self.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,0,0),mancare_rec)




pygame.init()
SCREEN_HEIGHT=800
SCREEN_WIDTH=800
cell_size=40
cell_number=20
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 50)
text = font.render('GAME OVER', True, (0,0,255))

sarpe=Snake()
mancare=Food()

while True:
    pygame.display.update()
    screen.fill((0,0,0))
    sarpe.draw_body()
    mancare.place_food()
    colision=sarpe.check_colision()
    curent_time=pygame.time.get_ticks()

    if colision==True:
        screen.blit(text,(300,400))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()


    if mancare.food == sarpe.body[0]:
        mancare = Food()
        mancare.place_food()
        sarpe.add_body()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                sarpe.move_body('left')
            if event.key == pygame.K_RIGHT:
                sarpe.move_body('right')
            if event.key==pygame.K_UP:
                sarpe.move_body('up')
            if event.key==pygame.K_DOWN:
                sarpe.move_body('down')
