#!usr/bin/python3
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    game_fps = 60
    game_dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #spawn player in the middle of the screen
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update
        for obj in updateable:
            obj.update(game_dt)

        #check player-asteroid collision
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        #draw
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        game_dt = game_clock.tick(game_fps)/1000


if __name__ == "__main__":
    main()