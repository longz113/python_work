
class Gamestats():
    def __init__(self,ai_set):
        #初始化统计信息
        self.ai_set=ai_set
        self.reset_stats()
        #让游戏一开始处于非活跃状态
        self.game_active=False

    def reset_stats(self):
        self.ship_left=self.ai_set.ship_limit
