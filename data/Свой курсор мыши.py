import os
import sys
import random
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"'{fullname}'")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


bomb_image = load_image("bomb.png")
all_sprites = pygame.sprite.Group()
bomb = pygame.sprite.Sprite(all_sprites)
bomb.image = bomb_image
bomb.rect = bomb.image.get_rect()
pygame.mouse.set_visible(False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            bomb.rect.topleft = event.pos
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
