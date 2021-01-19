# System Libraries
from typing import List, Union
from random import randint, randrange
from pathlib import Path
import json

# Engine Libraries
import pygame.locals

# Project Libraries
from ascii import ASCII
from crt import Crt
import sounds

class VisibleTiles:
    Null       = ASCII.Char[0]
    Block      = ASCII.Char[178]
    Whip       = ASCII.Char[244]
    Stairs     = ASCII.Char[240]
    Chest      = ASCII.Char[67]
    SlowTime   = ASCII.Char[232]
    Gem        = ASCII.Char[4]
    Invisible  = ASCII.Char[173]
    Teleport   = ASCII.Char[24]
    Key        = ASCII.Char[140]
    Door       = ASCII.Char[236]
    Wall       = ASCII.Char[219]
    SpeedTime  = ASCII.Char[233]
    Trap       = ASCII.Char[249]
    River      = ASCII.Char[247]
    Power      = ASCII.Char[9]
    Forest     = ASCII.Char[219]
    Tree       = ASCII.Char[5]
    Bomb       = ASCII.Char[157]
    Lava       = ASCII.Char[178]
    Pit        = ASCII.Char[176]
    Tome       = ASCII.Char[245]
    Tunnel     = ASCII.Char[239]
    Freeze     = ASCII.Char[159]
    Nugget     = ASCII.Char[15]
    Quake      = ASCII.Char[0]
    IBlock     = ASCII.Char[30]
    IWall      = ASCII.Char[0]
    IDoor      = ASCII.Char[0]
    Stop       = ASCII.Char[0]
    Trap2      = ASCII.Char[0]
    Zap        = ASCII.Char[30]
    Create     = ASCII.Char[31]
    Generator  = ASCII.Char[6]
    Trap3      = ASCII.Char[0]
    MBlock     = ASCII.Char[178]
    Trap4      = ASCII.Char[0]
    Player     = ASCII.Char[2]
    SMonster   = ASCII.Char[142]
    MMonster   = ASCII.Char[153]
    FMonster   = ASCII.Char[234]
    Tile       = ASCII.Char[0]
    ShowGems   = ASCII.Char[0]
    ZBlock     = ASCII.Char[178]
    BlockSpell = ASCII.Char[0]
    Chance     = ASCII.Char[63]
    Statue     = ASCII.Char[1]
    WallVanish = ASCII.Char[0]
    OWall1     = ASCII.Char[219]
    OWall2     = ASCII.Char[219]
    OWall3     = ASCII.Char[219]
    CWall1     = ASCII.Char[0]
    Cwall2     = ASCII.Char[0]
    CWall3     = ASCII.Char[0]
    OSpell1    = ASCII.Char[127]
    OSpell2    = ASCII.Char[127]
    OSpell3    = ASCII.Char[127]
    CSpell1    = ASCII.Char[0]
    CSpell2    = ASCII.Char[0]
    CSpell3    = ASCII.Char[0]
    GBlock     = ASCII.Char[178]
    Rock       = ASCII.Char[79]
    EWall      = ASCII.Char[88]
    Trap5      = ASCII.Char[0]
    TBlock     = ASCII.Char[0]
    TRock      = ASCII.Char[0]
    TGem       = ASCII.Char[0]
    TBlind     = ASCII.Char[0]
    TWhip      = ASCII.Char[0]
    TGold      = ASCII.Char[0]
    TTree      = ASCII.Char[0]
    Rope       = ASCII.Char[179]
    DropRope   = ASCII.Char[25]
    Amulet     = ASCII.Char[12]
    ShootRight = ASCII.Char[26]
    ShootLeft  = ASCII.Char[27]
    Trap6      = ASCII.Char[0]
    Trap7      = ASCII.Char[0]
    Trap8      = ASCII.Char[0]
    Trap9      = ASCII.Char[0]
    Trap10     = ASCII.Char[0]
    Trap11     = ASCII.Char[0]
    Trap12     = ASCII.Char[0]
    Trap13     = ASCII.Char[0]
    Message    = ASCII.Char[5]

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

