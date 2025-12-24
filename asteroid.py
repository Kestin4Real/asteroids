import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, deltaTime):
        self.position += self.velocity * deltaTime

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        log_event("asteroid_split")
        degrees = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(degrees) * 1.2
        velocity_2 = self.velocity.rotate(-degrees) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_2

