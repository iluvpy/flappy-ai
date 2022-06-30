from re import X
import pip
import pygame
from KeyboardHandler import KeyboardHandler
from constants import PIPE_WIDTH, PLAYER_COLOR, PLAYER_WEIGHT, PLAYER_SIZE, PLAYER_SPAWN_X, WINDOW_GEOMETRY
from PipeHandler import PipeHandler

class Player:
    x: float
    y: float
    dy: float
    def __init__(self) -> None:
        self.x = PLAYER_SPAWN_X
        self.y = WINDOW_GEOMETRY[1]/2-PLAYER_SIZE
        self.dy = 0

    def update(self, delta_time: float, kb_handler: KeyboardHandler):
        self.dy += 1
        self.y += self.dy * PLAYER_WEIGHT * delta_time
        if kb_handler.was_released(pygame.K_SPACE): # if space was just released
            self.dy -= 200
            print("released")

    # returns true if the player is touching a pipe
    def is_dead(self, pipe_handler: PipeHandler):
        # the next pipe, ie the pipe that comes after the pipe that is behind the player
        next_pipe = None
        for i, pipe in enumerate(pipe_handler.pipes):
            if pipe.x-PIPE_WIDTH < self.x:
                next_pipe = pipe_handler.pipes[i]

        return self.x >= next_pipe.x and (self.y > next_pipe.hole_y or self.y < next_pipe.hole_y2)  

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))