# Unit-level State
class Level:
    def __init__(self):
        self.Score: int = 0
        self.WhipPower: int = 0
        self.Level: int = 0
        self.Gems: int = 0
        self.Whips: int = 0
        self.Teleports: int = 0
        self.Keys: int = 0
        self.Bc: int = 0
        self.Bb: int = 0
        self.GemColor: int = 0
        # slow monsters
        self.Sx: list[int] = [0 for _ in range(1000)]
        self.Sy: list[int] = [0 for _ in range(1000)]
        # medium monsters
        self.Mx: list[int] = [0 for _ in range(1000)]
        self.My: list[int] = [0 for _ in range(1000)]
        # fast monsters
        self.Fx: list[int] = [0 for _ in range(1000)]
        self.Fy: list[int] = [0 for _ in range(1000)]
        # player
        self.Px: int = 0
        self.Py: int = 0
        # enum of space occupants
        self.Pf: list[list[int]] = [[0 for _ in range(66)] for _ in range(25)]
        # string definition of the levels for parsing
        self.Fp: list[str] = ['{0:{width}}'.format(' ', width = XSIZE) for _ in range(YSIZE)]
        self.Parsed: list[int] = [0 for _ in range(TOTOBJECTS)]
        self.GenNum: int = 0
        self.T: list[int] = [0 for 0 in range(TMAX)] # timers?
        self.LavaFlow: bool = False
        self.LavaRate: int = 0
        self.TreeRate: int = -1
        self.Evaporate: int = 0
        self.GravCounter: int = 0
        self.GravOn: bool = False
        self.GravRate: int = 0
        self.Sideways: bool = False
        self.FloorPattern: bool = False
        self.Bonus: int = 0
        self.MagicEWalls: bool = False
        self.HideRock: bool = False
        self.HideStairs: bool = False
        self.HideLevel: bool = False
        self.HideCreate: bool = False
        self.HideOpenWall: bool = False
        self.HideTrap: bool = False
        self.HideGems: bool = False
        self.HideMBlock: bool = False
        self.GenFactor: int = 0
        self.BTime: int = 0
        self.STime: int = 0
        self.MTime: int = 0
        self.FTime: int = 0
        self.SkipTime: int = 0
        # Floor colors
        self.Cf1: int = 0
        self.Cf2: int = 0
        self.Bf1: int = 0
        self.Bf2: int = 0

class Game:
    def __init__(self):
        self.HSList: list[HSType] = [HSType('', 0, 0) for _ in range(1, 15)]
        self.Restart: bool = False
        self.Df: list[str] = ['' for _ in range(1, 30)]
        self.OneMove: bool = True
        self.Replacement: Union[int, None] = None
        self.Difficulty: int = 0
        self.MixUp: bool = True
        self.Color: bool = True
        self.FastPC: bool = True
        self.FoundSet: list[int] = []

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
        console.write(VisibleTiles.Block)
        console.gotoxy(x, 1)
        console.write(VisibleTiles.Block)
    for y in range(YBOT - 1, YTOP + 2):
        console.gotoxy(1, y)
        console.write(VisibleTiles.Block)
        console.gotoxy(66, y)
        console.write(VisibleTiles.Block)
    Bak(0, 0, console)

def Restore_Border(level: Level, console: Crt):
    console.gotoxy(2, 25)
    Col(level.Bc, 0)
    Bak(level.Bb, 7)
    for _ in range(XBOT - 1, XTOP + 2):
        console.write(VisibleTiles.Block)
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
    Restore_Border(level, console)

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

def Col(color: int, bw: int, console: Crt):
    console.textcolor(color)

def Bak(color: int, bw: int, console: Crt):
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
    console.writeln('■ The six Kroz games! CAVERNS OF KROZ, KINGDOM OF KROZ, DUNGEONS OF KROZ,')
    console.writeln('     RETURN TO KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.')
    console.writeln('     Each volume is just $7.50, or order all six for $35!')
    console.writeln()
    Col(7, 7, console)
    console.writeln('■ SUPERNOVA - Explore a galaxy and save a planet from an exploding star!')
    console.writeln('     An epic adventure rated by Shareware Magazine as one of the best games')
    console.writeln('     ever! Highly advanced game has graphics, sound effects galore, clue')
    console.writeln('     command, and dozens of unique features. ($10)')
    console.writeln()
    console.writeln('■ BEYOND THE TITANIC - A fantastic adventure of exploration and survival.')
    console.writeln('     What really happened? Sound effects and 16 color screens.  ($8)')
    console.writeln()
    console.writeln('■ WORD WHIZ - New game that challenges your knowledge of the English')
    console.writeln('     language.  Fun to play, yet very education, too.  ($5)')
    console.writeln()
    Col(15, 15, console)
    console.writeln('■ THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best')
    console.write  ('     levels yet!  Built-in contest!  New features galore.  ($20)')
    Col(7, 7, console)
    ClearKeys(console)
    console.halt()

def Shareware(console: Crt, Wait: bool):
    Bak(1, 0, console)
    console.clrscr()
    Col(15, 15, console)
    console.gotoxy(22, 1)
    console.writeln('DUNGEONS OF KROZ II ─ HOW TO REGISTER')
    console.gotoxy(1, 2)
    for _ in range(1, 80):
        console.write('─')
    console.gotoxy(1, 3)
    Col(7, 7, console)
    console.writeln('  This is not a shareware game, but it is user-supported.  If you enjoy this')
    console.writeln('game you are asked by the author to please send a registration check in the')
    console.writeln('amount of $7.50 to Apogee Software.')
    console.writeln('  This registration fee will qualify you to order any of the other Kroz')
    console.writeln('volumes available:')
    console.writeln()
    Col(15, 7, console)
    console.write('  ■ Caverns of Kroz   - the first discovery of Kroz')
    console.write('  ■ Dungeons of Kroz  - the dark side of Kroz, fast-paced action')
    console.write('  ■ Kingdom of Kroz   - the national contest winner ("Best Game" in 1988)')
    console.write('  ■ Return to Kroz    - the discovery of entirely new underground chambers')
    console.write('  ■ Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems')
    console.write('  ■ The Final Crusade of Kroz - the suprising finish?')
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

def New_Gem_Color(level: Level):
    level.GemColor = randint(0, 15) + 1
    while level.GemColor == 8:
        level.GemColor = randint(0, 15) + 1

def Play(Start: int, Stop: int, Speed: int, console: Crt):
    if Start < Stop:
        for x in range(Start, Stop):
            console.sound(x, Speed)
    else:
        for x in range(Start, Stop, -1):
            console.sound(x, Speed)

def AddScore(What: int, level: Level, console: Crt):
    if What >= 1 and What <=3: # Monsters
        level.Score += What
    elif What == 4 or What == 14: # Block
        if level.Score > 2:
            level.Score -= 2
    elif What == 5: # Whip
        level.Score += 1
    elif What == 6: # Stairs
        level.Score += level.Level
    elif What == 7: # Chest
        level.Score += 5
    elif What == 9: # Gem
        level.Score += 1
    elif What == 10: # Invisible
        level.Score += 10
    elif What == 11: # Teleport
        level.Score += 1
    elif What == 15: # SpeedTime
        level.Score += 2
    elif What == 16: # Trap
        if level.Score > 5:
            level.Score -= 5
    elif What == 22: # Lava
        level.Score += 25
    elif What == 20: # Border
        if level.Score > level.Level:
            level.Score -= level.Level // 2
    elif What == 27: # Nugget
        level.Score += 50
    elif What == 35: # Create
        level.Score += level.Level * 2
    elif What == 36: # Generator
        level.Score += 50
    elif What == 38: # MBlock
        level.Score += 1

    Update_Info(level, console)

def Won(level: Level, console: Crt):
    Border(level, console)
    ClearKeys(console)
    Col(15, 31, console)
    Bak(level.Bb, 0, console)
    Print(5, 1, 'YOUR QUEST FOR THE MAGICAL STAFF OF KROZ WAS SUCCESSFUL!!', console)
    Bak(0, 0, console)
    High_Score(console, PlayAgain = False)

