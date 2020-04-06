import os
import pygame

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')
#文字颜色
TEXT_SCORE_COLOR = pygame.Color(255,222,220)

#击中小型飞机得分
SHOOT_SMALL_SCORE = 10

#游戏结果存储文件地址
PLAY_RESULTS_STORE_PATH = os.path.join(BASE_DIR,'store/results.txt')


# 我方飞机静态资源
OUR_PLANE_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
OUR_PLANE_IMG_2 = os.path.join(ASSETS_DIR, 'images/hero2.png')
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]

# 子弹图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')

# 子弹音效
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# 敌方小型飞机静态资源
SMALL_ENEMY_PLANE_IMG = os.path.join(ASSETS_DIR, 'images/enemy1.png')
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png'),
]
# 小型飞机坠毁音效
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')
