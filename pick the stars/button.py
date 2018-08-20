import pygame.sysfont


class Button():
    def __init__(self, ai_setting, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # 设置按钮的大小、颜色和按钮中文字的颜色、大小和字体
        self.width, self.height = 200, 50
        self.button_color = (105, 105, 105)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 设置按钮的位置
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 设置按钮中的文字
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)