def High_Score(PlayAgain: bool, game: Game, level: Level, console: Crt):
    ClearKeys(console)
    console.window(2, 2, XSIZE + 1, YSIZE + 1)
    Bak(0, 0, console)
    console.clrscr()
    console.window(1, 1, 80, 25)
    hsFile = Path('DUNGEON2.HS')
    if not hsFile.exists():
        game.HSList[0] = HSType('Scott Miller', 13640, 16)
        game.HSList[1] = HSType('Indy J.', 8574, 14)
        game.HSList[2] = HSType('J. T. Kirk', 6995, 11)
        game.HSList[3] = HSType('Neil Peart', 3501, 8)
        game.HSList[4] = HSType('Ttocs Rellim', 1228, 5)
        for x in range(5, len(game.HSList)):
            game.HSList[x] = HSType('Adventurer', 0, 0)
        hsFile.touch()
        with hsFile.open('w') as f:
            json.dump(game.HSList, f, separators=(',', ':'))
    Col(9, 9, console)
    console.gotoxy(25, 3)
    console.write('DUNGEONS OF KROZ II')
    Col(11, 7, console)
    console.gotoxy(16, 5)
    console.write('NAME')
    console.gotoxy(34, 5)
    console.write('HIGH SCORE')
    console.write('LEVEL')
    with hsFile.open('r') as f:
        game.HSList = json.load(f)
    place = 1
    stop = False
    while (stop is False and place <= 15):
        if level.Score > game.HSList[place].HighScore: stop = True
        place += 1
        if stop is False and place > 15: place = 100
    place -= 1
    if place < 16:
        for x in range (15, place, -1):
            game.HSList[x] = game.HSList[x - 1]
    game.HSList[place] = HSType('', level.Score, level.Level)
    for x in range(len(game.HSList)):
        if x % 2 == 1:
            Col(12, 7, console)
        else:
            Col(13, 7, console)
        console.gotoxy(13, x + 6)
        console.write('{0:2}'.format(x))
        console.gotoxy(16, x + 6)
        console.write(game.HSList[x].Name)
        console.gotoxy(36, x + 6)
        console.write('{0}0'.format(game.HSList[x].HighScore) if game.HSList[x].HighScore > 0 else '0')
        console.gotoxy(50, x + 6)
        console.write('{0}'.format(game.HSList[x].HighLevel))
    ClearKeys(console)
    if place < 16:
        Bak(4, 7, console)
        console.gotoxy(16, place + 6)
        console.write('               ')
        Col(4, 0, console)
        Bak(7, 7, console)
        console.gotoxy(16, 23)
        console.write('Enter your name then press <enter>.')
        Col(15, 15, console)
        Bak(4, 7, console)
        console.gotoxy(16, place + 6)
        game.HSList[place].Name = console.readln()
        with hsFile.open('w') as f:
            json.dump(game.HSList, f)
    Bak(0, 0, console)
    console.gotoxy(16, 23)
    console.write('                                   ')
    for x in range(1000):
        level.Sx[x] = 0
        level.Sy[x] = 0
        level.Mx[x] = 0
        level.My[x] = 0
        level.Fx[x] = 0
        level.Fy[x] = 0
    if PlayAgain:
        Flash(14, 25, 'Do you want to play another game (Y/N)?', level, console)
        ch = console.readkey()
    else:
        Flash(21, 25, 'Press any key to continue.', level, console)
        ch = 'N'
    if ch.upper() is not 'N': 
        game.Restart = True
    else:
        Bak(0, 0, console)
        Col(15, 15, console)
        console.clrscr()
        if not PlayAgain:
            console.gotoxy(1, 2)
            console.writeln('You''ve completed DUNGEIONS OF KROZ II!')
        else:
            console.gotoxy(17, 2)
            console.writeln('DUNGEONS OF KROZ II')
        Sign_Off(console)

