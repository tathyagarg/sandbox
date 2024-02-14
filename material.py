import pygame
import constants


class Material(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, color: tuple[int, int, int], gravity: bool = True):
        super().__init__()
        self.surface = pygame.Surface((constants.RENDER_SIZE, constants.RENDER_SIZE))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(
            center=(
                x, y
            )
        )

        self.gravity = gravity
        self.can_move = gravity

    def update(self, *args, **kwargs):
        if self.gravity:
            if self.rect.y < constants.HEIGHT:
                self.rect.move_ip(0, constants.GRAVITY)


class Concrete(Material):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, constants.COLORS.CONCRETE, False)
