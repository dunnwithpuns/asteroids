import pygame, random

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # set specs for the new asteroids
        angle = random.uniform(20, 50)
        pos_vector = self.velocity.rotate(angle)
        neg_vector = self.velocity.rotate((angle * -1))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create new asteroids
        pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        # increase velocity
        pos_asteroid.velocity = pos_vector * 1.2
        neg_asteroid.velocity = neg_vector * 1.2

