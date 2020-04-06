import pygame
import constants
from game import war


class Bullet(pygame.sprite.Sprite):
    """子弹类"""

    # 子弹状态
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.screen = screen
        # 速度
        self.speed = speed
        self.plane = plane

        # 加载子弹图片
        self.image = pygame.image.load(constants.BULLET_IMG)

        # 获取子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        # 发射音效
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def update(self, war):
        """更新子弹位置"""
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        # 绘制子弹
        self.screen.blit(self.image, self.rect)
        # 检测子弹是否碰到敌机
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        for r in rest:
            # 子弹消失
            self.kill()
            # 飞机爆炸，坠毁效果
            r.broken_down()
            # 统计游戏成绩
            war.rest.score += constants.SHOOT_SMALL_SCORE
            # 保存历史记录
            war.rest.save_history()
