import pygame
import Pong_OBjects
pygame.init()

screen_width = 700
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('PONG')

clock = pygame.time.Clock()

def redraw_window():
    win.fill((0,0,0)) #this gets rid of previous square before drawing another one       
    left_paddle.draw(win)
    ball.draw(win)
    right_paddle.draw(win)

    #score
    font = pygame.font.SysFont('timesnewroman', 40)
    text = font.render(str(left_score) + ' | ' + str(right_score), 1, (255,255,255))
    win.blit(text, (350 - text.get_width()/2, 10))

    pygame.display.update()

run = True
#paddle(width, length, color, x, y)
left_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 0, 190)
ball = Pong_OBjects.ball(10, (255,255,255), 20, 250, 1)
right_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 688, 190)
left_score = 0
right_score = 0
num_hits = 0
while run:

    #set fps to 27
    clock.tick(27)
    #gets a list of all events that happened (key presses, mouse clicks, mouse moving, etc)
    for event in pygame.event.get():
    #quit the game if the x is pressed
        if event.type == pygame.QUIT:
            run = False
    
    #making ball go faster as point goes on
    if num_hits != 0 and num_hits % 10 == 0:
        ball.xvel += 1
        num_hits += 1
        #FIXME does not increase y velocity
    
    #figuring out which key is pressed and implementing movement
    keys = pygame.key.get_pressed()
    #right paddle control
    if keys[pygame.K_UP] and right_paddle.y > 0:
        right_paddle.y -= right_paddle.velocity
    elif keys[pygame.K_DOWN] and right_paddle.y < 380:
        right_paddle.y += right_paddle.velocity
    #left paddle control
    if keys[pygame.K_w] and left_paddle.y > 0:
        left_paddle.y -= left_paddle.velocity
    elif keys[pygame.K_s] and left_paddle.y < 380:
        left_paddle.y += left_paddle.velocity
    #serve the ball with space
    if keys[pygame.K_SPACE] and ball.served == False:
        ball.serve()

    #make ball move once it is served
    if ball.moving == True:
        ball.move()
    #keep ball on paddle if it is not served
    if ball.served == False and ball.facing > 0:
        ball.y = left_paddle.y + 60
    elif ball.served == False and ball.facing < 0:
        ball.y = right_paddle.y + 60
    
    #bounce off of top and bottom walls
    if ball.y >= 490:
        ball.yvel *= -1
        num_hits += 1
    elif ball.y <= 10:
        ball.yvel *= -1
        num_hits += 1
    
    #bouncing the ball off the right paddle
    if ball.facing > 0 and ball.y <= right_paddle.y + right_paddle.length and ball.y >= right_paddle.y:
        if ball.x >= 676 and ball.x <= 695:
            ball.bounce(right_paddle.y)
            ball.facing *= -1
            num_hits += 1
    #bounce the ball off the left paddle
    elif ball.facing < 0 and ball.y <= left_paddle.y + left_paddle.length and ball.y >= left_paddle.y:
        if ball.x >= 5 and ball.x <= 22:
            ball.bounce(left_paddle.y)
            ball.facing *= -1
            num_hits += 1

    #left paddle scores
    if ball.x >= 695:
        ball = Pong_OBjects.ball(10, (255,255,255), 680, 250, -1)
        left_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 0, 190)
        right_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 688, 190)
        ball.served = False
        ball.moving = False
        left_score += 1
        num_hits = 0
    #right paddle scores
    if ball.x <= 5:
        ball = Pong_OBjects.ball(10, (255,255,255), 20, 250, 1)
        left_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 0, 190)
        right_paddle = Pong_OBjects.paddle(12, 120, (255,255,255), 688, 190)
        ball.served = False
        ball.moving = False
        right_score += 1
        num_hits = 0

    if left_score == 10 or right_score == 10:
        run = False
    redraw_window()