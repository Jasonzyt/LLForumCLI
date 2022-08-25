class Style:
    DEFAULT = 0
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    ANTI_WHITE = 7


class Color:
    DEFAULT = 39
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37
    LIGHT_BLACK = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    LIGHT_WHITE = 97


class BgColor:
    DEFAULT = 49
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47
    LIGHT_BLACK = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN = 106
    LIGHT_WHITE = 107


def color(fg=None, bg=None, style=None):
    fg_color = fg if fg else Color.DEFAULT
    bg_color = bg if bg else BgColor.DEFAULT
    style_color = style if style else Style.DEFAULT
    return '\033[{};{};{}m'.format(style_color, fg_color, bg_color)


LIGHT_YELLOW = color(Color.LIGHT_YELLOW)
LIGHT_BLUE = color(Color.LIGHT_BLUE)
LIGHT_CYAN = color(Color.LIGHT_CYAN)

ITALIC = color(style=Style.ITALIC)
RESET = color()
