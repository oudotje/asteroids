import pygame
from constants import *
import player
import asteroid
import asteroidfield
import sys

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    player.Shot.containers = (updatable, drawable, shots)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroid_field = asteroidfield.AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000
        for u in updatable:
            u.update(dt)
            print(f"{player1.shot_timer}")
        for a in asteroids:
            if a.check_collisions(player1):
                print("Game over!")
                sys.exit()
        for d in drawable: 
            d.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
