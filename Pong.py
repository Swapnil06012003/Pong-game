import pygame
pygame.init()

#running variables
screen_width=900
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
bg=(0,0,15)
white=(255,255,255)
grey=(150,150,150)
clock=pygame.time.Clock()
run=True

#game objects
stick1=pygame.Rect(screen_width-30,screen_height/2-45,10,90)
stick2=pygame.Rect(20,screen_height/2-45,10,90)
ball=pygame.Rect(screen_width/2-7,screen_height/2-7,15,15)

#game variables
#easy=3,4
#normal=5,7,s2v=6.7

stick1_vel=0
stick2_vel=6.7
ball_xvel=7
ball_yvel=8
q=0

def gameloop():
    global run,stick1_vel,ball_xvel,ball_yvel,stick2_vel


    decrease_speed=pygame.USEREVENT
    pygame.time.set_timer(decrease_speed,15000)


    def move_stick2():
        if ball.centery-stick2.centery<0:
            stick2.centery-=stick2_vel
        if ball.centery-stick2.centery>0:
            stick2.centery+= stick2_vel

    def movement():
        stick1.centery += stick1_vel
        ball.centerx += ball_xvel
        ball.centery += ball_yvel
        if ball.left>screen_width+100:
            ball.centerx=screen_width/2-7
            ball.centery=screen_height/2-7

    #collision
    def collision():
        global ball_xvel,ball_yvel,q
        if stick1.top<2:
            stick1.top=2
        if stick1.bottom>screen_height-2:
            stick1.bottom=screen_height-2
        if stick2.top<2:
            stick2.top=2
        if stick2.bottom>screen_height-2:
            stick2.bottom=screen_height-2
        if ball.top < 2:
            ball_yvel*=-1
        if ball.bottom > screen_height - 2:
            ball_yvel*=-1
        if ball.colliderect(stick1):
            if ball.right-stick1.left<4:
                ball_xvel*=-1
                ball_yvel=stick1_vel
            else:
                ball_yvel*=-1
            q=1
        if ball.colliderect(stick2):
            ball_xvel*=-1
            ball_yvel=stick2_vel
            q=0
    #drawing
    def draw():
        screen.fill(bg)
        pygame.draw.line(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
        pygame.draw.line(screen,white,(0,1),(screen_width,1))
        pygame.draw.line(screen,white,(0,2),(screen_width,2))
        pygame.draw.line(screen,white,(0,screen_height-2),(screen_width,screen_height-2))
        pygame.draw.line(screen,white,(0,screen_height-1),(screen_width,screen_height-1))
        pygame.draw.rect(screen, grey, stick1)
        pygame.draw.rect(screen, grey, stick2)
        pygame.draw.ellipse(screen, white, ball)

    def game_manager():
        draw()
        collision()
        movement()
        if q == 1:
            move_stick2()
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    stick1_vel=-7
                if event.key==pygame.K_DOWN:
                    stick1_vel=7
            if event.type==decrease_speed:
                stick1_vel=abs(stick1_vel)-1
                stick2_vel=abs(stick2_vel)-1
        game_manager()
        clock.tick(60)
        pygame.display.update()
gameloop()