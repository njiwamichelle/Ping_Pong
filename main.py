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
speed_x,speed_y = 3,3

font.init()
text = font.Font(None, 35)
player_a_win = text.render('PLAYER A WINS!', True, (255, 255, 255))
player_b_win = text.render('PLAYER B WINS!', True, (255, 255, 255))
statistics = font.Font(None, 30)
player_a_name = statistics.render('Player A', True, (255, 255, 0))
player_a_score = statistics.render('SCORE: 0', True, (200, 0, 255))
player_b_name = statistics.render('Player B', True, (255, 255, 0))
player_b_score = statistics.render('SCORE: 0', True, (200, 0, 255))

store_a = 0
store_b = 0

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    if finish == False:
        window.blit(background, (0,0))
        player_a.reset()
        player_b.reset()
        player_a.update()
        player_b.update()
        
        window.blit(player_a_name, (10, 10))
        window.blit(player_b_name, (screenwidth - 100, 10))
        window.blit(player_a_score, (10, 40))
        window.blit(player_b_score,  (screenwidth - 100, 40))
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, player_a) or sprite.collide_rect(ball, player_b):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > screenheight - 50 or ball.rect.y < 50:
            speed_y *= -1
        if ball.rect.x < 0:
            ball.rect.x = 450
            ball.rect.y = 300
            store_b += 1
            player_b_score = statistics.render('SCORE: ' + str(store_b), True, (200, 0, 255))
            
        if ball.rect.x > screenwidth:
            ball.rect.x = 450
            ball.rect.y = 300
            store_a += 1
            player_a_score = statistics.render('SCORE: ' + str(store_a), True, (200, 0, 255))
        if store_a >=  20:
            window.blit(player_a_win, (screenwidth/2 - 100, screenheight/2 - 100))
            finish = True
        if store_b >= 20:
            window.blit(player_b_win, (screenwidth/2 - 100, screenheight/2 - 100))
            finish = True



    display.update()
    clock.tick(FPS)
display.update()
clock.tick(FPS)

