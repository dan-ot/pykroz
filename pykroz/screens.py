from random import randint
import pygame.locals

from levels import Bak, ClearKeys, Col, Game, Level, New_Gem_Color, Print, TMAX, TOTOBJECTS, VisibleTiles, XBOT, XSIZE, XTOP, YBOT, YSIZE, YTOP
from crt import Crt

def Screen(game: Game, console: Crt):
    ClearKeys(console)
    game.Color = True
    Bak(0, 0, console)
    console.clrscr()
    Col(9, 9, console)
    console.gotoxy(31, 2)
    console.write('DUNGEONS OF KROZ II')
    console.gotoxy(18, 10)
    Col(15, 7, console)
    console.write('Is your screen Color or Monochrome (C/M)? C')
    console.gotoxy(console.cursor_x - 1, console.cursor_y)
    ch = console.read()
    console.sound(500, 30)
    if ch == pygame.locals.K_m:
        game.Color = False
    else:
        game.Color = True
    Bak(0, 0, console)
    console.gotoxy(18, 10)
    console.delline()
    console.gotoxy(9, 17)
    console.textcolor(7)
    console.write('If you have an older PC (like an XT model) choose "S" for Slow.')
    console.gotoxy(10, 19)
    console.write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.')
    console.gotoxy(32, 21)
    console.write('(Default = Slow)')
    Col(15, 15, console)
    console.gotoxy(28, 14)
    console.write('Slow or Fast PC (S/F)? S')
    console.gotoxy(console.cursor_x - 1, console.cursor_y)
    ch = console.read()
    console.sound(300, 30)
    if ch == pygame.locals.K_f:
        game.FastPC = True
    else:
        game.FastPC = False
    console.clrscr()

def Init_Screen(game: Game, level: Level, console: Crt):
    game.Restart = False
    level.Score = 0
    level.Level = 1
    level.Whips = 0
    level.Teleports = 0
    level.Keys = 0
    level.WhipPower = 2
    if game.Difficulty == 9:
        level.Gems = 250
        level.Whips = 100
        level.Teleports = 50
        level.Keys = 1
        level.WhipPower = 3
    elif game.Difficulty == 8:
        level.Gems = 20
        level.Whips = 10
    elif game.Difficulty == 5:
        level.Gems = 15
    elif game.Difficulty == 2:
        level.Gems = 10
    level.FloorPattern = False
    game.Replacement = None
    level.Bonus = 0
    level.LavaFlow = False
    level.LavaRate = 0
    level.Evaporate = 0
    level.MagicEWalls = False
    level.GravOn = False
    level.GravRate = 20
    level.GravCounter = 0
    level.TreeRate = -1
    if game.Difficulty == 2 or game.Difficulty == 9:
        game.FoundSet = [x for x in range(0, 255)]
    else:
        game.FoundSet = []
    level.GenNum = 0
    level.Sideways = False
    game.OneMove = False
    level.GenFactor = 17 # 28 for FastPC?
    if game.MixUp:
        level.Gems = 60
        level.Whips = 30
        level.Teleports = 15
        level.Keys = 2
        game.FoundSet = [x for x in range(0, TOTOBJECTS)]
    level.Px = randint(XSIZE) + XBOT
    level.Py = randint(YSIZE) + YBOT
    level.BTime = 2 # 9 for FastPC?
    level.STime = 3 # 10 for FastPC?
    level.MTime = 2 # 8 for FastPC?
    level.FTime = 1 # 6 for FastPC?
    level.SkipTime = 0
    for x in range(TMAX):
        level.T[x] = -1
    level.T[1] = 5
    level.T[2] = 6
    level.T[3] = 7
    level.T[8] = 6
    if game.Color:
        console.window(67, 1, 80, 25)
        Bak(1, 0, console)
        console.clrscr()
        console.window(1, 1, 80, 25)
    Col(14, 7, console)
    Print(71, 1, 'Score', console)
    Print(71, 4, 'Level', console)
    Print(71, 7, 'Gems', console)
    Print(71, 10, 'Whips', console)
    Print(69, 13, 'Teleports', console)
    Print(71, 16, 'Keys', console)
    Col(11, 7, console)
    Bak(4, 0, console)
    Print(70, 19, 'OPTIONS', console)
    Bak(1, 0, console)
    console.gotoxy(70, 20)
    Col(15, 15, console)
    console.write('W')
    Col(7, 7, console)
    console.write('hip')
    console.gotoxy(70, 21)
    Col(15, 15, console)
    console.write('T')
    Col(7, 7, console)
    console.write('eleport')
    console.gotoxy(70, 22)
    Col(15, 15, console)
    console.write('P')
    Col(7, 7, console)
    console.write('ause')
    console.gotoxy(70, 23)
    Col(15, 15, console)
    console.write('Q')
    Col(7, 7, console)
    console.write('uit')
    console.gotoxy(70, 24)
    Col(15, 15, console)
    console.write('S')
    Col(7, 7, console)
    console.write('ave')
    console.gotoxy(70, 25)
    Col(15, 15, console)
    console.write('R')
    Col(7, 7, console)
    console.write('estore')

