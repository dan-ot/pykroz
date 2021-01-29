# System Libraries
from pygame.event import post
from playerstate import PlayerState
from playfield import Playfield
from pieces import VisibleTiles, What, WhatSets, parse
from typing import List, Optional, Union
from random import randrange
from pathlib import Path
import json

# Engine Libraries
import pygame.locals
import pygame.key
from pygame import Color

# Project Libraries
from crt import Crt
import sounds
from colors import Colors

# Constants
TOTOBJECTS = 83

XBOT = 2
XTOP = 65
YBOT = 2
YTOP = 24
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
        self.Bc: int = 0
        self.Bb: int = 0
        self.GemColor: int = 0
        # slow monsters
        self.Sx: list[int] = [0 for _ in range(1000)]
        self.Sy: list[int] = [0 for _ in range(1000)]
        self.SNum: int = 0
        # medium monsters
        self.Mx: list[int] = [0 for _ in range(1000)]
        self.My: list[int] = [0 for _ in range(1000)]
        self.MNum: int = 0
        # fast monsters
        self.Fx: list[int] = [0 for _ in range(1000)]
        self.Fy: list[int] = [0 for _ in range(1000)]
        self.FNum: int = 0
        # string definition of the levels for parsing
        self.Fp: list[str] = ['{0:{width}}'.format(' ', width = XSIZE) for _ in range(YSIZE)]
        self.Parsed: list[int] = [0 for _ in range(TOTOBJECTS)]
        self.GenNum: int = 0
        # Timers:
        self.SkipTime: int = 0
        self.T: list[int] = [0 for _ in range(TMAX)]
        # * T[1..3] = Monster Move Timers?
        # * T[4] = SlowTime
        # * T[5] = Invisibility
        # * T[6] = FastTime
        # * T[7] = Freeze
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
        # Monster delay speeds
        self.STime: int = 0
        self.MTime: int = 0
        self.FTime: int = 0
        self.SkipTime: int = 0
        # Floor colors
        self.Cf1: int = 0
        self.Cf2: int = 0
        self.Bf1: int = 0
        self.Bf2: int = 0
        # Save/Restore Variables
        self.I_Score: int = 0
        self.I_Gems: int = 0
        self.I_Whips: int = 0
        self.I_Teleports: int = 0
        self.I_Keys: int = 0
        self.I_WhipPower: int = 0
        self.I_Px: int = 0
        self.I_Py: int = 0
        self.I_FoundSet: set[What] = set()
        self.I_Difficulty: int = 0

class Game:
    def __init__(self):
        self.HSList: list[HSType] = [HSType('', 0, 0) for _ in range(1, 15)]
        self.Restart: bool = False
        self.Df: list[str] = ['' for _ in range(1, 30)]
        self.OneMove: bool = True
        self.Difficulty: int = 0
        self.MixUp: bool = True
        self.FastPC: bool = True
        self.FoundSet: set[What] = set()

# Procedures
def PrintNum(YPos: int, Num: int, player: PlayerState, console: Crt, fore: Optional[Color] = None, back: Optional[Color] = None):
    # console.write(70, YPos, "       ")
    strVal = str(Num)
    if (YPos == 2 and player.score > 0):
        strVal += "0"
    if (YPos == 11):
        if (player.whip_power >= 3):
            strVal = strVal + "+" + str(player.whip_power)
    strVal = f"{strVal:^7}"
    console.write(69, YPos - 1, strVal, fore, back)

def Update_Info(player: PlayerState, console: Crt):
    console.default_colors(Colors.Red, Colors.LightGrey)
    PrintNum(2, player.score, player, console)
    PrintNum(5, player.level, player, console)
    if player.gems > 9:
        PrintNum(8, player.gems, player, console)
    else:
        PrintNum(8, player.gems, player, console, Colors.LightRed, Colors.DarkGrey) # Flashing Red when it can be managed
    PrintNum(11, player.whips, player, console)
    PrintNum(14, player.teleports, player, console)
    PrintNum(17, player.keys, player, console)
    console.reset_colors()

