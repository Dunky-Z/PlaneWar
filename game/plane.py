import random

import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """飞机的基类"""

    # 飞机图片
    plane_img = []
    # 飞机爆炸图片
    destroy_img = []
    # 坠毁音乐
    down_sound_src = None
    # 飞机状态: True/活的，False/死的
    active = True
    # 飞机发射的子弹
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        # 加载静态资源
        self.screen = screen
        self.img_list = []
        self.__destroy_img_list = []
        self.down_sound = None
        self.load_src()

        # 飞机速度
        self.speed = speed or 10
        # 飞机的位置
        self.rect = self.img_list[0].get_rect()
        # 飞机的宽度与高度
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        self.width, self.height = self.screen.get_size()
        # 改变飞机初始化位置
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height / 2)

    def load_src(self):
        """加载静态资源"""
        # 飞机图片
        for img in self.plane_img:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁图片
        for img in self.destroy_img:
            self.__destroy_img_list.append(pygame.image.load(img))
        # 坠毁音乐
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """"飞机上移动"""
        self.rect.top -= self.speed

    def move_down(self):
        """飞机下移动"""
        self.rect.top += self.speed

    def move_left(self):
        """飞机左移动"""
        self.rect.left -= self.speed

    def move_right(self):
        """飞机右移动"""
        self.rect.right += self.speed

    def broken_down(self):
        """飞机坠毁"""
        # 1. 播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()
        # 2. 播放坠毁动画
        for img in self.__destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3. 坠毁后
        self.active = False

    def shot(self):
        """飞机发射子弹"""
        bullet = Bullet(self.screen, self, 10)
        self.bullets.add(bullet)


class OurPlane(Plane):
    # 飞机图片
    plane_img = [constants.OUR_PLANE_IMG_1, constants.OUR_PLANE_IMG_2]
    # 飞机爆炸图片
    destroy_img = constants.OUR_DESTROY_IMG_LIST
    # 坠毁音乐
    down_sound_src = None

    def update(self, war):
        """ 更新飞机的动画效果 """
        self.move(war.key_down)
        # 1. 切换飞机的动画效果，喷气式效果
        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        # 飞机撞击检测
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            # 1. 游戏结束
            war.status = war.OVER
            # 2. 敌方飞机清除
            war.enemies.empty()
            war.small_enemies.empty()
            # 3. 我方飞机坠毁效果
            self.broken_down()
            # 4. 记录游戏成绩

    def move(self, key):
        """ 飞机移动自动控制 """
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        """ 向上移动，超出范围之后，拉回来 """
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top >= self.height - self.plane_h:
            self.rect.top = self.height - self.plane_h

    def move_left(self):
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left >= self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w


class SmallEnemyPlane(Plane):
    # 飞机图片
    plane_img = [constants.SMALL_ENEMY_PLANE_IMG]
    # 飞机爆炸图片
    destroy_img = constants.SMALL_ENEMY_DESTROY_IMG_LIST

    # 坠毁音乐
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        # 每次生成一架飞机时，随机出现在屏幕
        # 屏幕宽度-飞机宽度
        self.init_pos()

    def update(self, *args):
        """更细飞机移动"""
        super().move_down()

        # 绘制敌机
        self.blit_me()

        # 超出范围
        if self.rect.top >= self.height:
            self.active = False
            # self.kill()
            self.reset()
        # 多线程

    # 改变飞机的初始位置
    def init_pos(self):
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-5 * self.plane_h, -self.plane_h)

    def reset(self):
        # 重置飞机的状态
        self.active = True
        self.init_pos()

    def broken_down(self):
        # 重写
        super().broken_down()
        # 飞机重复使用
        self.reset()
