# System Libraries
from typing import List, cast
from random import randint, randrange
from pathlib import Path
import json

# Project Libraries
from tiles import Tiles
from crt import Crt
import sounds

class VisibleTiles:
    Null       = Tiles.Code[0]
    Block      = Tiles.Code[178]
    Whip       = Tiles.Code[244]
    Stairs     = Tiles.Code[240]
    Chest      = Tiles.Code[67]
    SlowTime   = Tiles.Code[232]
    Gem        = Tiles.Code[4]
    Invisible  = Tiles.Code[173]
    Teleport   = Tiles.Code[24]
    Key        = Tiles.Code[140]
    Door       = Tiles.Code[236]
    Wall       = Tiles.Code[219]
    SpeedTime  = Tiles.Code[233]
    Trap       = Tiles.Code[249]
    River      = Tiles.Code[247]
    Power      = Tiles.Code[9]
    Forest     = Tiles.Code[219]
    Tree       = Tiles.Code[5]
    Bomb       = Tiles.Code[157]
    Lava       = Tiles.Code[178]
    Pit        = Tiles.Code[176]
    Tome       = Tiles.Code[245]
    Tunnel     = Tiles.Code[239]
    Freeze     = Tiles.Code[159]
    Nugget     = Tiles.Code[15]
    Quake      = Tiles.Code[0]
    IBlock     = Tiles.Code[30]
    IWall      = Tiles.Code[0]
    IDoor      = Tiles.Code[0]
    Stop       = Tiles.Code[0]
    Trap2      = Tiles.Code[0]
    Zap        = Tiles.Code[30]
    Create     = Tiles.Code[31]
    Generator  = Tiles.Code[6]
    Trap3      = Tiles.Code[0]
    MBlock     = Tiles.Code[178]
    Trap4      = Tiles.Code[0]
    Player     = Tiles.Code[2]
    ShowGems   = Tiles.Code[0]
    ZBlock     = Tiles.Code[178]
    BlockSpell = Tiles.Code[0]
    Chance     = Tiles.Code[63]
    Statue     = Tiles.Code[1]
    WallVanish = Tiles.Code[0]
    OWall1     = Tiles.Code[219]
    OWall2     = Tiles.Code[219]
    OWall3     = Tiles.Code[219]
    CWall1     = Tiles.Code[0]
    Cwall2     = Tiles.Code[0]
    CWall3     = Tiles.Code[0]
    OSpell1    = Tiles.Code[127]
    OSpell2    = Tiles.Code[127]
    OSpell3    = Tiles.Code[127]
    CSpell1    = Tiles.Code[0]
    CSpell2    = Tiles.Code[0]
    CSpell3    = Tiles.Code[0]
    GBlock     = Tiles.Code[178]
    Rock       = Tiles.Code[79]
    EWall      = Tiles.Code[88]
    Trap5      = Tiles.Code[0]
    TBlock     = Tiles.Code[0]
    TRock      = Tiles.Code[0]
    TGem       = Tiles.Code[0]
    TBlind     = Tiles.Code[0]
    TWhip      = Tiles.Code[0]
    TGold      = Tiles.Code[0]
    TTree      = Tiles.Code[0]
    Rope       = Tiles.Code[179]
    DropRope   = Tiles.Code[25]
    Amulet     = Tiles.Code[12]
    ShootRight = Tiles.Code[26]
    ShootLeft  = Tiles.Code[27]
    Trap6      = Tiles.Code[0]
    Trap7      = Tiles.Code[0]
    Trap8      = Tiles.Code[0]
    Trap9      = Tiles.Code[0]
    Trap10     = Tiles.Code[0]
    Trap11     = Tiles.Code[0]
    Trap12     = Tiles.Code[0]
    Trap13     = Tiles.Code[0]
    Message    = Tiles.Code[5]

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
        self.Sx: list[int] = [0 for _ in range(1000)]
        self.Sy: list[int] = [0 for _ in range(1000)]
        self.Mx: list[int] = [0 for _ in range(1000)]
        self.My: list[int] = [0 for _ in range(1000)]
        self.Fx: list[int] = [0 for _ in range(1000)]
        self.Fy: list[int] = [0 for _ in range(1000)]

class Game:
    def __init__(self):
        self.HSList: list[HSType] = [HSType('', 0, 0) for _ in range(1, 15)]
        self.Restart: bool = False

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

def RestoreBorder(level: Level, console: Crt):
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