def Border(level: Level, console: Crt):
    level.Bc = randrange(8, 15)
    level.Bb = randrange(1, 8)
    for x in range(XBOT - 1, XTOP + 2):
        console.gotoxy(x, 25)
        console.write(VisibleTiles.Breakable_Wall, Colors.Code[level.Bc], Colors.Code[level.Bb])
        console.gotoxy(x, 1)
        console.write(VisibleTiles.Breakable_Wall, Colors.Code[level.Bc], Colors.Code[level.Bb])
    for y in range(YBOT - 1, YTOP + 2):
        console.gotoxy(1, y)
        console.write(VisibleTiles.Breakable_Wall, Colors.Code[level.Bc], Colors.Code[level.Bb])
        console.gotoxy(66, y)
        console.write(VisibleTiles.Breakable_Wall, Colors.Code[level.Bc], Colors.Code[level.Bb])

def Restore_Border(level: Level, console: Crt):
    console.gotoxy(2, 25)
    for _ in range(XBOT - 1, XTOP + 2):
        console.write(VisibleTiles.Breakable_Wall, Colors.Code[level.Bc], Colors.Code[level.Bb])

def Sign_Off(console: Crt):
    Shareware(console, Wait = False)
    console.clearkeys()
    console.default_colors(Colors.LightGrey, Colors.Black)
    console.clrscr()
    console.gotoxy(31, 2)
    console.write('DUNGEONS OF KROZ II')
    console.gotoxy(26, 3)
    console.writeln('An Apogee Software Production')
    console.writeln()
    console.writeln('Other great games available from Scott Miller:')
    console.writeln()
    console.default_colors(Colors.White)
    console.writeln('■ The six Kroz games! CAVERNS OF KROZ, KINGDOM OF KROZ, DUNGEONS OF KROZ,')
    console.writeln('     RETURN TO KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.')
    console.writeln('     Each volume is just $7.50, or order all six for $35!')
    console.writeln()
    console.default_colors(Colors.LightGrey)
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
    console.default_colors(Colors.White)
    console.writeln('■ THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best')
    console.write  ('     levels yet!  Built-in contest!  New features galore.  ($20)')
    console.clearkeys()
    console.halt()

def Shareware(console: Crt, Wait: bool):
    console.default_colors(Colors.White, Colors.Blue)
    console.clrscr()
    console.gotoxy(22, 1)
    console.writeln('DUNGEONS OF KROZ II ─ HOW TO REGISTER')
    console.gotoxy(1, 2)
    for _ in range(1, 80):
        console.write('─')
    console.gotoxy(1, 3)
    console.default_colors(Colors.LightGrey)
    console.writeln('  This is not a shareware game, but it is user-supported.  If you enjoy this')
    console.writeln('game you are asked by the author to please send a registration check in the')
    console.writeln('amount of $7.50 to Apogee Software.')
    console.writeln('  This registration fee will qualify you to order any of the other Kroz')
    console.writeln('volumes available:')
    console.writeln()
    console.default_colors(Colors.White)
    console.write('  ■ Caverns of Kroz   - the first discovery of Kroz')
    console.write('  ■ Dungeons of Kroz  - the dark side of Kroz, fast-paced action')
    console.write('  ■ Kingdom of Kroz   - the national contest winner ("Best Game" in 1988)')
    console.write('  ■ Return to Kroz    - the discovery of entirely new underground chambers')
    console.write('  ■ Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems')
    console.write('  ■ The Final Crusade of Kroz - the suprising finish?')
    console.writeln()
    console.default_colors(Colors.LightGrey)
    console.writeln('Each game is priced $7.50 each, any three for $20, or all six for only $35.')
    console.writeln('You''ll also get a secret code that makes this game easier to complete,')
    console.writeln('plus a "Hints, Tricks and Scoring Secrets" guide and "The Domain of Kroz" map.')
    console.writeln()
    console.write('Please make checks payable to:')
    console.writeln('   Apogee Software    (phone: 214/240-0614)', Colors.Yellow)
    console.gotoxy(31, 21)
    console.writeln('   4206 Mayflower', Colors.Yellow)
    console.write  ('Address always valid!', Colors.White)
    console.gotoxy(31, 22)
    console.writeln('  Garland, TX 75043  (USA)', Colors.Yellow)
    console.writeln()
    console.write('Thank you and enjoy the game.  -- Scott Miller')
    if Wait:
        console.delay(0)
    console.gotoxy(1, 25)
    console.gotoxy(27, 25)
    console.write('Press any key to continue.', Colors.White, Colors.RandomDark()) # Flashing when possible
    console.clearkeys()
    while not console.keypressed():
        pass
    console.clearkeys()
    console.reset_colors()
    console.clrscr()

