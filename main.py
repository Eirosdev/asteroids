#!usr/bin/python3
import pygame
from constants import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    game_fps = 60
    game_dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        game_dt = game_clock.tick(game_fps)/1000


if __name__ == "__main__":
    main()