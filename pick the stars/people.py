import pygame
from pygame.sprite import Sprite


class People(Sprite):
    def __init__(self, ai_settings, screen):
        super(People, self).__init__()
        self.screen = screen
        # 加载人的图片
        self.image = pygame.image.load('images/people.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        # 设置摘星人的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 存储摘星人的x，y轴位置
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        # 设置摘星人移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # 移动摘星人的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.people_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.people_speed_factor
        elif self.moving_up and self.rect.bottom > 126:
            self.bottom -= self.ai_settings.people_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.people_speed_factor

        # 更新摘星人的位置
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def center_people(self):
            # 让人在屏幕中居中
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

    def blitme(self):
        # 显示摘星人的位置
        self.screen.blit(self.image, self.rect)