
def add_text(text, font, surface, x, y, text_color):
    """

    :param text:
    :param font:
    :param surface:
    :param x:
    :param y:
    :param text_color:
    :return:
    """
    textobject = font.render(text, 1, text_color)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect)