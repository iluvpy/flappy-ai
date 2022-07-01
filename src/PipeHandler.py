from tkinter.tix import WINDOW
from typing import List
from Pipe import Pipe
import pygame
import time

from constants import PIPE_DISTANCE, WINDOW_GEOMETRY


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
                print("removed pipe")
            i += 1
        # create a new pipe if the last created one is at least PIPE_DISTANCE away from the right window border
        if self.pipes[-1].x <= WINDOW_GEOMETRY[0]-PIPE_DISTANCE: 
            self.add_pipe()
            
        
    def render(self, screen: pygame.Surface):
        for pipe in self.pipes:
            pipe.render(screen)

    def clean(self):
        self.pipes = []
        self.add_pipe()