# System Libraries
from typing import Sequence, Tuple
from random import randrange
from pathlib import Path
import json
from enum import Flag, auto

# Engine Libraries
import pygame.constants
import pygame.key
from pygame import Color

# Project Libraries
from display.game_display import GameDisplay
from engine.crt import Crt
from engine.colors import Colors
from playerstate import PlayerState
from playfield import Playfield
from pieces import VisibleTiles, What, WhatSets
import sounds

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
        self.name = name
        self.high_score = highScore
        self.high_level = highLevel

class SaveType:
    def __init__(self):
        self.level: int = 1
        self.score: int = 0
        self.gems: int = 0
        self.whips: int = 0
        self.teleports: int = 0
        self.keys: int = 0
        self.whip_power: int = 0
        self.difficulty: int = 0
        self.px: int = 0
        self.py: int = 0
        self.found_set: list[int] = []
        self.mix_up: bool = False

class VisibilityFlags(Flag):
    SHOW_ALL = 0
    FLOOR_PATTERN = auto()
    HIDE_ROCK = auto()
    HIDE_STAIRS = auto()
    HIDE_LEVEL = auto()
    HIDE_CREATE = auto()
    HIDE_OPEN_WALL = auto()
    HIDE_TRAP = auto()
    HIDE_GEMS = auto()
    HIDE_M_BLOCK = auto()

    def __contains__(self, flags: "VisibilityFlags") -> bool:
        return self & flags == flags

# Unit-level State
class Level:
    def __init__(self):
        # TODO: deprecated, now part of GameDisplay system
        self.Bc: Color = Colors.Black
        self.Bb: Color = Colors.Black
        self.GemColor: Color = Colors.Black
        # Floor colors
        # TODO: deprecated
        self.Cf1: Color = Colors.Black
        self.Cf2: Color = Colors.Black
        self.Bf1: Color = Colors.Black
        self.Bf2: Color = Colors.Black
        # slow monsters
        self.slow_monsters: list[Tuple[int, int]] = []
        self.slow_monster_timer: float = 0.0
        self.slow_monster_timer_base: float = 3.0
        # medium monsters
        self.medium_monsters: list[Tuple[int, int]] = []
        self.medium_monster_timer: float = 0.0
        self.medium_monster_timer_base: float = 2.0
        # fast monsters
        self.fast_monsters: list[Tuple[int, int]] = []
        self.fast_monster_timer: float = 0.0
        self.fast_monster_timer_base: float = 1.0
        # string definition of the levels for parsing
        self.GenNum: int = 0
        # Timers:
        self.SkipTime: int = 0
        self.T: dict[int, int] = {
            4: 0, # slow time
            5: 0, # invisibility
            6: 0, # fast time
            7: 0, # freeze
            8: 0  # don't know yet
        }
        self.LavaFlow: bool = False
        self.LavaRate: int = 0
        self.TreeRate: int = -1
        self.Evaporate: int = 0
        self.GravCounter: int = 0
        self.GravOn: bool = False
        self.GravRate: int = 0
        self.Sideways: bool = False
        self.Bonus: int = 0
        self.visibility: VisibilityFlags = VisibilityFlags.SHOW_ALL
        self.MagicEWalls: bool = False
        self.GenFactor: int = 17
        self.BTime: int = 2
        self.initial: SaveType = SaveType()

class LiteralLevel():
    def __init__(self, lines: Sequence[str]):
        self.lines = list(lines)

class RandomLevel():
    def __init__(self, width: int, height: int, what_counts: Sequence[Tuple[What, int]]):
        self.what_counts = what_counts
        self.width = width
        self.height = height

class Game:
    def __init__(self):
        self.HSList: list[HSType] = [HSType('', 0, 0) for _ in range(1, 15)]
        self.Restart: bool = False
        self.OneMove: bool = True
        self.Difficulty: int = 0
        self.MixUp: bool = True
        self.FastPC: bool = True
        self.FoundSet: set[What] = set()

