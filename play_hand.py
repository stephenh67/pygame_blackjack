from settings import Settings
import pygame
import sys
import game_functions as gf
import time


def play_hand(bet, chips, player, dealer, deck):
    """Play hand

    :param bet: amount of the bet
    :param chips: players total chips
    :param player: player hand
    :param dealer: dealer hand
    :param deck: the deck of cards
    :return: None
    """
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")
    bj_settings.screen.fill(bj_settings.GREEN)

    font = pygame.font.SysFont(None, 50)

    # text setting for chips
    gf.add_text(('Chips: ' + str(chips - bet)), font, bj_settings.screen, 100, 30, bj_settings.BLACK)

    # text setting for bet
    gf.add_text(('Bet: ' + str(bet)), font, bj_settings.screen, 600, 30, bj_settings.BLACK)

    pcardx, pcardy = (600, 100)

    # Load the card images into the game.
    for card in player.cards:
        pic = pygame.image.load('images/' + str(card) + '.png')
        bj_settings.screen.blit(pic, (pcardx, pcardy))
        pcardx += 75


    # hit and stand buttons
    hit_button = pygame.image.load('images/hit_button.png')
    hit_rect = hit_button.get_rect()
    hit_rect.topleft = ((600, 500))
    bj_settings.screen.blit(hit_button, (600, 500))

    stand_button = pygame.image.load('images/stand_button.png')
    stand_rect = stand_button.get_rect()
    stand_rect.topleft = ((850, 500))
    bj_settings.screen.blit(stand_button, (850, 500))

    next_hand_button = pygame.image.load('images/next_hand_button.png')
    next_hand_rect = next_hand_button.get_rect()
    next_hand_rect.topleft = ((850, 600))
    bj_settings.screen.blit(next_hand_button, (850, 600))
    


    # load dealer cards
    dcardx, dcardy = (100, 100)
    dcard1 = pygame.image.load('images/' + str(dealer.cards[0]) + '.png')
    dcard2 = pygame.image.load('images/' + str(dealer.cards[1]) + '.png')
    dcard_back = pygame.image.load('images/back.png')

    # draw dealer cards
    bj_settings.screen.blit(dcard1, (dcardx, dcardy))
    bj_settings.screen.blit(dcard_back, (dcardx + 75, dcardy))

    pygame.display.update()

    blackjack = False
    double_prize = False
    dealer_bust = False
    player_bust = False

    # for testing blackjack

    # check if player has blackjack
    if player.value == 21:
        # blackjack text

        # add blackjack image
        blackjack = pygame.image.load('images/blackjack.png')
        blackjack_rect = blackjack.get_rect()
        blackjack_rect.topleft = ((150, 420))
        bj_settings.screen.blit(blackjack, (150, 420))

        pygame.display.update()
        blackjack = True
        double_prize = True

    # dealer has natual 21 and player doesnt
    if dealer.value == 21 and player.value != 21:

        dealer_blackjack = pygame.image.load('images/dealer_blackjack.png')
        dealer_blackjack_rect = dealer_blackjack.get_rect()
        dealer_blackjack_rect.topleft = ((150, 420))
        bj_settings.screen.blit(dealer_blackjack, (150, 420))

        bj_settings.screen.blit(dcard2, (dcardx + 75, dcardy))
        pygame.display.update()
        blackjack = True

    stand = False
    hand_done = False
    player_wins = False
    dealer_wins = False
    push = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hit_rect.collidepoint(event.pos) and player.value < 22 and player.value != 21 and stand is False:
                    player.add_card(deck.deal())
                    bj_settings.screen.blit(pygame.image.load('images/' + str(player.cards[-1]) + '.png'),
                                            (pcardx, pcardy))
                    pcardx += 75
                    pygame.display.update()

                    if player.value > 21:

                        # display bust image
                        bust = pygame.image.load('images/bust.png')
                        bust_rect = bust.get_rect()
                        bust_rect.topleft = ((150, 420))
                        bj_settings.screen.blit(bust, (150, 420))

                        pygame.display.update()
                        player_bust = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if stand_rect.collidepoint(event.pos) and player.value < 22 and blackjack is False and stand is False:
                    dcardx += 75
                    bj_settings.screen.blit(pygame.image.load('images/' + str(dealer.cards[1]) + '.png'),
                                            (dcardx, dcardy))
                    pygame.display.update()
                    stand = True

                    # Win conditions
                    while dealer.value < 17 and stand is True and hand_done is False:

                        time.sleep(1)
                        dcardx += 75
                        dealer.add_card(deck.deal())
                        bj_settings.screen.blit(pygame.image.load('images/' + str(dealer.cards[-1]) + '.png'), (
                            dcardx, dcardy))
                        pygame.display.update()

                        if dealer.value > 21:

                            dealer_bust = pygame.image.load('images/dealer_bust.png')
                            dealer_bust_rect = dealer_bust.get_rect()
                            dealer_bust_rect.topleft = ((150, 420))
                            bj_settings.screen.blit(dealer_bust, (150, 420))

                            pygame.display.update()
                            dealer_bust = True

                    if dealer.value >= 17:
                        pygame.display.update()
                        hand_done = True

                    if dealer_bust is False and stand is True and player_bust is False \
                            and blackjack is False and hand_done is True:
                        if dealer.value <= 21 and player.value <= 21:
                            if player.value > dealer.value:

                                # add blackjack image
                                you_win = pygame.image.load('images/you_win.png')
                                you_win_rect = you_win.get_rect()
                                you_win_rect.topleft = ((150, 420))
                                bj_settings.screen.blit(you_win, (150, 420))

                                pygame.display.update()
                                player_wins = True
                            if player.value < dealer.value:

                                dealer_wins = pygame.image.load('images/dealer_wins.png')
                                dealer_wins_rect = dealer_wins.get_rect()
                                dealer_wins_rect.topleft = ((150, 420))
                                bj_settings.screen.blit(dealer_wins, (150, 420))

                                pygame.display.update()
                                dealer_wins = True
                            if player.value == dealer.value:

                                push = pygame.image.load('images/push.png')
                                push_rect = push.get_rect()
                                push_rect.topleft = ((150, 420))
                                bj_settings.screen.blit(push, (150, 420))

                                pygame.display.update()
                                push = True

            if event.type == pygame.MOUSEBUTTONUP:
                # check if player has blackjack
                if player.value == 21:
                    # blackjack text

                    # add blackjack image
                    blackjack = pygame.image.load('images/blackjack.png')
                    blackjack_rect = blackjack.get_rect()
                    blackjack_rect.topleft = ((150, 420))
                    bj_settings.screen.blit(blackjack, (150, 420))

                    pygame.display.update()
                    blackjack = True
                    double_prize = True

            # Game logic to allow to allow button presses on keyboard.
            if event.type == pygame.MOUSEBUTTONUP and double_prize is True:
                if next_hand_rect.collidepoint(event.pos):

                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet * 2
            if event.type == pygame.MOUSEBUTTONUP and dealer.value == 21 or event.type == pygame.MOUSEBUTTONUP and \
                    player.value > 21 or event.type == pygame.MOUSEBUTTONUP and dealer_wins is True:
                if next_hand_rect.collidepoint(event.pos):
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return -bet
            if event.type == pygame.MOUSEBUTTONUP and dealer.value > 21 or event.type == pygame.MOUSEBUTTONUP and \
                    player_wins is True:
                if next_hand_rect.collidepoint(event.pos):
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet
            if event.type == pygame.MOUSEBUTTONUP and push is True:
                if next_hand_rect.collidepoint(event.pos):
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return 0
