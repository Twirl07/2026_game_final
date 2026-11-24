import pygame
from background import Background1, Background2
from title import Title, End, Countdown
from player import Player
from npc import NPC
import math
pygame.init()

TS = 64
HEIGHT = 11 * TS
WIDTH = 14 * TS
SIZE = (WIDTH, HEIGHT)

#make screen
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

bgt = pygame.Surface(SIZE)
bgt.fill((255,255,255))
title = Title(WIDTH/2, HEIGHT/2)
end = End(WIDTH/2, HEIGHT/2)
countdown = Countdown(WIDTH/2, HEIGHT/2)

bg_size = ((14 * TS, 11 * TS))
bg1 = Background1(bg_size, TS)
bg1.make_bg()

bg2 = Background2(bg_size, TS)
bg2.make_bg()

#add a big loop in order to keep playing
playing = 1
while playing:
    chosen = 0
    #make title loop
    running =1
    while running:
        screen.blit(bgt,(0,0))
        title.draw(screen)
        pygame.display.flip()
        events = pygame.event.get()
        #Check for events to see if game quit/  map selection
        for e in events:
            if e.type == pygame.QUIT:
                running = 0
                playing = 0
            if e.type == pygame.MOUSEBUTTONDOWN:
                #calls the get_click method in order to return a certain map
                chosen = title.get_click(e.pos)
                if chosen != 0:
                    running = 0
                    
    if chosen != 0:
        running = 1
    else:
        running = 0

    #pick which map 
    if chosen == 1:
        bg = bg1
    else:
        bg = bg2

    player = Player(1.5 * TS -14, 10.5 * TS)
    npc = NPC(1.5 * TS + 14, 10.5 * TS, bg.waypoints, r"kenney_racing-pack\PNG\Cars\car_red_1.png", 3.7)
    npc2 = NPC(1.5 * TS, 10.6 * TS, bg.waypoints, r"kenney_racing-pack\PNG\Cars\car_green_1.png", 3.9)
    player_won = 0

    def touching(player, grass):
        return player.hitbox.colliderect(grass.rect)
    
    
    counting = running
    countdown.start()
    while counting:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                counting = 0
                running = 0
                playing = 0
        
        bg.draw(screen)
        npc.draw(screen)
        npc2.draw(screen)
        player.draw(screen)
        countdown.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        
        if countdown.done():
            counting = 0
            

    #start timer
    start_time = pygame.time.get_ticks()
    finished = 0

    pygame.mixer.init()
    vroom = pygame.mixer.Sound('f1.mp3')

    #main game loop
    while running:
        #play car sound
        if not pygame.mixer.get_busy():
            vroom.play()
        #takes the return and puts the map in the main game loop
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = 0
                playing = 0
                
        keys = pygame.key.get_pressed()
        
        #use sprite groups to see if a small center of the car and grass are touching in order for it to not slow while on track
        on_grass = len(pygame.sprite.spritecollide(player, bg.grass_group, False, touching)) > 0
        
        #call the player update
        player.update(keys, on_grass)
        
        #call npc update
        npc.update()
        npc2.update()
        
        #check to see if the car finished the race
        if chosen == 1:
            if player.y > HEIGHT and 4 * TS < player.x < 5 * TS:
                finished = 1
        else:
            if player.y < 0 and 12 * TS < player.x < 14 * TS:
                finished = 1
                
        if finished == 0 and (npc.finished == 1 or npc2.finished==1):
            finished = 1
            player_won = 0
        elif finished == 1:
            player_won = 1
                    
        if finished == 1:
            race_time = (pygame.time.get_ticks() - start_time) / 1000
            vroom.stop()
            running = 0
        
        bg.draw(screen)
        npc.draw(screen)
        npc2.draw(screen)
        player.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
              
    #End screen
    if finished == 1:
        running = 1
        end.race_time(race_time)
        end.results(player_won)
    else:
        running = 0
        
    #End screen loop
    while running:
        screen.blit(bgt, (0,0))
        end.draw(screen)
        pygame.display.flip()
        if e.type == pygame.MOUSEBUTTONDOWN:
            #calls the get_click method in order to return a certain map
            chosen = end.get_click(e.pos)
            if chosen != 0:
                running = 0
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = 0
                playing = 0
            
pygame.quit()



