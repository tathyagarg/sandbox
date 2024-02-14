import pygame
import constants
import material
from material import Concrete

pygame.init()
screen = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])

running = True
dragging = False

materials = pygame.sprite.Group()
gui = pygame.sprite.Group()


def render():
    x, y = pygame.mouse.get_pos()
    obj = material.Concrete(x, y)
    materials.add(obj)


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            render()
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging: render()

    for mat in materials:
        mat.update()
        screen.blit(mat.surface, mat.rect)

    for gui_obj in gui:
        screen.blit(gui_obj.surface, gui_obj.rect)

    pygame.display.flip()

pygame.quit()
