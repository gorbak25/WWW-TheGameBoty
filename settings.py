__author__ = 'Kalmar'

IP = "192.168.88.218"
PORT = 8080
PIN = 0x527b1a79
MY_NR = 10
HP = 200
DEBUG = False
THICKNESS = 2
BULLET_SIZE = 2
AMMO = 200
MAP_SIZE = 700
FPS = 30
BLOCK_SIZE = 15
GUN_SIZE = 1.9
FOOTER_SIZE = 20
BLOCK_SPEED = 1.0 * MAP_SIZE / 70
BULLET_SPEED = 1.5 * BLOCK_SPEED
BLOCK_ACCELERATION = 1.0 * BLOCK_SPEED / 70 * 2
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
