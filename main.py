import pygame
import os

WIDTH, HEIGHT = 1280,720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raging Seas")

#Colors
BLUE = (0, 140, 210)

#Setting game FPS
FPS = 60
#Set velocity
VELOCITY = 5

#Importing sprites
ADMIRAL_FISHPARK = pygame.image.load(os.path.join('Assets', 'Admiral_Fishpark.png'))
BOAT = pygame.image.load(os.path.join('Assets', 'boat.png'))

#Fills game window with background color
def draw_window(admiral):
    WIN.fill(BLUE)
    WIN.blit(BOAT, (250, 250))
    WIN.blit(ADMIRAL_FISHPARK, (admiral.x, admiral.y))
    pygame.display.update()

def admiral_movement(keys_pressed, admiral):
    if keys_pressed[pygame.K_UP]:
        admiral.y -= VELOCITY
    elif keys_pressed[pygame.K_DOWN]:
        admiral.y += VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        admiral.x += VELOCITY
    elif keys_pressed[pygame.K_LEFT]:
        admiral.x -= VELOCITY

def main():
    admiral = pygame.Rect(0, 0, 32, 32)
    clock = pygame.time.Clock()
    run = True
    while run:
        #caps framerate at 60FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            #Quits game when user closes window
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        admiral_movement(keys_pressed, admiral)
        #Updates game window background color
        draw_window(admiral)
        
        

    pygame.quit()

if __name__ == "__main__":
    main()