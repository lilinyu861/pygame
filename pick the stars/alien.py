import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星飞船图片
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 设置外星飞船初始位置
        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top
        # 保存外星飞船的x轴位置
        self.x = float(self.rect.x)
        # 设置外星飞船的移动标志
        self.moving_left = False
        self.moving_right = False

    def check_edge(self):
        # 当外星飞船碰到屏幕边界时，转换移动方向
        if self.rect.right >= self.screen_rect.right:
            self.ai_settings.alien_direction = -1
        elif self.rect.left <= self.screen_rect.left:
            self.ai_settings.alien_direction = 1

    def update(self):
        # 更新外星飞船位置
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.alien_direction)
        self.rect.x = self.x

    def left_alien(self):
        self.x = self.screen_rect.left

    def blitme(self):
        # 显示外星飞船的位置
        self.screen.blit(self.image, self.rect)