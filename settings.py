__author__ = 'Kalmar'

IP = ???
PORT = 8080
PIN = ???
MY_NR = ???
HP = 200
DEBUG = False
THICKNESS = 2
BULLET_SIZE = 2
AMMO = 200
MAP_SIZE = 700
FPS = 60
BLOCK_SIZE = 15
GUN_SIZE = 1.9
FOOTER_SIZE = 20
BLOCK_SPEED = 1.0 * MAP_SIZE / FPS
BULLET_SPEED = 1.5 * BLOCK_SPEED
BLOCK_ACCELERATION = 1.0 * BLOCK_SPEED / FPS * 2
GUN_RESOLUTION = 1.0 * BLOCK_SIZE / MAP_SIZE * 2

colors = dict(BLACK="\x1b[30m",
              RED="\x1b[31m",
              GREEN="\x1b[32m",
              YELLOW="\x1b[33m",
              BLUE="\x1b[34m",
              PURPLE="\x1b[35m",
              CYAN="\x1b[36m",
              RESET="\x1b[0m",
)


def color(txt, txt_color):
    try:
        return colors[txt_color.upper()] + txt + colors['RESET']
    except KeyError:
        return txt