# Procedures
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
    console.writeln('??? The six Kroz games! CAVERNS OF KROZ, KINGDOM OF KROZ, DUNGEONS OF KROZ,')
    console.writeln('     RETURN TO KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.')
    console.writeln('     Each volume is just $7.50, or order all six for $35!')
    console.writeln()
    console.default_colors(Colors.LightGrey)
    console.writeln('??? SUPERNOVA - Explore a galaxy and save a planet from an exploding star!')
    console.writeln('     An epic adventure rated by Shareware Magazine as one of the best games')
    console.writeln('     ever! Highly advanced game has graphics, sound effects galore, clue')
    console.writeln('     command, and dozens of unique features. ($10)')
    console.writeln()
    console.writeln('??? BEYOND THE TITANIC - A fantastic adventure of exploration and survival.')
    console.writeln('     What really happened? Sound effects and 16 color screens.  ($8)')
    console.writeln()
    console.writeln('??? WORD WHIZ - New game that challenges your knowledge of the English')
    console.writeln('     language.  Fun to play, yet very education, too.  ($5)')
    console.writeln()
    console.default_colors(Colors.White)
    console.writeln('??? THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best')
    console.write  ('     levels yet!  Built-in contest!  New features galore.  ($20)')
    console.clearkeys()
    console.halt()

def Shareware(console: Crt, Wait: bool):
    console.default_colors(Colors.White, Colors.Blue)
    console.clrscr()
    console.gotoxy(22, 1)
    console.writeln('DUNGEONS OF KROZ II ??? HOW TO REGISTER')
    console.gotoxy(1, 2)
    for _ in range(1, 80):
        console.write('???')
    console.gotoxy(1, 3)
    console.default_colors(Colors.LightGrey)
    console.writeln('  This is not a shareware game, but it is user-supported.  If you enjoy this')
    console.writeln('game you are asked by the author to please send a registration check in the')
    console.writeln('amount of $7.50 to Apogee Software.')
    console.writeln('  This registration fee will qualify you to order any of the other Kroz')
    console.writeln('volumes available:')
    console.writeln()
    console.default_colors(Colors.White)
    console.write('  ??? Caverns of Kroz   - the first discovery of Kroz')
    console.write('  ??? Dungeons of Kroz  - the dark side of Kroz, fast-paced action')
    console.write('  ??? Kingdom of Kroz   - the national contest winner ("Best Game" in 1988)')
    console.write('  ??? Return to Kroz    - the discovery of entirely new underground chambers')
    console.write('  ??? Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems')
    console.write('  ??? The Final Crusade of Kroz - the suprising finish?')
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
    # TODO: prompt
    console.gotoxy(27, 25)
    console.write('Press any key to continue.', Colors.White, Colors.RandomDark()) # Flashing when possible
    console.clearkeys()
    while not console.keypressed():
        pass
    console.clearkeys()
    console.reset_colors()
    console.clrscr()

