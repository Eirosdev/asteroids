#!usr/bin/python3
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    game_fps = 60
    game_dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #spawn player in the middle of the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        game_dt = game_clock.tick(game_fps)/1000


if __name__ == "__main__":
    main()