#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import MENU_OPTIONS, COLOR_WHITE, COLOR_PURPLE, WIN_WIDTH, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/terrace.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_colour: tuple, text_center_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont('Arial Black', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_colour).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer.music.load('./asset/MusicaMenu.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 100, text= 'Ghost Runner', text_colour=COLOR_BLACK, text_center_pos=((WIN_WIDTH/ 2), 400))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(text_size= 50, text= MENU_OPTIONS[i], text_colour=COLOR_PURPLE, text_center_pos=((WIN_WIDTH/ 2), 500 + 80 * i ))

            pygame.display.flip()

        # Check for all events (checar todos os eventos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window (fechar a janela do jogo)
                    quit() #end pygame (encerrar)


