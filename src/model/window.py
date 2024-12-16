import pygame
from pygame import *

class Window:
    canvas: Surface = None
    exit: bool = False

    def __init__(self) -> None:
        pygame.init()
        self.canvas = pygame.display.set_mode((500, 500))

        pygame.display.set_caption("Test")

    def clear(self) -> None:
        pygame.draw.rect(self.canvas, (255, 255, 255), (0, 0, 500, 500))

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def display(self) -> None:
        pygame.display.update()