import pygame
from constants import *

class GameScore():

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.score_text = self.font.render(f"Score: {self.score}", True, "white")
        self.score_rect = self.score_text.get_rect(topleft=(10, 10))
        self.score_end_screen_rect = self.score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    def update(self, points):
        self.score += points
        self.score_text = self.font.render(f"Score: {self.score}", True, "white")

    def draw(self, game_over):
        if game_over == False:
            self.screen.blit(self.score_text, self.score_rect)
        else:
            self.screen.blit(self.score_text, self.score_end_screen_rect)