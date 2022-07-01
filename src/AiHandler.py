from typing import List
from KeyboardHandler import KeyboardHandler
from PipeHandler import PipeHandler
from Player import Player
from PlayerAI import PlayerAi
import pygame
import copy

class DeathPoint:
    player_ai: PlayerAi # the player ai that died
    death_x: float # x position at player death
    def __init__(self, player: Player) -> None:
        self.death_x = player.x
        self.player_ai = player.player_ai

    def __gt__(self, other):
        return self.death_x > other.death_x
    
    def __lt__(self, other):
        return self.death_x < other.death_x

class AiHandler:
    def __init__(self, player_amount: int) -> None:
        self.ai_players: List[Player] = []
        self.death_points: List[DeathPoint] = [] # contains the death points 
        self.player_amount = player_amount
        self.generation = 0
        self.start_generation()

    def generate_mutated(self, genes: PlayerAi):
        player = Player(True)
        cpy_genes = copy.deepcopy(genes)
        cpy_genes.mutate()
        player.set_ai(cpy_genes)
        return player

    def start_generation(self, player_genes: PlayerAi = None):
        if player_genes is None:
            for _ in range(self.player_amount):
                self.ai_players.append(Player(True))
        else:
            for _ in range(self.player_amount):
                player = self.generate_mutated(player_genes)
                self.ai_players.append(player)
        self.generation += 1

    # returns true if a new generation is created    
    def update(self, delta_time: float, kb_handler: KeyboardHandler, pipe_handler: PipeHandler) -> bool:
        i = 0
        while i < len(self.ai_players):
            self.ai_players[i].update(delta_time, kb_handler, pipe_handler)
            if self.ai_players[i].is_dead(pipe_handler):
                self.death_points.append(DeathPoint(self.ai_players[i]))
                del self.ai_players[i]
            i += 1

        if len(self.ai_players) == 0:
            sorted_ai_players: List[DeathPoint] = sorted(self.death_points)
            first = sorted_ai_players[0]
            self.start_generation(first.player_ai)
            return True
        print(len(self.ai_players))
    
    def render(self, screen: pygame.Surface):
        for player in self.ai_players:
            player.render(screen)
            

if __name__ == "__main__":
    # testing
    p1 = Player(False)
    p1.x = 2
    dp1 = DeathPoint(p1)
    p2 = Player(False)
    p2.x = 3
    dp2 = DeathPoint(p2)
    print(dp1 > dp2)