def Dead(DeadDot: bool, game: Game, level: Level, console: Crt):
    if level.Gems > 9:
        Col(4, 7, console)
    else:
        level.Gems = 0
        Col(23, 23, console)
    Bak(7, 0, console)
    console.gotoxy(71, 8)
    console.write('     ')
    strVal = '{0}'.format(level.Gems)
    console.gotoxy(73 - len(strVal) // 2, 8)
    console.write(strVal)
    Bak(0, 0, console)
    if DeadDot:
        for x in range(150, 5, -1):
            console.gotoxy(level.Px, level.Py)
            Col(x, x, console)
            Bak(randint(8), 0, console)
            console.write(VisibleTiles.Player)
            console.sound(x * x, 0.5)
    ClearKeys(console)
    Col(16, 16, console)
    Bak(level.Bb, 7, console)
    Print(27, 1, 'YOU HAVE DIED!!', console)
    Bak(0, 0, console)
    while not console.keypressed():
        Col(randint(16), randint(16), console)
        console.gotoxy(level.Px, level.Py)
        if DeadDot: console.write('*')
        Print(21, 25, 'Press any key to continue.', console)
    Border(level, console)
    High_Score(True, game, level, console)

def Define_Levels(game: Game):
    for i in range(1, 30):
        game.Df[i] = ''
                  #  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -
    game.Df[2] =  '200  5   100     2  1  1 40        1    50     5                                                '
    game.Df[4] =  '   200       38  2                                                                              '
    game.Df[6] =  '      180 50     2       75                                                                     '
    game.Df[8] =  '             20  2  1    40 35  2              5         990              3                     '
    game.Df[10] = '   400           1       20                 1                                     35            '
    game.Df[12] = '100 75 50100 10  1  1  1 30     1  1                          5                     100         '
    game.Df[14] = '      170     5  1  1    25500  1       50 50 50     1        1          28        1            '
    game.Df[16] = '    60           1     6 30 20              1                  550        4     5  2            '
    game.Df[18] = '100           3  1  1    20     2              5              1           4    20   850         '
    game.Df[20] = '   550   650  5  1  1     5     1  1           1              1                20  8            '
    game.Df[22] = '      300        1         300            150150              1               300               '
    game.Df[24] = '   305        5  1  1     5     1           1                             2     5            999'
    game.Df[26] = '   100 20    25  2  1  2 20  1  2             10     1        5   785    10    15               '
    game.Df[28] = '133133133        3  3    80420  1  1                                           10  5            '

def Convert_Format(level: Level):
    SNum = 0
    MNum = 0
    FNum = 0
    BNum = 0
    GenNum = 0
    level.T[9] = -1
    level.LavaFlow = False
    level.TreeRate = 0
    level.GravCounter = 0
    level.GravOn = False
    for x in range(66):
        for y in range(25):
            level.Pf[x][y] = 0
    for m in range(1000):
        level.Sx[m] = 0
        level.Sy[m] = 0
        level.Mx[m] = 0
        level.My[m] = 0
        level.Fx[m] = 0
        level.Fy[m] = 0
    New_Gem_Color(level)
    for YLoop in range(YSIZE):
        for XLoop in range(XSIZE):
            tempstr = level.Fp[YLoop][XLoop]
            if tempstr == ' ':
                level.Pf[XLoop + 1, YLoop + 1] = 0
            elif tempstr == '1':
                SNum += 1
                level.Sx[SNum] = XLoop + 1
                level.Sy[SNum] = YLoop + 1
                level.Pf[XLoop + 1, YLoop + 1] = 1
            elif tempstr == '2':
                MNum += 1
                level.Mx[MNum] = XLoop + 1
                level.My[MNum] = YLoop + 1
                level.Pf[XLoop + 1, YLoop + 1] = 1
            elif tempstr == '3':
                FNum += 1
                level.Fx[FNum] = XLoop + 1
                level.Fy[FNum] = YLoop + 1
                level.Pf[XLoop + 1, YLoop + 1] = 1
            elif tempstr == 'X':
                level.Pf[XLoop + 1, YLoop + 1] = 4
            elif tempstr == 'W':
                level.Pf[XLoop + 1, YLoop + 1] = 5
            elif tempstr == 'L':
                level.Pf[XLoop + 1, YLoop + 1] = 6
            elif tempstr == 'C':
                level.Pf[XLoop + 1, YLoop + 1] = 7
            elif tempstr == 'S':
                level.Pf[XLoop + 1, YLoop + 1] = 8
            elif tempstr == '+':
                level.Pf[XLoop + 1, YLoop + 1] = 9
            elif tempstr == 'I':
                level.Pf[XLoop + 1, YLoop + 1] = 10
            elif tempstr == 'T':
                level.Pf[XLoop + 1, YLoop + 1] = 11
            elif tempstr == 'K':
                level.Pf[XLoop + 1, YLoop + 1] = 12
            elif tempstr == 'D':
                level.Pf[XLoop + 1, YLoop + 1] = 13
            elif tempstr == '#':
                level.Pf[XLoop + 1, YLoop + 1] = 14
            elif tempstr == 'F':
                level.Pf[XLoop + 1, YLoop + 1] = 15
            elif tempstr == '.':
                level.Pf[XLoop + 1, YLoop + 1] = 16
            elif tempstr == 'R':
                level.Pf[XLoop + 1, YLoop + 1] = 17
            elif tempstr == 'Q':
                level.Pf[XLoop + 1, YLoop + 1] = 18
            elif tempstr == '/':
                level.Pf[XLoop + 1, YLoop + 1] = 19
            elif tempstr == '\\':
                level.Pf[XLoop + 1, YLoop + 1] = 20
            elif tempstr == 'B':
                level.Pf[XLoop + 1, YLoop + 1] = 21
            elif tempstr == 'V':
                level.Pf[XLoop + 1, YLoop + 1] = 22
            elif tempstr == '=':
                level.Pf[XLoop + 1, YLoop + 1] = 23
            elif tempstr == 'A':
                level.Pf[XLoop + 1, YLoop + 1] = 24
            elif tempstr == 'U':
                level.Pf[XLoop + 1, YLoop + 1] = 25
            elif tempstr == 'Z':
                level.Pf[XLoop + 1, YLoop + 1] = 26
            elif tempstr == '*':
                level.Pf[XLoop + 1, YLoop + 1] = 27
            elif tempstr == 'E':
                level.Pf[XLoop + 1, YLoop + 1] = 28
            elif tempstr == ';':
                level.Pf[XLoop + 1, YLoop + 1] = 29
            elif tempstr == ':':
                level.Pf[XLoop + 1, YLoop + 1] = 30
            elif tempstr == '`':
                level.Pf[XLoop + 1, YLoop + 1] = 31
            elif tempstr == '-':
                level.Pf[XLoop + 1, YLoop + 1] = 32
            elif tempstr == '@':
                level.Pf[XLoop + 1, YLoop + 1] = 33
            elif tempstr == '%':
                level.Pf[XLoop + 1, YLoop + 1] = 34
            elif tempstr == ']':
                level.Pf[XLoop + 1, YLoop + 1] = 35
            elif tempstr == 'G':
                level.Pf[XLoop + 1, YLoop + 1] = 36
                GenNum += 1
            elif tempstr == '(':
                level.Pf[XLoop + 1, YLoop + 1] = 37
            elif tempstr == '!':
                level.Pf[XLoop + 1, YLoop + 1] = 222
            elif tempstr == 'P':
                level.Pf[XLoop + 1, YLoop + 1] = 40
                level.Px = XLoop + 1
                level.Py = YLoop + 1
            else:
                level.Pf[XLoop + 1, YLoop + 1] = ASCII.Ord[tempstr]

def Go(XWay: int, YWay: int, Human: bool, game: Game, level: Level, console: Crt):
    if level.Sideways and YWay == -1 and not game.OneMove and game.Replacement != 75:
        return
    previous = game.Replacement
    old_x = level.Px
    old_y = level.Py

    level.Pf[level.Px, level.Py] = game.Replacement
    console.gotoxy(level.Pf, level.Py)
    console.write(' ')
    level.Px += XWay
    level.Py += YWay
    if level.Pf[level.Px, level.Py] >=55 and level.Pf[level.Px, level.Py] <= 57 or level.Pf[level.Px, level.Py] == 75:
        game.Replacement = level.Pf[level.Px, level.Py]
    else:
        game.Replacement = None
    if previous == 75:
        Col(7, 7, console)
        console.gotoxy(old_x, old_y)
        console.write(VisibleTiles.Rope)
    level.Pf[level.Px, level.Py] = 40
    if level.T[5] < 1:
        console.gotoxy(level.Px, level.Py)
        Col(14, 15, console)
        Bak(0, 0, console)
        console.write(VisibleTiles.Player)
    else:
        console.gotoxy(level.Px, level.Py)
        console.write(' ')
    if not level.Sideways:
        FootStep(console)
    elif game.Replacement != 75 and Human:
        FootStep(console)
    if console.keypressed() and Human:
        ch = console.read()
        if ch == pygame.locals.K_ESCAPE:
            console.read()

def MoveRock(XWay: int, YWay: int):
    pass

def Trigger_Trap(Place: bool, i: int, ch: str):
    pass

def End_Routine(level: Level, console: Crt):
    FootStep(console)
    console.delay(200)
    FootStep(console)
    console.delay(300)
    FootStep(console)
    for x in range(1, 250):
        console.sound(randint(3000) + x, 0.5)
        console.gotoxy(level.Px, level.Py)
        Bak(randint(8), 0, console)
        Col(14, 15, console)
        console.write(VisibleTiles.Player)
        Col(randint(16), randint(16), console)
        Bak(0, 0, console)
        Print(15, 25, 'Oh no, something strange is happening!', console)
    for i in range(2200, 20, -1):
        console.sound(randint(i))
    Col(14, 15, console)
    Bak(0, 0, console)
    for x in range(650):
        console.sound(x * 3, 2)
        console.gotoxy(level.Px, level.Py)
        console.write(220 + randint(4))
    console.gotoxy(level.Px, level.Py)
    Col(16, 16, console)
    Bak(2, 7, console)
    console.write(VisibleTiles.Stairs)
    Restore_Border(level, console)
    Flash(14, 25, 'You are magically transported from Kroz!')
    ClearKeys(console)
    Col(15, 15, console)
    Bak(0, 0, console)
    Print(15, 25, 'Your gems are worth 100 points each...')
    for i in range(level.Gems):
        level.Score += 10
        Update_Info(level, console)
        console.sound(i * 8 + 100, 20)
    console.read()
    Restore_Border(level, console)
    ClearKeys(console)
    Col(15, 15, console)
    Bak(0, 0, console)
    Print(15, 25, 'Your whips are worth 100 points each...')
    for i in range(level.Whips):
        level.Score += 10
        Update_Info(level, console)
        console.sound(i * 10 + 200, 20)
    console.read()
    Restore_Border(level, console)
    ClearKeys(console)
    Col(15, 15, console)
    Bak(0, 0, console)
    Print(9, 25, 'Your Teleport Scrolls are woth 200 points each...')
    for i in range(level.Teleports):
        level.Score += 20
        Update_Info(level, console)
        console.sound(i * 12 + 300, 30)
    console.read()
    Restore_Border(level, console)
    ClearKeys(console)
    Col(15, 15, console)
    Bak(0, 0, console)
    Print(14, 25, 'Your Keys are worth 10,000 points each...')
    for i in range(level.Keys):
        level.Score += 1000
        Update_Info(level, console)
        console.sound(i * 30 + 100, 50)
    console.read()
    Restore_Border(level, console)
    ClearKeys(console)
    Bak(level.GemColor, 7, console)
    for x in range(30):
        console.window(32 - x, 12 - x // 3, 35 + x, 14 + (x // 3))
        console.clrscr()
    Bak(0, 0, console)
    for x in range(30):
        console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
        console.clrscr()
        console.sound(x * 45, 3)
    console.window(1, 1, 80, 25)
    Bak(1, 0, console)
    console.window(2, 2, 65, 24)
    console.clrscr()
    Col(14, 15, console)
    console.gotoxy(25, 2)
    console.writeln('BACK AT YOUR HUT')
    console.gotoxy(25, 3)
    console.writeln('────────────────')
    console.writeln()
    Col(15, 7, console)
    console.writeln('   For years you''ve waited for such a wonderful archaeological')
    console.writeln(' discovery. And now you possess one of the greatest finds ever!')
    console.writeln('   The Magical Staff will bring you even more recognition than')
    console.writeln(' the Priceless Amulet you previously found in the depths of')
    console.writeln(' Kroz.  However, Kroz is still mostly unexplored, and you have')
    console.writeln(' reason to believe that even more fabulous treasures lie below.')
    console.writeln('   Therefore, it doesn''t take much to convince you that another')
    console.writeln(' expedition is in order.  You must leave no puzzle unsolved, no')
    console.writeln(' treasure unfound--to quit now would be a coward''s choice.')
    console.writeln('   So you plan for a good night''s rest, and think ahead to')
    console.writeln(' tomorrow''s new journey.  What does the mysterious Kingdom of')
    console.writeln(' Kroz have waiting for you, what type of new creatures will')
    console.writeln(' try for you blood, and what new brilliant treasure does')
    console.writeln(' Kroz protect.  Tomorrow will tell...')
    console.writeln()
    Col(14, 15, console)
    console.writeln('                         KINGDOM OF KROZ')
    Col(15, 7, console)
    console.write  ('        ( Now available -- $7.50 or write for details. )')
    ClearKeys(console)
    console.window(1, 1, 80, 25)
    Bak(0, 0, console)
    Flash(21, 25, 'Press any key, Adventurer.', console)
    Won(level, console)