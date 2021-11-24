import pygame
import sys
from rocket import Rocket


class Game(object):
    def __init__(self):
        # Config Game
        self.tps_max = 80.0

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_detla = 0.0

        self.player = Rocket(self)

        while True:
            # Handle event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_detla += self.tps_clock.tick()/1000.0
            while self.tps_detla > 1/self.tps_max:
                self.tick()
                self.tps_detla -= 1/self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()
