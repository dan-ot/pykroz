from random import randrange

import pygame.constants

from engine.colors import Colors
from engine.ascii import ASCII
from engine.crt import ColorMode, Crt
from playerstate import PlayerState
from pieces import What, WhatSets, score_for
from levels import Game, Level, TMAX, VisibilityFlags, VisibleTiles, YTOP
from playfield import Playfield
import sounds

def Screen(game: Game, console: Crt):
    console.clearkeys()
    console.reset_colors()
    console.clrscr()
    console.gotoxy(31, 2)
    console.write('DUNGEONS OF KROZ II', Colors.DarkGrey)
    console.gotoxy(18, 10)
    console.write('Is your screen Color or Monochrome (C/M)? C')
    console.gotoxy(console.cursor_x - 1, console.cursor_y)
    ch = console.read()
    console.sounds(sounds.Color_Prompt())
    if ch == pygame.constants.K_m:
        console.color_mode = ColorMode.BLACK_AND_WHITE
    else:
        console.color_mode = ColorMode.COLOR_PALLETTE
    console.gotoxy(18, 10)
    console.delline()
    console.gotoxy(9, 17)
    console.default_colors(Colors.LightGrey)
    console.write('If you have an older PC (like an XT model) choose "S" for Slow.')
    console.gotoxy(10, 19)
    console.write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.')
    console.gotoxy(32, 21)
    console.write('(Default = Slow)')
    console.default_colors(Colors.White)
    console.gotoxy(28, 14)
    console.write('Slow or Fast PC (S/F)? S')
    console.gotoxy(console.cursor_x - 1, console.cursor_y)
    ch = console.read()
    console.sounds(sounds.Speed_Prompt())
    if ch == pygame.constants.K_f:
        game.FastPC = True
    else:
        game.FastPC = False
    console.clrscr()

def Init_Screen(game: Game, player: PlayerState, console: Crt):
    game.Restart = False
    player.score = 0
    player.level = 1
    player.whips = 0
    player.teleports = 0
    player.keys = 0
    player.whip_power = 2
    if game.Difficulty == 9:
        player.gems = 250
        player.whips = 100
        player.teleports = 50
        player.keys = 1
        player.whip_power = 3
    elif game.Difficulty == 8:
        player.gems = 20
        player.whips = 10
    elif game.Difficulty == 5:
        player.gems = 15
    elif game.Difficulty == 2:
        player.gems = 10
    if game.Difficulty == 2 or game.Difficulty == 9:
        game.FoundSet = set(What)
    else:
        game.FoundSet = set()
    game.OneMove = False
    if game.MixUp:
        player.gems = 60
        player.whips = 30
        player.teleports = 15
        player.keys = 2
        game.FoundSet = WhatSets.auto_discover_on_mixup.copy()
    player.position = (0, 0)
    # TODO: Handled by StatsDisplay natively.
    console.window(67, 1, 80, 25)
    console.default_colors(Colors.Yellow, Colors.Blue)
    console.clrscr()
    console.window(1, 1, 80, 25)
    console.print(71, 1, 'Score')
    console.print(71, 4, 'Level')
    console.print(71, 7, 'Gems')
    console.print(71, 10, 'Whips')
    console.print(69, 13, 'Teleports')
    console.print(71, 16, 'Keys')
    console.print(70, 19, 'OPTIONS', Colors.LightCyan, Colors.Red)
    console.gotoxy(70, 20)
    console.default_colors(Colors.LightGrey)
    console.write('W', Colors.White)
    console.write('hip')
    console.gotoxy(70, 21)
    console.write('T', Colors.White)
    console.write('eleport')
    console.gotoxy(70, 22)
    console.write('P', Colors.White)
    console.write('ause')
    console.gotoxy(70, 23)
    console.write('Q', Colors.White)
    console.write('uit')
    console.gotoxy(70, 24)
    console.write('S', Colors.White)
    console.write('ave')
    console.gotoxy(70, 25)
    console.write('R', Colors.White)
    console.write('estore')

