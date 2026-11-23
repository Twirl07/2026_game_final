import pygame

class Title():
    def __init__(self, x, y):
        #Make big words for title screen
        self.font_fn = r"orange juice 2.0.ttf"
        self.title_font = pygame.font.Font(self.font_fn, 100)
        self.title_surface = self.title_font.render("Welcome to Racer!" , 1, (100,100,255))
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (x,y-50)
        
        #Make smaller words for your title screen
        self.words_font = pygame.font.Font(self.font_fn, 40)
        self.words_surface = self.words_font.render("Click a map to race! GOODLUCK!!", 1, (100,100,255))
        self.words_rect = self.words_surface.get_rect()
        self.words_rect.center = (x, y+50)
        
        #make buttons for the map selection
        self.button_font = pygame.font.Font(self.font_fn, 40)
        
        #make rect for map1 button
        self.map1_button = pygame.Rect(0, 0, 250, 100)
        self.map1_button.center = (x/2, y*1.5)
        
        #make rect for map2 button
        self.map2_button = pygame.Rect(0,0,250,100)
        self.map2_button.center = (x*1.5, y*1.5)
        
        #make the words for the buttons
        self.map1_label = self.button_font.render("Map 1!", 1, (100,100,255))
        self.map2_label = self.button_font.render("Map 2!", 1, (100,100,255))
        
    def draw_button(self, screen, rect, label, mouse_pos):
        #draws a full rect of blue when hovering
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (220,220,255), rect, border_radius=12)
        #black outline for the button
        pygame.draw.rect(screen, (0,0,0), rect, 4, border_radius=12)
        screen.blit(label, label.get_rect(center=rect.center))
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.words_surface, self.words_rect)
        self.draw_button(screen, self.map1_button, self.map1_label, mouse_pos)
        self.draw_button(screen, self.map2_button, self.map2_label, mouse_pos)
        
    def get_click(self, pos):
        if self.map1_button.collidepoint(pos):
            return 1
        elif self.map2_button.collidepoint(pos):
            return 2
        return 0
    
class End():
    def __init__(self, x, y):
        #Make words for end screen
        self.font_fn = r"orange juice 2.0.ttf"
        self.x = x
        self.y = y
        self.end_font = pygame.font.Font(self.font_fn, 100)
        self.end_surface = self.end_font.render("Amazing race!" , 1, (100,100,255))
        self.end_rect = self.end_surface.get_rect()
        self.end_rect.center = (self.x, self.y-50)
        
        self.words_font = pygame.font.Font(self.font_fn, 40)
        self.words_surface = self.words_font.render("Click the X above and reload to race again!", 1, (100,100,255))
        self.words_rect = self.words_surface.get_rect()
        self.words_rect.center = (x, y+115)
        
        #play again button
        self.button_font = pygame.font.Font(self.font_fn, 40)
        self.again_button = pygame.Rect(0,0,300,100)
        self.again_button.center = (x, y+200)
        self.again_label = self.button_font.render("Play again!", 1, (100,100,255))
        
    def race_time(self, race_time):
        self.time_surface = self.end_font.render("Time: " + str(float(race_time)) + "seconds", 1, (100,100,255))
        self.time_rect = self.time_surface.get_rect()
        self.time_rect.center = (self.x, self.y+50)
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(self.end_surface, self.end_rect)
        screen.blit(self.time_surface, self.time_rect)
        screen.blit(self.words_surface, self.words_rect)
        
        if self.again_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (220,220,255), self.again_button, border_radius=12)
        #black outline for the button
        pygame.draw.rect(screen, (0,0,0), self.again_button, 4, border_radius=12)
        screen.blit(self.again_label, self.again_label.get_rect(center=self.again_button.center))
        
    def get_click(self, pos):
        if self.again_button.collidepoint(pos):
            return 1
        return 0
        
        