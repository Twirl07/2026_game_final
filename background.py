import pygame

class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, ts):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, ts, ts)

class Background1():
    def __init__(self, size, ts):
        #make all the file paths 
        start_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt79.png"
        up_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt01.png"
        side_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt02.png"
        right_up_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt03.png"
        right_down_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt05.png"
        end_fp = r"kenney_racing-pack\PNG\Tiles\Asphalt road\road_asphalt42.png"
        grass_fp = r"kenney_racing-pack\PNG\Tiles\Grass\land_grass11.png"
        
        #turn the file paths into images 
        start = self.load(start_fp, ts)
        end = self.load(end_fp, ts)
        up = self.load(up_fp, ts)
        side = self.load(side_fp, ts)
        right_up = self.load(right_up_fp, ts)
        right_down = self.load(right_down_fp, ts)
        left_down = self.load(right_down_fp, ts, 270)
        left_up = self.load(right_up_fp, ts, 90)
        grass = self.load(grass_fp, ts)
            
        self.size = size
        self.ts = ts
        self.grass = grass
        
        #make the matrix for what the map should look like
        self.tile_matrix = [
                [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
                [grass, right_up, side, side, side, side, side, side, side, side, side, side, right_down, grass],
                [grass, up, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, up, grass],
                [grass, up, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, up, grass],
                [grass, up, grass, grass, right_up, side, side, side, side, side, side, side, left_down, grass],
                [grass, up, grass, grass, up, grass, grass, grass, grass, grass, grass, grass, grass, grass],
                [grass, up, grass, grass, up, grass, grass, grass, grass, grass, grass, grass, grass, grass],
                [grass, up, grass, grass, left_up, side, side, side, side, side, side, side, right_down, grass],
                [grass, start, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, up, grass],
                [grass, start, grass, grass, right_up, side, side, side, side, side, side, side, left_down,grass],
                [grass, start, grass, grass, end, grass, grass, grass, grass, grass, grass, grass, grass, grass]
            ]
        
        #make a group for the grass sprite in order to slow car while it is in the grass
        self.grass_group = pygame.sprite.Group()
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                if self.tile_matrix[r][c] is grass:
                    self.grass_group.add(Grass(c*ts, r*ts, ts))
                    
        #make the path for the waypoints in oreder to keep npc on the road
        path = [(1,1), (12,1), (12,4), (4,4), (4,7), (12,7), (12,9), (4,9), (4,12)]
        self.waypoints = []
        for c, r in path:
            self.waypoints.append(((c + 0.5) * ts, (r + 0.5) * ts))
            
                        
    #function that works like rotozoom
    def load(self, fp, ts, angle=0):
        #change pixel size to match in order to have clean edges
        img = pygame.image.load(fp).convert_alpha()
        #blend pixels in to the tile next to it for clean look
        img = pygame.transform.smoothscale(img, (ts, ts))
        #rotates the tile if you give an angle 
        if angle:
            img = pygame.transform.rotate(img, angle)
        return img
    
    def make_bg(self):
        self.bg = pygame.Surface(self.size)
        
        for y in range(0, self.size[1], self.ts):
            for x in range(0, self.size[0], self.ts):
                self.bg.blit(self.grass, (x, y))
        
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                self.bg.blit(self.tile_matrix[r][c], (c*self.ts, r*self.ts))
                
        self.rect = self.bg.get_rect()      
        return self.bg
    
    def draw(self, screen):
        screen.blit(self.bg, self.rect)
        
        
        
class Background2():
    def __init__(self, size, ts):
        start_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt78.png"
        up_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt90.png"
        side_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt01.png"
        right_up_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt02.png"
        right_down_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt04.png"
        end_fp = r"kenney_racing-pack\PNG\Tiles\Dirt road\road_dirt41.png"
        grass_fp = r"kenney_racing-pack\PNG\Tiles\Grass\land_grass11.png"
        
        start = self.load(start_fp, ts)
        end = self.load(end_fp, ts)
        up = self.load(up_fp, ts)
        side = self.load(side_fp, ts)
        right_up = self.load(right_up_fp, ts)
        right_down = self.load(right_down_fp, ts)
        left_down = self.load(right_down_fp, ts, 270)
        left_up = self.load(right_up_fp, ts, 90)
        grass = self.load(grass_fp, ts)
            
        self.size = size
        self.ts = ts
        self.grass = grass
        
        self.tile_matrix = [
                [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,end,grass],
                [grass, right_up,side,side,side,side,side,side,side,side,side,side,left_down,grass],
                [grass,up,grass, grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                [grass,left_up,side,side,side,side,side,side,side,side,side,side,right_down,grass],
                [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,up,grass],
                [grass,right_up,side,side,side,side,side,side,side,side,side,side,left_down,grass],
                [grass, up, grass,grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass,],
                [grass, left_up, side, side,side,side,side,side,side,side,side,side,right_down,grass],
                [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,up,grass],
                [grass,right_up,side,side,side,side,side,side,side,side,side,side,left_down,grass],
                [grass,start, grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass]
            ]
        
        #make a group for the grass sprite in order to slow car while it is in the grass
        self.grass_group = pygame.sprite.Group()
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                if self.tile_matrix[r][c] is grass:
                    self.grass_group.add(Grass(c*ts, r*ts, ts))
                    
        #make path for map two
        path = [(1,9), (12,9), (12,7), (1,7), (1,5), (12,5), (12,3), (1,3), (1,1), (12,1), (12,-2)]
        self.waypoints = []
        for c, r in path:
            self.waypoints.append(((c + 0.5) * ts, (r + 0.5) * ts))

    
    
    
    def load(self, fp, ts, angle=0):
        img = pygame.image.load(fp).convert_alpha()
        img = pygame.transform.smoothscale(img, (ts, ts))
        if angle:
            img = pygame.transform.rotate(img, angle)
        return img
    
    def make_bg(self):
        self.bg = pygame.Surface(self.size)
        
        for y in range(0, self.size[1], self.ts):
            for x in range(0, self.size[0], self.ts):
                self.bg.blit(self.grass, (x, y))
        
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                self.bg.blit(self.tile_matrix[r][c], (c*self.ts, r*self.ts))
                
        self.rect = self.bg.get_rect()      
        return self.bg
    
    def draw(self, screen):
        screen.blit(self.bg, self.rect)
        
        

                             
                    