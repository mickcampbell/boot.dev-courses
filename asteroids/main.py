import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.draw(screen)

    AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if object.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    object.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = pygame.time.Clock().tick(60) / 1000



if __name__ == "__main__":
    main()
