import pygame
import constants


class PlayRest():
    __score = 0  # 总分
    __life = 3  # 生命数
    __blood = 1000  # 生命值

    @property
    def score(self):
        """单词游戏分数"""
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            return None
        self.__score = value

    def save_history(self):
        """记录最高分"""
        # 1.读取文件中存储的分数
        # 2.如果新分数比文件分数大，则保存新分数
        # 3.如果新分数比文件分数小，则不保存
        # 4.存储分数，不是追加而是替换模式
        if int(self.get_max_score()) < self.score:
            with open(constants.PLAY_RESULTS_STORE_PATH, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_score(self):
        rest = 0
        with open(constants.PLAY_RESULTS_STORE_PATH, 'r') as f:
            r = f.read()
            if r:
                rest = r
            return rest
