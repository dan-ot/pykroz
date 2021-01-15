# Usable level bounds
from tiles import Tiles
from crt import Crt
from typing import List
from random import randint, randrange
from time import sleep
import sounds

class GameTiles:
    Block = Tiles.Code[178]

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
    def __init__(self):
    # StrVal: str = ""
        self.Score: int = 0
        self.WhipPower: int = 0
        self.Level: int = 0
        self.Gems: int = 0
        self.Whips: int = 0
        self.Teleports: int = 0
        self.Keys: int = 0
        self.Bc: int = 0
        self.Bb: int = 0

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
def Print(XPos: int, YPos: int, Message: str, console: Crt):
    console.write(XPos - 1, YPos - 1, Message)

def PrintNum(YPos: int, Num: int, level: Level, console: Crt):
    # console.write(70, YPos, "       ")
    strVal = str(Num)
    if (YPos == 2 and level.Score > 0):
        strVal += "0"
    if (YPos == 11):
        if (level.WhipPower >= 3):
            strVal = strVal + "+" + str(level.WhipPower)
    strVal = f"{strVal:^7}"
    console.write(69, YPos - 1, strVal)

def Update_Info(level: Level, console: Crt):
    Bak(7, 0, console)
    Col(4, 7, console)
    PrintNum(2, level.Score, 4, 7, console)
    PrintNum(5, level.Level, 4, 7, console)
    if level.Gems > 9:
        PrintNum(8, level.Gems, 7, 7, console)
    else:
        Col(7, 23, console)
        PrintNum(8, level.Gems, 15, 4, console)
        Col(4, 7, console)
    PrintNum(11, level.Whips, 4, 7, console)
    PrintNum(14, level.Teleports, 4, 7, console)
    PrintNum(17, level.Keys, 4, 7, console)
    Bak(0, 0, console)

def Border(level: Level, console: Crt):
    level.Bc = randrange(8, 15)
    level.Bb = randrange(1, 8)
    Col(level.Bc, 0, console)
    Bak(level.Bb, 7, console)
    for x in range(XBOT - 1, XTOP + 2):
        console.gotoxy(x, 25)
        console.write(GameTiles.Block)
        console.gotoxy(x, 1)
        console.write(GameTiles.Block)
    for y in range(YBOT - 1, YTOP + 2):
        console.gotoxy(1, y)
        console.write(GameTiles.Block)
        console.gotoxy(66, y)
        console.write(GameTiles.Block)
    Bak(0, 0, console)

def RestoreBorder(level: Level, console: Crt):
    console.gotoxy(2, 25)
    Col(level.Bc, 0)
    Bak(level.Bb, 7)
    for x in range(XBOT - 1, XTOP + 2):
        console.write(GameTiles.Block)
    Bak(0, 0)

def Flash(XPos: int, YPos: int, Message: str, level: Level, console: Crt):
    counter = 14
    ClearKeys(console)
    while not console.keypressed():
        counter += 1
        if counter > 15:
            counter = 13
        Col(counter, 15)
        delay(20)
        Print(XPos, YPos, Message, console)
    RestoreBorder(level, console)

def ClearKeys(console: Crt):
    console.keyboard.clear()

def FootStep(console: Crt):
    console.sounds(sounds.FootStep())

def GrabSound(console: Crt):
    console.sounds(sounds.GrabSound())

def BlockSound(console: Crt):
    console.sounds(sounds.BlockSound())

def NoneSound(console: Crt):
    console.sounds(sounds.NoneSound())

def Static(console: Crt):
    console.sounds(sounds.Static())

def delay(ms: int):
    sleep(ms / 1000)

def Col(color: int, _: int, console: Crt):
    console.textcolor(color)

def Bak(color: int, _: int, console: Crt):
    console.textbackground(color)