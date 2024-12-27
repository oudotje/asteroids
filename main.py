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

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000
        player1.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
