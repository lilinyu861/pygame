import pygame
import random


class Stars():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载星星图片
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 设置星星的位置
        self.rect.x = random.randint(60, 1140)
        self.rect.y = random.randint(160, 540)

    def update(self):
        # 更新星星的位置
        self.rect.x = random.randint(60, 1140)
        self.rect.y = random.randint(160, 540)

    def blitme(self):
        # 显示星星
        self.screen.blit(self.image, self.rect)