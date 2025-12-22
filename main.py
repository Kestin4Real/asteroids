import pygame
from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

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
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0)

    while True:
        log_state()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Logic
        updatable.update(deltaTime)

        # Draw
        screen.fill("black")
        for drwbl in drawable:
            drwbl.draw(screen)
        
        pygame.display.flip()
        deltaTime = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
