import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    def __init__(self, ai_settings, screen, alien):
        super(Bullets, self).__init__()
        self.screen = screen
        # 初始化子弹的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        # 保存子弹的y轴位置
        self.y = float(self.rect.y)
        # 设置子弹的颜色和运动速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 更新子弹的位置
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)

