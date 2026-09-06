import pygame
from logger import *
from constants import *

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 100)
        self.start_text_font = pygame.font.Font(None, 48)
        self.title_text = self.title_font.render("Asteroids", True, "white")
        self.start_text = self.start_text_font.render("Press ANY KEY to Start", True, "white")
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    
    def draw(self):
        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.start_text, self.start_rect)