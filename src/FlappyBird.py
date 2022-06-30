import pygame
from Pipe import Pipe
import time
from PipeHandler import PipeHandler
from constants import WINDOW_GEOMETRY
pygame.init()

# flappy bird program/window
class FlappyBird:
    running = True
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(WINDOW_GEOMETRY)
        pygame.display.set_caption("Flappy Bird")
        self.pipe_handler = PipeHandler()
        self.delta_time = 0

    # registers events
    def update(self):
        start_time = time.perf_counter()
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.pipe_handler.update(self.delta_time)

        end_time = time.perf_counter()
        self.delta_time = end_time-start_time
        
    # renders everything on screen
    def render(self):
        self.screen.fill((84, 86, 89))
        self.pipe_handler.render(self.screen)
        pygame.display.flip()

    def is_running(self):
        return self.running