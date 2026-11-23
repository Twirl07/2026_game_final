import pygame
import math
ts = 64

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #make the image of the car
        self.car_fp = r"kenney_racing-pack\PNG\Cars\car_blue_1.png"
        car = pygame.image.load(self.car_fp)
        self.car_og = pygame.transform.rotozoom(car,0,0.5)
        self.car_surface = self.car_og
        self.rect = self.car_surface.get_rect()
        self.rect.center = (x,y)
        
        self.hitbox = pygame.Rect(0,0,10,10)
        self.hitbox.center = (x,y)
        self.grass_max = 2
        
        #make your position for your car + speeds
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 4
        self.accel = 0.2
        self.friction = 0.05
        self.turn_speed = 4
        
    def update(self, keys, on_grass):
        #make the car not get lost in space and bounce off the wall so it does not get stuck
        if self.x <= 0:
            self.speed = 0
            self.x = 5
        if self.x >= 14 * ts:
            self.speed = 0
            self.x = 14 * ts - 5
        #do the same for the top/bottom wall but make the finish lines be okay
        if self.y <= 0 and self.x != 14 * ts:
            self.speed = 0
            self.y = 5
        if self.y >= 11 * ts and self.x != 5 * ts:
            self.speed = 0
            self.y = 11 * ts - 5
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed += self.accel
        elif keys[pygame.K_DOWN]:
            self.speed -= self.accel
        else:
            if self.speed > 0:
                self.speed -= self.friction
                
        #Make a speed limit so the car doesnt start going to fast that it cannot be controlled
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if 0 > self.speed < -self.max_speed:
            self.speed = -self.max_speed
            
        #make the grass group work with the player
        if on_grass:
            if self.speed > self.grass_max:
                self.speed -= 0.3
                
        #turn while the car is moving
        if self.speed != 0:
            if keys[pygame.K_LEFT]:
                self.angle += self.turn_speed
            if keys[pygame.K_RIGHT]:
                self.angle -= self.turn_speed
                
        #move the correct direction
        rad = math.radians(self.angle)
        self.x += -math.sin(rad) * self.speed
        self.y += -math.cos(rad) * self.speed
        
        #move og car and rect
        self.car_surface = pygame.transform.rotate(self.car_og, self.angle)
        self.rect = self.car_surface.get_rect()
        self.rect.center = (self.x, self.y)
        self.hitbox.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.car_surface, self.rect)
        
        
        