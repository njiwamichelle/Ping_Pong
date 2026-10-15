from pygame import *

screenwidth = 900
screenheight = 600

window = display.set_mode((screenwidth, screenheight))
display.set_caption("Ping-Pong")

background = transform.scale(image.load('background.jpg'), (screenwidth, screenheight))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image =transform.scale(image.load(img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerOne(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < screenheight - self.rect.height -5:
            self.rect.y += self.speed

class PlayerTwo(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < screenwidth - 5:
            self.rect.y += self.speed

player_a = PlayerOne('racket.png', 30, 200, 40, 100, 5)
player_b = PlayerTwo('racket.png', 820, 400, 40, 100, 5)

ball = GameSprite('tennisball.png', 450, 300, 40, 40, 8)
    
running = True
finish = False
FPS = 60
clock = time.Clock()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if finish == False:
        window.blit(background, (0, 0))
        player_a.reset()
        player_b.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)

