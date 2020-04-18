import new_bet
from cards import Hand, Deck
import pygame
from settings import Settings
import game_functions as gf


def game_over():
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")

    font = pygame.font.SysFont(None, 150)

    # create play button rect
    play_button = pygame.image.load('images/play.png')
    play_rect = play_button.get_rect()
    play_rect.topleft = ((475, 300))

    # set background
    bj_settings.screen.fill(bj_settings.bg_color)

    # display play button
    bj_settings.screen.blit(play_button, (475, 300))

    gf.add_text('GAME OVER', font, bj_settings.screen, 300, 100, bj_settings.BLACK)

    pygame.display.update()

    while True:
        # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    player = Hand()
                    dealer = Hand()
                    deck = Deck()
                    new_bet.take_bet(100, player, dealer, deck)
    """
    player = Hand()
    dealer = Hand()
    deck = Deck()
    new_bet.take_bet(100, player, dealer, deck)
    """