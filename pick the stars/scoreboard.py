import pygame.sysfont


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color=(30, 30, 30)
        self.font = pygame.font.SysFont(None, 32)

        # 准备初始得分图像
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render("Score: "+score_str, True, self.text_color, self.ai_settings.bg_color)
        # 将得分放在屏幕右下角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
