# ¡Crea tu propio juego de disparos!
from random import *
from pygame import *

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


# clase del jugador principal
class Player(GameSprite):
    def update(self):
        global count_goal
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - 90:
            self.rect.x += self.speed
        wins = font.render(
            'Aciertos:'+ str(count_goal), True, (255, 255, 255)
        )
        win.blit(wins, (0, 50))
    def fire(self):
        bal = bala('bullet.png', self.rect.centerx, self.rect.top, 30, 50, 2)
        bal.add(balas)
class bala(GameSprite):
    def update(self):
        self.rect.y -= 1
        if self.rect.y <= 1:
            self.kill()
class enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global count_enemy
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(40, 660)
            self.speed = randint(2, 4)
            count_enemy += 1
        winw = font.render(
            'Fallos:'+ str(count_enemy), True, (255, 255, 255)
        ) 
        win.blit(winw, (0, 0))
WIDTH, HEIGHT = 700, 500
win = display.set_mode((WIDTH, HEIGHT))
display.set_caption("MONOS ESPACIALES")
count_enemy = 0
count_goal = 0
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
font.init()
font = font.Font(None, 50)
end = font.render(
    'F, Fallaste', True, (255, 0, 0)
)
pedro = Player('rocket.png', 80, 400, 60, 80, 8)
balas = sprite.Group()
monsters = sprite.Group()
perso = sprite.Group()
perso.add(pedro)
for i in range (1,6):
    monster = enemy('ufo.png', randint(40, 660), 0, 40, 60, randint(1, 3))
    monsters.add(monster)
mixer.init()
mixer.music.load('Black Vortex.mp3')
mixer.music.play()
fire = mixer.Sound('fire.ogg')


clock = time.Clock()
finish = False
game = True
while game:
    win.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                pedro.fire()

    if finish != True:
        pedro.reset()
        pedro.update()
       
        monsters.draw(win)
        monsters.update()
        balas.draw(win)
        balas.update()

    if count_enemy >= 3:
        finish = True
        win.blit(end, (300, 200))
    
    if sprite.groupcollide(balas, monsters, True, True):
        count_goal += 1
        monster = enemy('ufo.png', randint(40, 660), 0, 40, 60, randint(1, 3))
        monsters.add(monster)
    if sprite.groupcollide(monsters, perso, True, True):
        finish = True
        win.blit(end, (300, 200))
    display.update()
    clock.tick(60)

#hgfnduijlw g4rby uwhlf FNY UOEGHSUYIEHWi fwhyASUHFG UIGNAIÒ´2 130f