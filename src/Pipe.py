import random
from turtle import update
import pygame
from constants import PIPE_COLOR, PIPE_HOLE_SIZE, SPEED, PIPE_WIDTH, WINDOW_GEOMETRY

class Pipe:
    x: float
    hole_y: float # start of the hole in the pipe
    hole_y2: float # end of the hole in pipe
    def __init__(self) -> None:
        self.x = WINDOW_GEOMETRY[0]
        self.hole_y = random.uniform(0, WINDOW_GEOMETRY[1]-PIPE_HOLE_SIZE)
        self.hole_y2 = self.hole_y+PIPE_HOLE_SIZE

    def render(self, screen: pygame.Surface):
        rect1 = (self.x, 0, PIPE_WIDTH, self.hole_y)
        rect2 = (self.x, self.hole_y2, PIPE_WIDTH, WINDOW_GEOMETRY[1]-self.hole_y2)
        pygame.draw.rect(screen, PIPE_COLOR, rect1)
        pygame.draw.rect(screen, PIPE_COLOR, rect2)
    
    def update(self, delta_time: float):
        self.x -= delta_time * SPEED
    
    def should_despawn(self) -> bool:
        return self.x+PIPE_WIDTH < 0