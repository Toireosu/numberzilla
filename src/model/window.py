import pygame
from pygame import *
from pygame.font import *

class Window:
    canvas: Surface = None
    exit: bool = False
    font: Font = None

    def __init__(self) -> None:
        pygame.init()
        self.canvas = pygame.display.set_mode((500, 500))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

        pygame.display.set_caption("Test")

    def clear(self) -> None:
        pygame.draw.rect(self.canvas, (0, 0, 0), (0, 0, 500, 500))

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def display(self) -> None:
        pygame.display.update()

    def render_text(self, text: str, x: float, y: float) -> None:
        textRender = self.font.render(text, False, (255, 255, 255), None)
        textRect = textRender.get_rect()
        textRect.center = (x, y)
        self.canvas.blit(textRender, textRect)