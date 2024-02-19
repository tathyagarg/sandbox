import pygame
import constants
import material
from itertools import combinations

pygame.init()
screen = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])

frame = pygame.image.load("assets/frame_white.png").convert()

running = True
dragging = False

materials = []

render_material = material.Concrete


def render():
    x, y = pygame.mouse.get_pos()
    obj = render_material(x, y)
    materials.append(obj)


while running:
    x, y = -1, -1
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            x, y = event.pos
            render()
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging: render()

    # Collision checker
    for (mat1, mat2) in combinations(materials, 2):
        if mat1 == mat2: pass
        if mat1.gravity ^ mat2.gravity:
            if mat1.rect.colliderect(mat2.rect):
                upper, lower = (mat2, mat1) if mat2.rect.y > mat1.rect.y else (mat1, mat2)
                upper.can_move = False

    for mat in materials:
        mat.update()
        screen.blit(mat.surface, mat.rect)

    screen.blit(frame, (10, 10))
    if x != -1 and y != -1:
        if frame.get_rect().collidepoint(x, y):
            print("switching")
            render_material = material.Concrete if isinstance(render_material(-1, -1), material.Sand) else material.Sand
            print(f"{render_material.__name__}")

    pygame.display.flip()

pygame.quit()
