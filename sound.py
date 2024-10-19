import pygame

class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'sound/'
        self.swing = pygame.mixer.Sound(self.path + 'Swing.mp3')
