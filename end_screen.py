import pygame
from logger import *
from constants import *

class EndScreen:
    def __init__(self, screen):
        self.screen = screen
        self.end_text_font = pygame.font.Font(None, 120)
        self.restart_text_font = pygame.font.Font(None, 48)
        self.end_text = self.end_text_font.render("Game Over", True, "white")
        self.restart_text = self.restart_text_font.render("Press ANY KEY to Return to Start Screen", True, "white")
        self.end_rect = self.end_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.restart_rect = self.restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.end_text, self.end_rect)
        self.screen.blit(self.restart_text, self.restart_rect)