# TODO: This should be some mix of Whatness and result...
def Hit(x: int, y: int, ch: str, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    # Remember what we're overwriting
    what_thing = playfield[x, y]
    char_thing = ASCII.Char[int(what_thing)]

    # Swing the whip
    console.reset_colors()
    for _ in range(45):
        console.gotoxy(x, y)
        console.write(ch, Colors.Random())

    # React to the hit, or restore the original, as appropriate
    console.gotoxy(x, y)
    if what_thing in WhatSets.monsters: # Monsters, they get killed
        playfield[x, y] = What.Nothing
        console.write(' ')
        player.score += int(what_thing)
        console.sounds(sounds.Whip_Hit())
    elif what_thing in WhatSets.breakable_obstacles: # Impediments, they might break
        i = player.whip_power if what_thing != What.Forest else 8
        if what_thing == What.Breakable_Wall:
            char_thing = VisibleTiles.Breakable_Wall
        elif what_thing == What.Forest:
            char_thing = VisibleTiles.Forest
        elif what_thing in (What.Tree, What.Tree_2):
            char_thing = VisibleTiles.Tree
        if randrange(7) < i: # A whip-power in 7 chance...
            console.write(' ')
            playfield[x, y] = What.Nothing
            console.sounds(sounds.Whip_Breakable_Destroy())
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if char_thing == VisibleTiles.Tree:
                console.write(char_thing, Colors.Brown, Colors.Green)
            elif char_thing == VisibleTiles.Forest:
                console.write(char_thing, Colors.Green)
    elif what_thing == What.Stairs: # Stairs
        console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing when possible
    elif what_thing in WhatSets.breakable_things: # Things that break
        playfield[x, y] = What.Nothing
        console.write(' ')
        console.sounds(sounds.Whip_Breakable_Hit())
        if what_thing == What.Generator:
            console.sounds(sounds.Whip_Breakable_Destroy())
            player.add_score(score_for(What.Generator, player.level))
            level.GenNum -= 1

    # Things that don't break - if any were hidden under Chance symbols, they're revealed
    elif what_thing == What.Whip:
        console.write(VisibleTiles.Whip, Colors.White)
    elif what_thing == What.Chest:
        console.write(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
    elif what_thing == What.SlowTime:
        console.write(VisibleTiles.SlowTime, Colors.LightCyan)
    elif what_thing == What.Gem:
        console.write(VisibleTiles.Gem, level.GemColor)
    elif what_thing == What.TeleportScroll:
        console.write(VisibleTiles.Teleport, Colors.LightMagenta)
    elif what_thing == What.Key:
        console.write(VisibleTiles.Key, Colors.LightRed)
    elif what_thing == What.Door:
        console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
    elif what_thing in WhatSets.wall_variants: # Invisible walls become visible?
        console.write(VisibleTiles.Wall, Colors.Brown)
    elif what_thing == What.Wall_Grey:
        console.write(VisibleTiles.Wall, Colors.LightGrey)
    elif what_thing == What.River:
        console.write(VisibleTiles.River, Colors.LightBlue, Colors.Blue)
    elif what_thing == What.Bomb:
        console.write(VisibleTiles.Bomb, Colors.White)
    elif what_thing == What.Lava:
        console.write(VisibleTiles.Lava, Colors.LightRed, Colors.Red)
    elif what_thing == What.Pit:
        console.write(VisibleTiles.Pit, Colors.LightGrey)
    elif what_thing == What.Tome:
        console.write(VisibleTiles.Tome, Colors.White, Colors.Magenta) # Flashing when possible
    elif what_thing == What.Tunnel:
        console.write(VisibleTiles.Tunnel, Colors.White)
    elif what_thing == What.Freeze:
        console.write(VisibleTiles.Freeze, Colors.LightCyan)
    elif what_thing == What.Nugget:
        console.write(VisibleTiles.Nugget, Colors.Yellow)
    elif what_thing in WhatSets.invisible_to_whip:
        # Invisible things that stay invisible?
        console.write(' ', Colors.Black, Colors.Black)
    elif what_thing == What.Stop:
        playfield[x, y] = What.Nothing
        console.write(' ')
    elif what_thing == What.Zap:
        console.write(VisibleTiles.Zap, Colors.LightRed)
    elif what_thing == What.Create:
        console.write(VisibleTiles.Create, Colors.Yellow)
    elif what_thing == What.Chance:
        console.write(VisibleTiles.Chance, Colors.White)
    elif what_thing in WhatSets.ospell_1s:
        console.write(VisibleTiles.OSpell1, Colors.LightCyan)
    elif what_thing == What.EWall:
        console.write(VisibleTiles.EWall, Colors.LightRed, Colors.Red)
    elif what_thing in WhatSets.invisible_to_whip_2:
        console.write(' ')
    elif what_thing in WhatSets.drop_ropes:
        console.write(VisibleTiles.DropRope, Colors.LightGrey)
    elif what_thing == What.Rope:
        console.write(VisibleTiles.Rope, Colors.LightGrey)
    elif what_thing == What.Amulet:
        console.write(VisibleTiles.Amulet, Colors.White) # Flashing when possible
    elif what_thing == What.ShootRight:
        console.write(VisibleTiles.ShootRight, Colors.LightGrey)
    elif what_thing == What.ShootLeft:
        console.write(VisibleTiles.ShootLeft, Colors.LightGrey)
    elif what_thing in WhatSets.breakable_wall_variants: # Breakable Walls?
        if randrange(7) < player.whip_power:
            console.write(' ')
            playfield[x, y] = What.Nothing
            console.sounds(sounds.Whip_Breakable_Destroy())
            player.add_score(score_for(What.MBlock, player.level))
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if what_thing == What.Breakable_Wall_Grey:
                console.write(VisibleTiles.Breakable_Wall, Colors.LightGrey)
            else:
                console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
    elif what_thing == What.Nothing:
        console.write(' ')
    else:
        console.write(ASCII.Char[int(playfield[x, y])].upper(), Colors.White, Colors.Brown)

def Secret_Message():
    pass

def Shoot_Right(x_way: int, y_way: int, Human: bool):
    pass

def Shoot_Left(x_way: int, y_way: int, Human: bool):
    pass

def Tome_Message(level: Level, console: Crt):
    console.alert(YTOP + 1, ' You reach out to grab the object of your long quest... ', level.Bc, level.Bb)
    console.alert(YTOP + 1, ' the Magical Staff of Kroz. ', level.Bc, level.Bb)
    console.alert(YTOP + 1, ' Your body surges with electricity as you clutch it! ', level.Bc, level.Bb)

def Tome_Effects(playfield: Playfield, console: Crt):
    console.reset_colors()
    for b in range(14, 0, -1):
        for x in range(playfield.bounds().width):
            for y in range(playfield.bounds().height):
                if playfield[x, y] == What.Nothing:
                    console.sounds(sounds.Victory_MacGuffin_2(b, x, y))
                    console.gotoxy(x, y)
                    console.write(VisibleTiles.Wall, Colors.Code[(b * 2) % len(Colors.Code)])
