import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, deltaTime):
        if self.shoot_cooldown > 0: self.shoot_cooldown -= deltaTime
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-deltaTime)

        if keys[pygame.K_d]:
            self.rotate(deltaTime)

        if keys[pygame.K_z]:
            self.move(deltaTime)

        if keys[pygame.K_s]:
            self.move(-deltaTime)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, deltaTime):
        self.rotation += PLAYER_TURN_SPEED * deltaTime

    def move(self, deltaTime):
        up_vector = pygame.Vector2(0, 1)
        forward_vector = up_vector.rotate(self.rotation)
        move_vector = forward_vector * PLAYER_SPEED * deltaTime
        self.position += move_vector
    
    def shoot(self):
        if self.shoot_cooldown > 0: return

        shot = Shot(self.position.x, self.position.y)
        up_vector = pygame.Vector2(0, 1)
        forward_vector = up_vector.rotate(self.rotation)
        shot.velocity = forward_vector * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
