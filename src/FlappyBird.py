import pygame
from AiHandler import AiHandler
from KeyboardHandler import KeyboardHandler
import time
from PipeHandler import PipeHandler
from constants import BLACK, WINDOW_GEOMETRY
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
        self.default_font = pygame.font.SysFont("helvetica", 16)
        self.speed_multiplier = 1

    # handles events
    def update(self):
        start_time = time.perf_counter()
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.kb_handler.press(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: 
                    if self.speed_multiplier < 10:
                        self.speed_multiplier += 1
                if event.button == 5: 
                    if self.speed_multiplier >= 2:
                        self.speed_multiplier += -1

       
        for _ in range(self.speed_multiplier):
            self.kb_handler.update()
            self.pipe_handler.update(self.delta_time)
            if self.ai_handler.update(self.delta_time, self.kb_handler, self.pipe_handler):
                self.pipe_handler.clean()
            

        end_time = time.perf_counter()   
        self.delta_time = (end_time-start_time)
        
    # renders everything on screen
    def render(self):
        self.screen.fill((84, 86, 89))
        self.pipe_handler.render(self.screen)
        self.ai_handler.render(self.screen)
        self.draw_data()
        pygame.display.flip()
    
    def draw_data(self):
        generation_text = self.default_font.render(f"generation: {self.ai_handler.generation}", True, BLACK)
        alive_text = self.default_font.render(f"alive: {self.ai_handler.alive_ais()}", True, BLACK)
        speed_text = self.default_font.render(f"speed: x{self.speed_multiplier}", True, BLACK)
        self.screen.blit(generation_text, (20, 20))
        self.screen.blit(alive_text, (20, 50))
        self.screen.blit(speed_text, (20, 80))

    def is_running(self):
        return self.running
    
   
