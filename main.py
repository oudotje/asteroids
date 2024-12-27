import pygame
from constants import *
import player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player1)
    drawable.add(player1)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000
        for u in updatable:
            u.update(dt)
        for d in drawable: 
            d.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
