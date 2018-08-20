
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 人的速度
        self.people_speed_factor = 1

        # 外星飞船的移动
        self.alien_speed_factor = 0.5
        self.alien_direction = 1

        # 子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)

        # 记分
        self.star_points = 10
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.people_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        # 记分
        self.star_points = 10