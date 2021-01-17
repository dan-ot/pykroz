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
    for _ in range(XBOT - 1, XTOP + 2):
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
        console.delay(20)
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

def Col(color: int, _: int, console: Crt):
    console.textcolor(color)

def Bak(color: int, _: int, console: Crt):
    console.textbackground(color)

def Sign_Off(console: Crt):
    Shareware(console, Wait = False)
    ClearKeys(console)
    Col(7, 7, console)
    Bak(0, 0, console)
    console.clrscr()
    console.gotoxy(31, 2)
    console.write('DUNGEONS OF KROZ II')
    console.gotoxy(26, 3)
    console.writeln('An Apogee Software Production')
    console.writeln()
    console.writeln('Other great games available from Scott Miller:')
    console.writeln()
    Col(15, 15, console)
    console.write(254); console.writeln(' The six Kroz games! CAVERNS OF KROZ, KINGDOM OF KROZ, DUNGEONS OF KROZ,')
    console.writeln('     RETURN TO KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.')
    console.writeln('     Each volume is just $7.50, or order all six for $35!')
    console.writeln()
    Col(7, 7, console)
    console.write(254); console.writeln(' SUPERNOVA - Explore a galaxy and save a planet from an exploding star!')
    console.writeln('     An epic adventure rated by Shareware Magazine as one of the best games')
    console.writeln('     ever! Highly advanced game has graphics, sound effects galore, clue')
    console.writeln('     command, and dozens of unique features. ($10)')
    console.writeln()
    console.write(254); console.writeln(' BEYOND THE TITANIC - A fantastic adventure of exploration and survival.')
    console.writeln('     What really happened? Sound effects and 16 color screens.  ($8)')
    console.writeln()
    console.write(254); console.writeln(' WORD WHIZ - New game that challenges your knowledge of the English')
    console.writeln('     language.  Fun to play, yet very education, too.  ($5)')
    console.writeln()
    Col(15, 15, console)
    console.write(254); console.writeln(' THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best')
    console.write  ('     levels yet!  Built-in contest!  New features galore.  ($20)')
    Col(7, 7, console)
    ClearKeys(console)
    console.halt()

def Shareware(console: Crt, Wait: bool):
    Bak(1, 0, console)
    console.clrscr()
    Col(15, 15, console)
    console.gotoxy(22, 1)
    console.write('CAVERNS OF KROZ '); console.write(196); console.writeln(' HOW TO REGISTER')
    console.gotoxy(1, 2)
    for _ in range(1, 80):
        console.write(196)
    console.gotoxy(1, 3)
    Col(7, 7, console)
    console.writeln('  This is not a shareware game, but it is user-supported.  If you enjoy this')
    console.writeln('game you are asked by the author to please send a registration check in the')
    console.writeln('amount of $7.50 to Apogee Software.')
    console.writeln('  This registration fee will qualify you to order any of the other Kroz')
    console.writeln('volumes available:')
    console.writeln()
    Col(15, 7, console)
    console.write('  '); console.write(254); console.write(' Caverns of Kroz   - the first discovery of Kroz')
    console.write('  '); console.write(254); console.write(' Dungeons of Kroz  - the dark side of Kroz, fast-paced action')
    console.write('  '); console.write(254); console.write(' Kingdom of Kroz   - the national contest winner ("Best Game" in 1988)')
    console.write('  '); console.write(254); console.write(' Return to Kroz    - the discovery of entirely new underground chambers')
    console.write('  '); console.write(254); console.write(' Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems')
    console.write('  '); console.write(254); console.write(' The Final Crusade of Kroz - the suprising finish?')
    console.writeln()
    Col(7, 7, console)
    console.writeln('Each game is priced $7.50 each, any three for $20, or all six for only $35.')
    console.writeln('You''ll also get a secret code that makes this game easier to complete,')
    console.writeln('plus a "Hints, Tricks and Scoring Secrets" guide and "The Domain of Kroz" map.')
    console.writeln()
    Col(7, 7, console)
    console.write('Please make checks payable to:')
    Col(14, 7, console)
    console.writeln('   Apogee Software    (phone: 214/240-0614)')
    console.gotoxy(31, 21)
    console.writeln('   4206 Mayflower')
    Col(15, 15, console)
    console.write  ('Address always valid!')
    console.gotoxy(31, 22)
    Col(14, 7, console)
    console.writeln('  Garland, TX 75043  (USA)')
    console.writeln()
    Col(7, 7, console)
    console.write('Thank you and enjoy the game.  -- Scott Miller')
    if Wait:
        console.delay(0)
    Bak(randint(0, 6) + 1, 7)
    console.gotoxy(1, 25)
    console.gotoxy(27, 25)
    Col(16, 16, console)
    console.write('Press any key to continue.')
    ClearKeys(console)
    while not console.keypressed():
        pass
    ClearKeys(console)
    Bak(0, 0, console)
    console.clrscr()