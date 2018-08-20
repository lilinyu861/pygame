class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    # 初始化在游戏运行期间可能变化的统计信息
    def reset_stats(self):
        self.score = 0
        self.high_score = 0
        self.level = 1