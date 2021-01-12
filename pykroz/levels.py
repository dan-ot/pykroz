# Usable level bounds
from typing import List
from random import randrange
from time import sleep
import tcod
from tcod.tileset import CHARMAP_CP437

# Tiles
class Tiles:
    Block = CHARMAP_CP437[178]

# Constants
TOTOBJECTS = 83

XBOT = 1
XTOP = 64
YBOT = 1
YTOP = 23
YSIZE = YTOP - YBOT + 1 # 23 by default
XSIZE = XTOP - XBOT + 1 # 64 by default
TMAX = 9

GMOVE = False
PMOVE = True

# Unit-level State
class Level:
    # StrVal: str = ""
    Score: int = 0
    WhipPower: int = 0
    Level: int = 0
    Gems: int = 0
    Whips: int = 0
    Teleports: int = 0
    Keys: int = 0
    BC: int = 0
    BB: int = 0

# Types
class HSType:
    def __init__(self, name: str, highScore: int, highLevel: int):
        self.Name = name
        self.HighScore = highScore
        self.HighLevel = highLevel

class SaveType:
    def __init__(self, level: int, score: int, gems: int, whips: int, teleports: int, keys: int, whipPower: int, difficulty: int, px: int, py: int, foundSet: List[int], mixUp: bool):
        self.S_Level = level
        self.S_Score = score
        self.S_Gems = gems
        self.S_Whips = whips
        self.S_Teleports = teleports
        self.S_Keys = keys
        self.S_WhipPower = whipPower
        self.S_Difficulty = difficulty
        self.S_Px = px
        self.S_Py = py
        self.S_FoundSet = foundSet
        self.S_MixUp = mixUp

# Procedures
def Print(XPos: int, YPos: int, Message: str, fgColor: int, bgColor: int, console: tcod.Console):
    console.print(XPos - 1, YPos - 1, Message, color_of(fgColor), color_of(bgColor))

def PrintNum(YPos: int, Num: int, fgColor: int, bgColor: int, console: tcod.Console):
    # console.print(70, YPos, "       ")
    strVal = str(Num)
    if (YPos == 2 and Level.Score > 0):
        strVal += "0"
    if (YPos == 11):
        if (Level.WhipPower >= 3):
            strVal = strVal + "+" + str(Level.WhipPower)
    strVal = f"{strVal:^7}"
    console.print(69, YPos - 1, strVal, color_of(fgColor), color_of(bgColor))

def Update_Info(console: tcod.Console):
    Bak(7, 0, console)
    Col(4, 7, console)
    PrintNum(2, Level.Score, 4, 7, console)
    PrintNum(5, Level.Level, 4, 7, console)
    if Level.Gems > 9:
        PrintNum(8, Level.Gems, 7, 7, console)
    else:
        Col(7, 23, console)
        PrintNum(8, Level.Gems, 15, 4, console)
        Col(4, 7, console)
    PrintNum(11, Level.Whips, 4, 7, console)
    PrintNum(14, Level.Teleports, 4, 7, console)
    PrintNum(17, Level.Keys, 4, 7, console)
    Bak(0, 0, console)

def Border(console: tcod.Console):
    Level.BC = randrange(8, 15)
    Level.BB = randrange(1, 8)
    Col(Level.BC, 0, console)
    Bak(Level.BB, 7, console)
    for x in range(XBOT - 1, XTOP + 2):
        console.put_char(x, YTOP + 1, Tiles.Block)
        console.put_char(x, YBOT - 1, Tiles.Block)
    for y in range(YBOT - 1, YTOP + 2):
        console.put_char(XBOT - 1, y, Tiles.Block)
        console.put_char(XTOP + 1, y, Tiles.Block)
    Bak(0, 0, console)

def RestoreBorder(console: tcod.Console):
    Col(Level.BC, 0)
    Bak(Level.BB, 7)
    for x in range(XBOT - 1, XTOP + 2):
        console.put_char(x, YTOP + 1, Tiles.Block)
    Bak(0, 0)

def Flash(XPos: int, YPos: int, Message: str, console: tcod.Console):
    counter = 14
    keypressed = False
    while not keypressed:
        counter += 1
        if counter > 15:
            counter = 13
        Col(counter, 15)
        delay(20)
        console.print(XPos - 1, YPos - 1, Message)

def delay(ms: int):
    sleep(ms / 1000)

def color_of(color: int):
    if color == 0:
        return tcod.black
    elif color == 1:
        return tcod.blue
    elif color == 2:
        return tcod.green
    elif color == 3:
        return tcod.cyan
    elif color == 4:
        return tcod.red
    elif color == 5:
        return tcod.magenta
    elif color == 6:
        return tcod.amber
    elif color == 7:
        return tcod.light_gray
    elif color == 8:
        return tcod.dark_gray
    elif color == 9:
        return tcod.light_blue
    elif color == 10:
        return tcod.light_green
    elif color == 11:
        return tcod.light_cyan
    elif color == 12:
        return tcod.light_red
    elif color == 13:
        return tcod.light_magenta
    elif color == 14:
        return tcod.yellow
    elif color == 15:
        return tcod.white

def Col(color: int, _: int, console: tcod.Console):
    console.default_fg = color_of(color)

def Bak(color: int, _: int, console: tcod.Console):
    console.default_bg = color_of(color)