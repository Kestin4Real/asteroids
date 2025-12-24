import sys
import pygame
from logger import log_state, log_event

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from music import Music
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    deltaTime = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0)
    asteroidfield = AsteroidField()
    music = Music()
    
    while True:
        log_state()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Logic
        updatable.update(deltaTime)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
                    break
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                #sys.exit()

        # Draw
        screen.fill("black")
        for drwbl in drawable:
            drwbl.draw(screen)
        
        pygame.display.flip()
        deltaTime = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