def New_Gem_Color(level: Level):
    level.GemColor = Colors.RandomExcept([8])

def AddScore(what: What, player: PlayerState, console: Crt):
    player.add_score(what)
    Update_Info(player, console)

def Won(level: Level, console: Crt):
    Border(level, console)
    console.clearkeys()
    console.print(5, 1, 'YOUR QUEST FOR THE MAGICAL STAFF OF KROZ WAS SUCCESSFUL!!', Colors.White, Colors.Code[level.Bb]) # Flashing when possible
    High_Score(console, PlayAgain = False)

def High_Score(PlayAgain: bool, game: Game, player: PlayerState, level: Level, console: Crt):
    console.clearkeys()
    console.window(2, 2, XSIZE + 1, YSIZE + 1)
    console.reset_colors()
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
    console.gotoxy(25, 3)
    console.write('DUNGEONS OF KROZ II', Colors.LightBlue)
    console.gotoxy(16, 5)
    console.write('NAME', Colors.LightCyan)
    console.gotoxy(34, 5)
    console.write('HIGH SCORE', Colors.LightCyan)
    console.write('LEVEL', Colors.LightCyan)
    with hsFile.open('r') as f:
        game.HSList = json.load(f)
    place = 1
    stop = False
    while (stop is False and place <= 15):
        if player.score > game.HSList[place].HighScore: stop = True
        place += 1
        if stop is False and place > 15: place = 100
    place -= 1
    if place < 16:
        for x in range (15, place, -1):
            game.HSList[x] = game.HSList[x - 1]
    game.HSList[place] = HSType('', player.score, player.level)
    for x in range(len(game.HSList)):
        if x % 2 == 1:
            console.default_colors(Colors.LightRed)
        else:
            console.default_colors(Colors.LightMagenta)
        console.gotoxy(13, x + 6)
        console.write('{0:2}'.format(x))
        console.gotoxy(16, x + 6)
        console.write(game.HSList[x].Name)
        console.gotoxy(36, x + 6)
        console.write('{0}0'.format(game.HSList[x].HighScore) if game.HSList[x].HighScore > 0 else '0')
        console.gotoxy(50, x + 6)
        console.write('{0}'.format(game.HSList[x].HighLevel))
    console.clearkeys()
    if place < 16:
        console.gotoxy(16, place + 6)
        console.write('               ', back = Colors.Red)
        console.gotoxy(16, 23)
        console.write('Enter your name then press <enter>.', Colors.Red, Colors.LightGrey)
        console.gotoxy(16, place + 6)
        console.default_colors(Colors.White, Colors.Red)
        game.HSList[place].Name = console.readln()
        with hsFile.open('w') as f:
            json.dump(game.HSList, f)
    console.reset_colors()
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
        console.alert(YTOP + 1, 'Do you want to play another game (Y/N)?', Colors.Code[level.Bc], Colors.Code[level.Bb])
        ch = pygame.key.name(console.read())
    else:
        console.alert(YTOP + 1, 'Press any key to continue.', Colors.Code[level.Bc], Colors.Code[level.Bb])
        ch = 'N'
    if ch.upper() is not 'N': 
        game.Restart = True
    else:
        console.reset_colors()
        console.clrscr()
        if not PlayAgain:
            console.gotoxy(1, 2)
            console.writeln('You''ve completed DUNGEIONS OF KROZ II!')
        else:
            console.gotoxy(17, 2)
            console.writeln('DUNGEONS OF KROZ II')
        Sign_Off(console)

