from typing import List
from KeyboardHandler import KeyboardHandler
from PipeHandler import PipeHandler
from Player import Player
from PlayerAI import PlayerAi
import pygame
import copy
import random

class AiHandler:
    def __init__(self, player_amount: int) -> None:
        self.ai_players: List[Player] = []
        self.last_deaths: List[Player] = [] # contains the death points 
        self.player_amount = player_amount
        self.generation = 0
        self.start_generation()

    def generate_mutated(self, genes: PlayerAi):
        player = Player(True)
        cpy_genes = copy.deepcopy(genes)
        cpy_genes.mutate()
        player.set_ai(cpy_genes)
        return player

    def start_generation(self, player_genes: List[PlayerAi] = None):
        if player_genes is None:
            for _ in range(self.player_amount):
                self.ai_players.append(Player(True))
        else:
            for _ in range(self.player_amount):
                player = self.generate_mutated(random.choice(player_genes))
                self.ai_players.append(player)
        self.generation += 1

    # returns true if a new generation is created    
    def update(self, delta_time: float, kb_handler: KeyboardHandler, pipe_handler: PipeHandler) -> bool:
        i = 0
        while i < len(self.ai_players):
            self.ai_players[i].update(delta_time, kb_handler, pipe_handler)
            if self.ai_players[i].is_dead(pipe_handler):
                self.last_deaths.append(self.ai_players[i])
                if len(self.last_deaths) > 3:
                    del self.last_deaths[0]
                # remove player from list
                del self.ai_players[i]
            i += 1

        if len(self.ai_players) == 0:
            genes = [player.player_ai for player in self.last_deaths]
            self.start_generation(genes)
            return True
    
    def render(self, screen: pygame.Surface):
        for player in self.ai_players:
            player.render(screen)
    
    def alive_ais(self) -> int:
        return len(self.ai_players)
    