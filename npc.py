import pygame
import math

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, waypoints, car_fp, max_speed = 3.7):
        pygame.sprite.Sprite.__init__(self)
        #make npc image
        self.car_fp = car_fp
        car = pygame.image.load(self.car_fp)
        self.car_og = pygame.transform.rotozoom(car,0,0.5)
        self.car_surface = self.car_og
        self.rect = self.car_surface.get_rect()
        self.rect.center = (x,y)
        
        #make movement same as player with no controls
        self.x =x
        self.y =y
        self.angle = 0
        self.speed = 0
        self.max_speed = max_speed
        self.accel = 0.1
        self.turn_speed =4
        
        #make waypoints for the car to follow in order to stay on track
        self.waypoints = waypoints
        #which target to go to, how far the target needs to be for it to want to go to it, how close it is when it reaches ti
        self.target = 0
        self.reach = 40
        self.finished = 0
        
    def update(self):
        #stop racing if you lose
        if self.finished == 1:
            return
        #find distnace to waypoint
        target_x, target_y = self.waypoints[self.target]
        dx = target_x - self.x
        dy = target_y - self.y
        
        #find hypotenuse (found in youtube video, part of original pygame math docs)
        distance = math.hypot(dx, dy)
        
        #move to next waypoint
        if distance < self.reach:
            self.target += 1
            if self.target >= len(self.waypoints):
                self.finished = 1
                return
            target_x, target_y = self.waypoints[self.target]
            dx = target_x - self.x
            dy = target_y - self.y
            
            
        #find the angle that the car needs to go in order to stay on the track to the next waypoint
        wanted_angle = math.degrees(math.atan2(-dx, -dy))
        turn = (wanted_angle - self.angle + 180) % 360 -180
        
        #make the turns look smoothe while it stays on the track
        if turn > self.turn_speed:
            turn = self.turn_speed
        if turn < -self.turn_speed:
            turn = -self.turn_speed
        self.angle += turn
        
        if self.speed < self.max_speed:
            self.speed += self.accel
            
        #go the rifht way
        rad = math.radians(self.angle)
        self.x += -math.sin(rad) * self.speed
        self.y += -math.cos(rad) * self.speed
        
        
        #move the car
        self.car_surface = pygame.transform.rotate(self.car_og, self.angle)
        self.rect = self.car_surface.get_rect()
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.car_surface, self.rect)
    
        