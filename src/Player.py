import pygame
from KeyboardHandler import KeyboardHandler
from Pipe import Pipe
from PlayerAI import PlayerAi
from constants import PIPE_WIDTH, PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPAWN_X, WINDOW_GEOMETRY
from PipeHandler import PipeHandler

class Player:
    x: float
    y: float
    dy: float
    using_ai: bool # if the ai should be active
    player_ai: PlayerAi
    def __init__(self, using_ai: bool) -> None:
        self.x = PLAYER_SPAWN_X
        self.y = WINDOW_GEOMETRY[1]/2-PLAYER_SIZE
        self.dy = 0
        self.using_ai = using_ai
        self.player_ai = PlayerAi()
    
    def set_ai(self, new_ai: PlayerAi):
        self.player_ai = new_ai

    def update(self, delta_time: float, kb_handler: KeyboardHandler, pipe_handler: PipeHandler):
        self.dy += 5
        self.y += self.dy * delta_time

        if self.using_ai:
            if self.execute_ai(pipe_handler):
                self.jump()
        elif kb_handler.was_released(pygame.K_SPACE): # if space was just released
            self.jump()  
            

    def jump(self):
        self.dy = -1000

    # gets the next pipe, ie the pipe that comes after the pipe that is behind the player
    def get_next_pipe(self, pipe_handler: PipeHandler) -> Pipe:
        next_pipe = pipe_handler.pipes[0] # default value
       
        for i, pipe in enumerate(pipe_handler.pipes):
            if pipe.x-PIPE_WIDTH < self.x+PLAYER_SIZE:
                next_pipe = pipe_handler.pipes[i]

        return next_pipe

    # returns true if the player is touching a pipe
    def is_dead(self, pipe_handler: PipeHandler) -> bool:

        next_pipe = self.get_next_pipe(pipe_handler)
        player_at_pipe = self.x+PLAYER_SIZE >= next_pipe.x and self.x <= next_pipe.x+PIPE_WIDTH
        player_not_at_hole = self.y <= next_pipe.hole_y or self.y+PLAYER_SIZE > next_pipe.hole_y2
        # the player dies if:
        # if the player is at the pipe but not at the hole at the same time 
        # then the player is touching the pipe meaning that hes dead
        # or when the player goes outside the screen
        return (player_at_pipe and player_not_at_hole) or self.y < 0 or self.y+PLAYER_SIZE > WINDOW_GEOMETRY[1]

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
        
    def execute_ai(self, pipe_handler: PipeHandler) -> bool:
        next_pipe: Pipe = self.get_next_pipe(pipe_handler)
        y = self.y
        x_distance_pipe = next_pipe.x-self.x
        y_distance_top_pipe = next_pipe.hole_y-self.y
        y_distance_bottom_pipe = next_pipe.hole_y2-self.y
        speed = self.dy
        return self.player_ai.output(y, y_distance_bottom_pipe, y_distance_top_pipe, x_distance_pipe, speed)
        