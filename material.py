import string

import pygame
import constants
import random


class Material(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, color: tuple[int, int, int], name: str, gravity: bool = True):
        super().__init__()
        self.surface = pygame.Surface((constants.RENDER_SIZE, constants.RENDER_SIZE))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(
            center=(
                x, y
            )
        )

        self.name = name

        self.gravity = gravity
        self.can_move = gravity
        self.id = "".join(random.choices(string.printable, k=20))

    def update(self, *args, **kwargs):
        if self.gravity and self.can_move:
            if self.rect.y < constants.HEIGHT:
                self.rect.move_ip(0, constants.GRAVITY)

    def __eq__(self, other):
        return self.id == other.id


class Concrete(Material):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, constants.COLORS.CONCRETE, "Concrete", False)


class Sand(Material):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, constants.COLORS.SAND, "Sand", True)
