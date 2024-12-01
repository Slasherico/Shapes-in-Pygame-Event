import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("Grey")
pygame.display.update()

class Circle():
    def __init__(self, size, color, spawnpos, bordersize):
        self.circsize = size
        self.circcolor = color
        self.circspawn = spawnpos
        self.circborder = bordersize
        self.circsurface = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circsurface, self.circcolor, self.circspawn, self.circsize, self.circborder)
    
    def grow(self, r):
        self.circsize = self.circsize+r
        self.draw_circle = pygame.draw.circle(self.circsurface, self.circcolor, self.circspawn, self.circsize, self.circborder)





circ = Circle(50, (0,0,255), (100,100), 0)
circ.draw()



pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