def Dead(DeadDot: bool, game: Game, player: PlayerState, level: Level, console: Crt):
    if player.gems > 9:
        console.default_colors(Colors.Red, Colors.LightGrey)
    else:
        player.ems = 0
        console.default_colors(Colors.LightRed, Colors.DarkGrey) # Flashing, when possible
    console.gotoxy(71, 8)
    console.write('     ')
    strVal = '{0}'.format(player.gems)
    console.gotoxy(73 - len(strVal) // 2, 8)
    console.write(strVal)
    if DeadDot:
        for x in range(150, 5, -1):
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Code[x], Colors.Code[Colors.RandomDark()])
            console.sound(x * x, 0.5) # sounds.Death()
    console.clearkeys()
    console.print(27, 1, 'YOU HAVE DIED!!', Colors.Black, Colors.Code[level.Bb]) # Flashing, when possible
    while not console.keypressed():
        console.gotoxy(*player.position)
        if DeadDot: console.write('*', Colors.Code[Colors.Random()], Colors.Black)
        console.print(21, 25, 'Press any key to continue.')
    Border(level, console)
    High_Score(True, game, player, level, console)

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

def Convert_Format(player: PlayerState, level: Level, playfield: Playfield):
    level.SNum = 0
    level.MNum = 0
    level.FNum = 0
    level.GenNum = 0
    level.T[9] = -1
    level.LavaFlow = False
    level.TreeRate = 0
    level.GravCounter = 0
    level.GravOn = False
    playfield.parse(level.Fp)
    for m in range(1000):
        level.Sx[m] = 0
        level.Sy[m] = 0
        level.Mx[m] = 0
        level.My[m] = 0
        level.Fx[m] = 0
        level.Fy[m] = 0
    New_Gem_Color(level)
    for (x, y, monster) in playfield.coords_of([What.SlowMonster, What.MediumMonster, What.FastMonster, What.Generator]):
        if monster == What.SlowMonster:
            level.SNum += 1
            level.Sx[level.SNum] = x
            level.Sy[level.SNum] = y
        elif monster == What.MediumMonster:
            level.MNum += 1
            level.Mx[level.MNum] = x
            level.My[level.MNum] = y
        elif monster == What.FastMonster:
            level.FNum += 1
            level.Fx[level.FNum] = x
            level.Fy[level.FNum] = y
        elif monster == What.Generator:
            level.GenNum += 1
    
    players = playfield.coords_of(What.Player)
    if len(players) != 1:
        raise ValueError("Inappropriate number of players: {0}, expected 1.".format(len(players)))
    [(player_x, player_y, _)] = players
    player.position = (player_x, player_y)

def Go(XWay: int, YWay: int, Human: bool, game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    if level.Sideways and YWay == -1 and not game.OneMove and playfield.replacement != What.Rope:
        return
    previous = playfield.replacement
    (old_x, old_y) = player.position

    playfield[player.position] = playfield.replacement
    console.gotoxy(*player.position)
    console.write(' ')
    player.position = (player.position[0] + XWay, player.position[1] + YWay)
    if playfield[player.position] in WhatSets.becomes_replacement_with_go:
        playfield.replacement = playfield[player.position]
    else:
        playfield.replacement = What.Nothing
    if previous == What.Rope:
        console.gotoxy(old_x, old_y)
        console.write(VisibleTiles.Rope, Colors.LightGrey)
    playfield[player.position] = What.Player
    if level.T[5] < 1:
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Yellow, Colors.Black)
    else:
        console.gotoxy(*player.position)
        console.write(' ')
    if not level.Sideways:
        console.sounds(sounds.FootStep())
    elif playfield.replacement != What.Rope and Human:
        console.sounds(sounds.FootStep())
    if console.keypressed() and Human:
        ch = console.read()
        if ch == pygame.locals.K_ESCAPE:
            console.read()

