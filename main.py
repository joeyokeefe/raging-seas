import pygame
import os

WIDTH, HEIGHT = 720,480

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raging Seas")

#Colors
BLUE = (0, 140, 210)

#Setting game FPS
FPS = 60

#Importing character sprite
ADMIRAL_FISHPARK = pygame.image.load(os.path.join('Assets', 'Admiral_Fishpark.png'))

#Fills game window with background color
def draw_window():
    WIN.fill(BLUE)
    WIN.blit(ADMIRAL_FISHPARK, (360, 240))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        #caps framerate at 60FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            #Quits game when user closes window
            if event.type == pygame.QUIT:
                run = False

        #Updates game window background color
        draw_window()
        

    pygame.quit()

if __name__ == "__main__":
    main()