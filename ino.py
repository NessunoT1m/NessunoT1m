import pygame

class Ino(pygame.sprite.Sprite):
    """Класс одного пришельца"""

    def __init__(self, screen):
        """Инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ Выводим пришельца  на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает прищельцев"""
        self.y += 0.1
        self.rect.y = self.y