def MoveRock(XWay: int, YWay: int):
    pass

def Trigger_Trap(Place: bool, i: int, ch: str):
    pass

def End_Routine(player: PlayerState, level: Level, console: Crt):
    console.sounds(sounds.FootStep())
    console.delay(200)
    console.sounds(sounds.FootStep())
    console.delay(300)
    console.sounds(sounds.FootStep())
    for x in range(1, 250):
        console.sound(randrange(3000) + x, 0.5) # sounds.Victory_Strange()
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Yellow, Colors.Code[Colors.RandomDark()])
        console.print(15, 25, 'Oh no, something strange is happening!', Colors.Code[Colors.Random()], Colors.Black)
    for i in range(2200, 20, -1):
        console.sound(randrange(i)) # Also sounds.Victory_Strage() - one sound covers the whole sequence
    for x in range(650):
        console.sound(x * 3, 2) # sounds.Victory_ScramblePlayer()
        console.gotoxy(*player.position)
        console.write(220 + randrange(4), Colors.Yellow, Colors.Black)
    console.gotoxy(*player.position)
    console.write(VisibleTiles.Stairs, Colors.Black, Colors.Green) # Flashing, when possible
    Restore_Border(level, console)
    console.alert(YTOP + 1, 'You are magically transported from Kroz!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    console.clearkeys()
    console.reset_colors()
    console.print(15, 25, 'Your gems are worth 100 points each...')
    for i in range(player.gems):
        player.score += 10
        Update_Info(level, console)
        console.sounds(sounds.Points_For_Gems(i))
    console.read()
    Restore_Border(level, console)
    console.clearkeys()
    console.print(15, 25, 'Your whips are worth 100 points each...')
    for i in range(player.whips):
        player.score += 10
        Update_Info(level, console)
        console.sounds(sounds.Points_For_Whips(i))
    console.read()
    Restore_Border(level, console)
    console.clearkeys()
    console.print(9, 25, 'Your Teleport Scrolls are woth 200 points each...')
    for i in range(player.teleports):
        player.score += 20
        Update_Info(level, console)
        console.sounds(sounds.Points_For_Teleports(i))
    console.read()
    Restore_Border(level, console)
    console.clearkeys()
    console.print(14, 25, 'Your Keys are worth 10,000 points each...')
    for i in range(player.keys):
        player.score += 1000
        Update_Info(level, console)
        console.sounds(sounds.Points_For_Keys(i))
    console.read()
    Restore_Border(level, console)
    console.clearkeys()
    for x in range(30):
        console.window(32 - x, 12 - x // 3, 35 + x, 14 + (x // 3))
        console.clrscr(Colors.Code[level.GemColor])
    for x in range(30):
        console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
        console.clrscr(Colors.Black)
        console.sound(x * 45, 3) # sounds.Level_Wipe()
    console.window(1, 1, 80, 25)
    console.window(2, 2, 65, 24)
    console.clrscr(Colors.Blue)
    console.default_colors(Colors.Yellow, Colors.Blue)
    console.gotoxy(25, 2)
    console.writeln('BACK AT YOUR HUT')
    console.gotoxy(25, 3)
    console.writeln('────────────────')
    console.writeln()
    console.default_colors(Colors.White)
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
    console.writeln('                         KINGDOM OF KROZ', Colors.Yellow)
    console.write  ('        ( Now available -- $7.50 or write for details. )')
    console.clearkeys()
    console.window(1, 1, 80, 25)
    console.default_colors(back = Colors.Black)
    console.alert(YTOP + 1, 'Press any key, Adventurer.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    Won(level, console)