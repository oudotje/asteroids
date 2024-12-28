import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20.0, 50.0)
        new_asteroid1_velocity = self.velocity.rotate(spawn_angle)
        new_asteroid2_velocity = self.velocity.rotate(-spawn_angle)
        new_asteroids_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
        new_asteroid1.velocity = new_asteroid1_velocity * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
        new_asteroid2.velocity = new_asteroid2_velocity * 1.2