# TODO: Move to GameDisplay
def Won(game: Game, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    display.new_border_color()
    console.clearkeys()
    console.print(5, 1, 'YOUR QUEST FOR THE MAGICAL STAFF OF KROZ WAS SUCCESSFUL!!', Colors.White, level.Bb) # Flashing when possible
    High_Score(False, game, player, level, console)

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
        if player.score > game.HSList[place].high_score:
            stop = True
            place += 1
        if stop is False and place > 15:
            place = 100
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
        console.write(game.HSList[x].name)
        console.gotoxy(36, x + 6)
        console.write('{0}0'.format(game.HSList[x].high_score) if game.HSList[x].high_score > 0 else '0')
        console.gotoxy(50, x + 6)
        console.write('{0}'.format(game.HSList[x].high_level))
    console.clearkeys()
    if place < 16:
        console.gotoxy(16, place + 6)
        console.write('               ', back = Colors.Red)
        console.gotoxy(16, 23)
        console.write('Enter your name then press <enter>.', Colors.Red, Colors.LightGrey)
        console.gotoxy(16, place + 6)
        console.default_colors(Colors.White, Colors.Red)
        game.HSList[place].name = console.readln()
        with hsFile.open('w') as f:
            json.dump(game.HSList, f)
    console.reset_colors()
    console.gotoxy(16, 23)
    console.write('                                   ')
    level.slow_monsters = []
    level.medium_monsters = []
    level.fast_monsters = []
    if PlayAgain:
        console.alert(YTOP + 1, 'Do you want to play another game (Y/N)?', level.Bc, level.Bb)
        ch = pygame.key.name(console.read())
    else:
        console.alert(YTOP + 1, 'Press any key to continue.', level.Bc, level.Bb)
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

def Dead(DeadDot: bool, game: Game, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    # TODO: Handled by GameDisplay
    if player.gems > 9:
        console.default_colors(Colors.Red, Colors.LightGrey)
    else:
        player.gems = 0
        console.default_colors(Colors.LightRed, Colors.DarkGrey) # Flashing, when possible
    console.gotoxy(71, 8)
    console.write('     ')
    strVal = '{0}'.format(player.gems)
    console.gotoxy(73 - len(strVal) // 2, 8)
    console.write(strVal)
    if DeadDot:
        for x in range(150, 5, -1):
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Code[x % len(Colors.Code)], Colors.RandomDark())
            console.sound(x * x, 0.5) # sounds.Death()
    console.clearkeys()
    console.print(27, 1, 'YOU HAVE DIED!!', Colors.Black, level.Bb) # Flashing, when possible
    while not console.keypressed():
        console.gotoxy(*player.position)
        if DeadDot:
            console.write('*', Colors.Random(), Colors.Black)
        console.print(21, 25, 'Press any key to continue.')
    display.new_border_color()
    High_Score(True, game, player, level, console)

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
        if ch == pygame.constants.K_ESCAPE:
            console.read()

def MoveRock(XWay: int, YWay: int):
    pass

def Trigger_Trap(Place: bool, i: int, ch: str):
    pass

def End_Routine(game: Game, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    console.sounds(sounds.FootStep())
    console.delay(200)
    console.sounds(sounds.FootStep())
    console.delay(300)
    console.sounds(sounds.FootStep())
    for x in range(1, 250):
        console.sound(randrange(3000) + x, 0.5) # sounds.Victory_Strange()
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Yellow, Colors.RandomDark())
        # TODO: Writing the border here...
        console.print(15, 25, 'Oh no, something strange is happening!', Colors.Random(), Colors.Black)
    for i in range(2200, 20, -1):
        console.sound(randrange(i), 3) # Also sounds.Victory_Strage() - one sound covers the whole sequence
    for x in range(650):
        console.sound(x * 3, 2) # sounds.Victory_ScramblePlayer()
        console.gotoxy(*player.position)
        console.write(220 + randrange(4), Colors.Yellow, Colors.Black)
    console.gotoxy(*player.position)
    console.write(VisibleTiles.Stairs, Colors.Black, Colors.Green) # Flashing, when possible
    console.alert(YTOP + 1, 'You are magically transported from Kroz!', level.Bc, level.Bb)
    console.clearkeys()
    console.reset_colors()
    # TODO: Writing in the border here...
    console.print(15, 25, 'Your gems are worth 100 points each...')
    for i in range(player.gems):
        player.score += 10
        display.mark_player_dirty()
        console.sounds(sounds.Points_For_Gems(i))
    console.read()
    console.clearkeys()
    # TODO: Writing in the border here...
    console.print(15, 25, 'Your whips are worth 100 points each...')
    for i in range(player.whips):
        player.score += 10
        display.mark_player_dirty()
        console.sounds(sounds.Points_For_Whips(i))
    console.read()
    console.clearkeys()
    # TODO: Writing in the border here...
    console.print(9, 25, 'Your Teleport Scrolls are woth 200 points each...')
    for i in range(player.teleports):
        player.score += 20
        display.mark_player_dirty()
        console.sounds(sounds.Points_For_Teleports(i))
    console.read()
    console.clearkeys()
    # TODO: Writing in the border here...
    console.print(14, 25, 'Your Keys are worth 10,000 points each...')
    for i in range(player.keys):
        player.score += 1000
        display.mark_player_dirty()
        console.sounds(sounds.Points_For_Keys(i))
    console.read()
    console.clearkeys()
    for x in range(30):
        console.window(32 - x, 12 - x // 3, 35 + x, 14 + (x // 3))
        console.clrscr(level.GemColor)
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
    console.writeln('????????????????????????????????????????????????')
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
    console.alert(YTOP + 1, 'Press any key, Adventurer.', level.Bc, level.Bb)
    Won(game, player, level, display, console)