def Parse_Field(game: Game, level: Level):
    slot = 1
    counter = 1
    while not counter > TOTOBJECTS:
        fetch = game.Df[level.Level][slot:slot + 3]
        level.Parsed[counter] = int(fetch)
        slot += 3
        counter += 1

def Create_Playfield(game: Game, level: Level):
    s_num = 0
    m_num = 0
    f_num = 0
    b_num = 0
    level.GenNum = 0
    level.LavaFlow = False
    level.T[9] = -1
    for x in range(1, 999):
        level.Sx[x] = 0
        level.Sy[x] = 0
        level.Mx[x] = 0
        level.My[x] = 0
        level.Fx[x] = 0
        level.Fy[x] = 0
    New_Gem_Color(level)
    for x in range(XBOT, XTOP):
        for y in range(YBOT, YTOP):
            level.Pf[x, y] = 0
    level.Pf[level.Px, level.Py] = 40
    Parse_Field(game, level)
    for obj in range(TOTOBJECTS):
        if level.Parsed[obj] > 0:
            for _ in range(level.Parsed[obj]):
                done = False
                while not done:
                    x_spot = randint(XSIZE) + XBOT
                    y_spot = randint(YSIZE) + YBOT
                    if level.Pf[x_spot, y_spot] == 0:
                        if obj == 1:
                            s_num += 1
                            level.Sx[s_num] = x_spot
                            level.Sy[s_num] = y_spot
                        elif obj == 2:
                            m_num += 1
                            level.Mx[m_num] = x_spot
                            level.My[m_num] = y_spot
                        elif obj == 3:
                            f_num += 1
                            level.Fx[f_num] = x_spot
                            level.Fy[f_num] = y_spot
                        elif obj == 36:
                            level.GenNum += 1

def Diplay_Playfield(level: Level, console: Crt):
    for x_loop in range(XBOT, XTOP):
        for y_loop in range(YBOT, YTOP):
            if (level.Pf[x_loop, y_loop] > 0 or level.FloorPattern) and (not level.HideLevel):
                console.gotoxy(x_loop, y_loop)
                if level.Pf[x_loop, y_loop] == 0: # Floor
                    Col(level.Cf1, level.Cf2, console)
                    Bak(level.Bf1, level.Bf2, console)
                    console.write(VisibleTiles.Tile)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 1: # Slow Monster
                    Col(12, 7, console)
                    console.write(VisibleTiles.SMonster)
                elif level.Pf[x_loop, y_loop] == 2: # Medium Monster
                    Col(10, 7, console)
                    console.write(VisibleTiles.MMonster)
                elif level.Pf[x_loop, y_loop] == 3: # Fast Monster
                    Col(9, 7, console)
                    console.write(VisibleTiles.FMonster)
                elif level.Pf[x_loop, y_loop] == 4: # Block
                    if level.Level != 71:
                        Col(6, 7, console)
                        console.write(VisibleTiles.Block)
                elif level.Pf[x_loop, y_loop] == 5: # Whip
                    Col(15, 7, console)
                    console.write(VisibleTiles.Whip)
                elif level.Pf[x_loop, y_loop] == 6: # Stairs
                    if not level.HideStairs:
                        Bak(7, 7, console)
                        Col(16, 16, console)
                        console.write(VisibleTiles.Stairs)
                        Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 7: # Chest
                    if randint(20) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(14, 7, console)
                        Bak(4, 0, console)
                        console.write(VisibleTiles.Chest)
                        Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 8: # Slow Time
                    if randint(35) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(11, 7)
                        console.write(VisibleTiles.SlowTime)
                elif level.Pf[x_loop, y_loop] == 9: # Gem
                    if not level.HideGems:
                        Col(level.GemColor, 7, console)
                        console.write(VisibleTiles.Gem)
                elif level.Pf[x_loop, y_loop] == 10: # Invisible
                    Col(2, 7, console)
                    console.write(VisibleTiles.Invisible)
                elif level.Pf[x_loop, y_loop] == 11: # Teleport
                    Col(13, 7, console)
                    console.write(VisibleTiles.Teleport)
                elif level.Pf[x_loop, y_loop] == 12: # Key
                    if randint(25) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(12, 15, console)
                        console.write(VisibleTiles.Key)
                elif level.Pf[x_loop, y_loop] == 13: # Door
                    Bak(5, 7, console)
                    Col(3, 0, console)
                    console.write(VisibleTiles.Door)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 14: # Wall
                    Col(6, 7, console)
                    console.write(VisibleTiles.Wall)
                elif level.Pf[x_loop, y_loop] == 15: # SpeedTime
                    if randint(10) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(11, 7, console)
                        console.write(VisibleTiles.SpeedTime)
                elif level.Pf[x_loop, y_loop] == 16: # Trap
                    if not level.HideTrap:
                        Col(7, 7, console)
                        console.write(VisibleTiles.Trap)
                
