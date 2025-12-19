import pygame
import sys
import random
import os
pygame.init()

def reset_game_state():
    global snake_pos, snake_body, direction, change_to, score, food_pos, food_spawn
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    food_pos = [random.randrange(1, (width // 10)) * 10,
                random.randrange(1, (height // 10)) * 10]
    food_spawn = True

def show_score(score):
    font=pygame.font.SysFont("arial",20)
    font2=pygame.font.SysFont("arial",20)
    show_high=font2.render(f'Highest Score : {highest_score}',True,(0,0,0))
    screen.blit(show_high,(100,10))
    score_surface=font.render(f'Score:{score}',True,(0,0,0))
    screen.blit(score_surface,(10,10))
    
def game_over(score,highest_score):
    os.system('afplay /System/Library/Sounds/Submarine.aiff')
    font=pygame.font.SysFont("arial",40)
    over_surface=font.render(f'Game Over!',True,(255,0,0))
    go_rect=over_surface.get_rect(center=(width//2,((height//2)-40)))
    screen.blit(over_surface,go_rect)
    
    font_small=pygame.font.SysFont("arial",25)
    restart_surface=font_small.render("Press R to Restart or Q to Quit",True,(0,0,0))
    restart_rect=restart_surface.get_rect(center=(width//2,((height//2)-10)))
    screen.blit(restart_surface,restart_rect)
    
    score_surface=font_small.render(f'Final Score = {score}, Highest Score={highest_score} ', True,(0,0,0))
    score_rect=score_surface.get_rect(center=(width//2,((height//2)+10)))
    screen.blit(score_surface,score_rect)
    pygame.display.update()
    
    #listen for R or Q key
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("key pressed:",event.key,event.unicode)
                    reset_game_state()
                    main()
                    waiting = False
                     #restart
                elif event.key==pygame.K_q:
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()
            


width,height=800,500
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game 🐍")

yellow=(255,255,0)  #colour

snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]]  #snake
snake_colour=(0,255,0)
snake_size=10
direction="RIGHT"
change_to = direction
speed=10





#food
food_pos=[random.randrange(1,(width//10))*10,random.randrange(1,(height//10))*10]
food_spawn=True
score=0
food_colour=(255, 0, 0)


highest_score=0
if score>highest_score:
    highest_score=score

def main():
    global direction,change_to,food_pos,food_spawn,score
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_UP and direction !="DOWN":
                     change_to="UP"
                 if event.key==pygame.K_DOWN and direction!= "UP":
                     change_to="DOWN"
                 if event.key==pygame.K_LEFT and direction != "RIGHT":
                     change_to="LEFT"
                 if event.key==pygame.K_RIGHT and direction != "LEFT":
                     change_to="RIGHT"
        direction=change_to
    
        if direction=="UP":
            snake_pos[1]-=10
        
        if direction=="DOWN":
            snake_pos[1] += 10
        if direction=="LEFT":
            snake_pos[0] -=10
        if direction=="RIGHT":
            snake_pos[0] += 10
    
        snake_body.insert(0,list(snake_pos))
    
         #wall collision
        if snake_pos[0]<0 or snake_pos[0]>=width or snake_pos[1]<0 or snake_pos[1]>=height:
            game_over(score,highest_score)
        
         #snake's head hit its own body
        for block in snake_body[1:]:
            if snake_pos[0]==block[0] and snake_pos[1]==block[1]:
                game_over(score,highest_score)
    
    
        #check if snake eats food
        if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
            score += 10
            os.system("afplay /System/Library/Sounds/Ping.aiff")
            food_spawn=False
        else:
            if len(snake_body)>1:
                snake_body.pop() #dont grow if no food eaten
        if not food_spawn:
            food_pos=[random.randrange(1,(width//10))*10,random.randrange(1,(height//10))*10]
        
        food_spawn=True
    
        screen.fill(yellow)
        for pos in snake_body:  #drawing part
            pygame.draw.rect(screen,snake_colour,pygame.Rect(pos[0],pos[1],snake_size,snake_size))
            
        pygame.draw.rect(screen,food_colour,pygame.Rect(food_pos[0],food_pos[1],snake_size,snake_size))

        show_score(score)
       
        pygame.display.update()
    
    
        pygame.time.Clock().tick(speed)#add a clock to control speed before game ends
    
    


main()




    

