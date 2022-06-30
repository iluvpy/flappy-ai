from typing import List
from Pipe import Pipe
import pygame
import time

from constants import PIPE_SPAWN_INTERVAL


"""
adds a new pipe every PIPE_SPAWN_INTERVAL
and removes pipes that need to despawn (pipes that moved out of the screen)
"""
class PipeHandler:
    def __init__(self) -> None:
        self.pipes: List[Pipe] = []
        self.last_pipe_added = 0
        self.add_pipe()

    def add_pipe(self):
        self.pipes.append(Pipe())
        self.last_pipe_added = time.perf_counter()
        print("added pipe")

    def update(self, delta_time: float):
        i = 0
        for pipe in self.pipes:
            pipe.update(delta_time)
            if pipe.should_despawn():
                del self.pipes[i]
            i += 1
        now = time.perf_counter()
        if now-self.last_pipe_added >= PIPE_SPAWN_INTERVAL:
            self.add_pipe()
            
        
    def render(self, screen: pygame.Surface):
        for pipe in self.pipes:
            pipe.render(screen)