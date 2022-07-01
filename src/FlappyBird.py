import pygame
from AiHandler import AiHandler
from KeyboardHandler import KeyboardHandler
from Pipe import Pipe
import time
from PipeHandler import PipeHandler
from Player import Player
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
        self.ai_handler = AiHandler(1000)
        self.kb_handler = KeyboardHandler()
    
        

    # handles events
    def update(self):
        start_time = time.perf_counter()
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.kb_handler.press(event.key)
            if event.type == pygame.KEYUP:
                self.kb_handler.release(event.key)

   
        self.kb_handler.update()
        self.pipe_handler.update(self.delta_time)
        if self.ai_handler.update(self.delta_time, self.kb_handler, self.pipe_handler):
            self.pipe_handler.clean()
        end_time = time.perf_counter()   
        self.delta_time = end_time-start_time
        
    # renders everything on screen
    def render(self):
        self.screen.fill((84, 86, 89))
        self.pipe_handler.render(self.screen)
        self.ai_handler.render(self.screen)
        pygame.display.flip()

    def is_running(self):
        return self.running
    
   