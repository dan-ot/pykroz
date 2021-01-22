from random import randint
import pygame.locals

from ascii import ASCII
from levels import AddScore, Bak, Col, Flash, Game, Level, New_Gem_Color, Print, TMAX, TOTOBJECTS, Update_Info, VisibleTiles, XBOT, XSIZE, XTOP, YBOT, YSIZE, YTOP
from crt import Crt
import sounds

def Screen(game: Game, console: Crt):
    console.clearkeys()
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
    console.sounds(sounds.Color_Prompt())
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
    console.sounds(sounds.Speed_Prompt())
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
    level.Replacement = None
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
                            level.SNum += 1
                            level.Sx[level.SNum] = x_spot
                            level.Sy[level.SNum] = y_spot
                        elif obj == 2:
                            level.MNum += 1
                            level.Mx[level.MNum] = x_spot
                            level.My[level.MNum] = y_spot
                        elif obj == 3:
                            level.FNum += 1
                            level.Fx[level.FNum] = x_spot
                            level.Fy[level.FNum] = y_spot
                        elif obj == 36:
                            level.GenNum += 1

def Display_Playfield(level: Level, console: Crt):
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
                elif level.Pf[x_loop, y_loop] == 17: # River
                    if randint(15) == 0:
                        Col(15, 7, console)
                        Bak(4, 7, console)
                        console.write(VisibleTiles.Lava)
                        Bak(0, 0, console)
                    else:
                        Col(9, 0, console)
                        Bak(1, 7, console)
                        console.write(VisibleTiles.River)
                        Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 18: # Power
                    if randint(15) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Power)
                elif level.Pf[x_loop, y_loop] == 19: # Forest
                    Col(2, 7, console)
                    console.write(VisibleTiles.Forest)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 20 or level.Pf[x_loop, y_loop] == 252: # Tree
                    Col(6, 0, console)
                    Bak(2, 7, console)
                    console.write(VisibleTiles.Tree)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 21: # Bomb
                    if randint(40) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                    else:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Bomb)
                elif level.Pf[x_loop, y_loop] == 22: # Lava
                    Col(12, 16, console)
                    Bak(4, 7, console)
                    console.write(VisibleTiles.Lava)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 23: # Pit
                    Col(7, 7, console)
                    console.write(VisibleTiles.Pit)
                elif level.Pf[x_loop, y_loop] == 24: # Tome
                    Col(31, 31, console)
                    Bak(5, 0, console)
                    console.write(VisibleTiles.Tome)
                    Bak(0, 0, console)
                elif level.Pf[x_loop, y_loop] == 25: # Tunnel
                    Col(15, 7, console)
                    console.write(VisibleTiles.Tunnel)
                elif level.Pf[x_loop, y_loop] == 26: # Freeze
                    Col(11, 7, console)
                    console.write(VisibleTiles.Freeze)
                elif level.Pf[x_loop, y_loop] == 27: # Nugget
                    Col(14, 7, console)
                    console.write(VisibleTiles.Nugget)
                elif level.Pf[x_loop, y_loop] == 28: # Quake
                    if randint(15) == 0:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                # 29: IBlock
                # 30: IWall
                # 31: IDoor
                # 32: Stop
                # 33: Trap2
                elif level.Pf[x_loop, y_loop] == 34: # Zap
                    Col(12, 7, console)
                    console.write(VisibleTiles.Zap)
                elif level.Pf[x_loop, y_loop] == 35: # Create
                    if not level.HideCreate:
                        Col(15, 7, console)
                        console.write(VisibleTiles.Chance)
                elif level.Pf[x_loop, y_loop] == 36: # Generator
                    Col(30, 31, console)
                    console.write(VisibleTiles.Generator)
                # 37: Trap3
                elif level.Pf[x_loop, y_loop] == 38: # MBlock
                    if not level.HideMBlock:
                        Col(6, 7, console)
                        console.write(VisibleTiles.MBlock)
                # 39: Trap4
                elif level.Pf[x_loop, y_loop] == 40: # Player
                    Bak(7, 7, console)
                    Col(16, 16, console)
                    console.write(VisibleTiles.Stairs)
                    Bak(0, 0, console)
                # 41: ShowGems
                # 42:
                elif level.Pf[x_loop, y_loop] == 43: # ZBlock
                    Col(6, 7, console)
                    console.write(VisibleTiles.ZBlock)
                # 44: BlockSpell
                elif level.Pf[x_loop, y_loop] == 45: # Chance
                    Col(15, 7, console)
                    console.write(VisibleTiles.Chance)
                elif level.Pf[x_loop, y_loop] == 46: # Statue
                    Col(31, 23, console)
                    console.write(VisibleTiles.Statue)
                # 67: Trap5
                elif level.Pf[x_loop, y_loop] == 222: # ??
                    Col(15, 0, console)
                    Bak(6, 7, console)
                    console.write('!')
                    Bak(0, 0, console)
                # 224...231: Traps
                elif level.Pf[x_loop, y_loop] in [29, 30, 31, 32, 33, 37, 39, 41, 42, 44, 67, 224, 225, 226, 227, 228, 229, 230, 231]:
                    # Explained in comments above
                    pass
                else:
                    Col(15, 0, console)
                    Bak(6, 7, console)
                    console.write(ASCII.Char[level.Pf[x_loop, y_loop]].upper())
                    Bak(0, 0, console)
    level.FloorPattern = False

def BadKeySound(console: Crt):
    console.sounds(sounds.Bad_Key())

def GetKey(game: Game, level: Level, console: Crt) -> int:
    if console.keypressed():
        key = console.read()
        if key == pygame.locals.K_EQUALS or key == pygame.locals.K_KP_PLUS:
            game.FoundSet = []
            Flash(13, 25, 'Newly found object descriptions are reset.', level, console)
            return 0
        elif key == pygame.locals.K_MINUS or key == pygame.locals.K_KP_MINUS:
            game.FoundSet = [x for x in range(255)]
            Flash(10, 25, 'References to new objects will not be displayed.', level, console)
            return 0
        elif key == pygame.locals.K_9:
            level.Pf[level.Px + 1, level.Py] = 6 # Stairs!
            console.sounds(sounds.Generate_Stairs())
            return 0
        elif key == pygame.locals.K_0:
            level.Gems = 150
            level.Whips = 99
            level.Teleports = 99
            level.Keys = 9
            Update_Info(level, console)
            return 0
        elif key == pygame.locals.K_PAUSE or key == pygame.locals.K_p:
            return 80
        elif key == pygame.locals.K_ESCAPE or key == pygame.locals.K_q:
            return 81
        elif key == pygame.locals.K_r:
            return 82
        elif key == pygame.locals.K_s:
            return 83
        elif key == pygame.locals.K_t:
            return 84
        elif key == pygame.locals.K_w:
            return 87
        elif key == pygame.locals.K_u or key == pygame.locals.K_KP7:
            return 171
        elif key == pygame.locals.K_UP or key == pygame.locals.K_i or key == pygame.locals.K_KP8:
            return 172
        elif key == pygame.locals.K_o or key == pygame.locals.K_KP9:
            return 173
        elif key == pygame.locals.K_LEFT or key == pygame.locals.K_j or key == pygame.locals.K_KP4:
            return 175
        elif key == pygame.locals.K_RIGHT or key == pygame.locals.K_k or key == pygame.locals.K_KP6:
            return 177
        elif key == pygame.locals.K_n or key == pygame.locals.K_KP1:
            return 179
        elif key == pygame.locals.K_DOWN or key == pygame.locals.K_m or key == pygame.locals.K_KP2:
            return 180
        elif key == pygame.locals.K_COMMA or key == pygame.locals.K_KP4:
            return 181
        else:
            console.sounds(sounds.Bad_Key())
            return 0
    else:
        return 0

def Hit(x: int, y: int, ch: str, level: Level, console: Crt):
    # Remember what we're overwriting
    int_thing = level.Pf[x, y]
    char_thing = ASCII.Char[int_thing]

    # Swing the whip
    Bak(0, 0, console)
    for _ in range(45):
        Col(randint(16), 15, console)
        console.gotoxy(x, y)
        console.write(ch)

    # React to the hit, or restore the original, as appropriate
    console.gotoxy(x, y)
    if int_thing in [1, 2, 3]: # Monsters, they get killed
        level.Pf[x, y] = 0
        console.write(' ')
        level.Score += int_thing
        console.sounds(sounds.Whip_Hit())
    elif int_thing in [4, 19, 20, 252]: # Impediments, they might break
        i = level.WhipPower if int_thing != 19 else 8
        if int_thing == 4:
            char_thing = VisibleTiles.Block
        elif int_thing == 19:
            char_thing = VisibleTiles.Forest
        elif int_thing == 20 or int_thing == 252:
            char_thing = VisibleTiles.Tree
        if randint(7) < i: # A whip-power in 7 chance...
            console.write(' ')
            level.Pf[x, y] = 0
            console.sounds(sounds.Whip_Breakable_Destroy())
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            Col(6, 7, console)
            if char_thing == VisibleTiles.Tree:
                Col(6, 0, console)
                Bak(2, 7, console)
            elif char_thing == VisibleTiles.Forest:
                Col(2, 7, console)
            console.write(char_thing)
            if char_thing == VisibleTiles.Tree:
                Bak(0, 0, console)
    elif int_thing == 6: # Stairs
        Col(16, 16, console)
        Bak(7, 7, console)
        console.write(VisibleTiles.Stairs)
        Bak(0, 0, console)
    elif int_thing in [10, 15, 16, 18, 36, 48, 49, 50, 51]: # Things that break
        level.Pf[x, y] = 0
        console.write(' ')
        console.sounds(sounds.Whip_Breakable_Hit())
        if int_thing == 36:
            console.sounds(sounds.Whip_Breakable_Destroy())
            AddScore(36)
            level.GenNum -= 1

    # Things that don't break - if any were hidden under Chance symbols, they're revealed
    elif int_thing == 5:
        Col(15, 7, console)
        console.write(VisibleTiles.Whip)
    elif int_thing == 7:
        Col(14, 7, console)
        Bak(4, 0, console)
        console.write(VisibleTiles.Chest)
        Bak(0, 0, console)
    elif int_thing == 8:
        Col(11, 7)
        console.write(VisibleTiles.SlowTime)
    elif int_thing == 9:
        Col(level.GemColor, 7, console)
        console.write(VisibleTiles.Gem)
    elif int_thing == 11:
        Col(13, 7, console)
        console.write(VisibleTiles.Teleport)
    elif int_thing == 12:
        Col(12, 15, console)
        console.write(VisibleTiles.Key)
    elif int_thing == 13:
        Col(3, 0, console)
        Bak(5, 7, console)
        console.write(VisibleTiles.Door)
    elif int_thing in [14, 52, 53]: # Invisible walls become visible?
        Col(6, 7, console)
        console.write(VisibleTiles.Wall)
    elif int_thing == 54:
        Col(7, 7, console)
        console.write(VisibleTiles.Wall)
    elif int_thing == 17:
        Col(9, 0, console)
        Bak(1, 7, console)
        console.write(VisibleTiles.River)
        Bak(0, 0, console)
    elif int_thing == 21:
        Col(15, 7, console)
        console.write(VisibleTiles.Bomb)
    elif int_thing == 22:
        Col(12, 16, console)
        Bak(4, 7, console)
        console.write(VisibleTiles.Lava)
        Bak(0, 0, console)
    elif int_thing == 23:
        Col(7, 7, console)
        console.write(VisibleTiles.Wall)
    elif int_thing == 24:
        Col(31, 31, console)
        Bak(5, 0, console)
        console.write(VisibleTiles.Tome)
        Bak(0, 0, console)
    elif int_thing == 25:
        Col(15, 7, console)
        console.write(VisibleTiles.Tunnel)
    elif int_thing == 26:
        Col(11, 7, console)
        console.write(VisibleTiles.Freeze)
    elif int_thing == 27:
        Col(14, 7, console)
        console.write(VisibleTiles.Nugget)
    elif int_thing in [28, 29, 30, 31, 33, 37, 39, 41, 44, 67, 224, 225, 226, 227, 228, 229, 230, 231]:
        # Invisible things that stay invisible?
        Col(0, 0, console)
        Bak(0, 0, console)
        console.write(' ')
    elif int_thing == 32:
        level.Pf[x, y] = 0
        console.write(' ')
    elif int_thing == 34:
        Col(12, 7, console)
        console.write(VisibleTiles.Zap)
    elif int_thing == 35:
        Col(14, 7, console)
        console.write(VisibleTiles.Create)
    elif int_thing == 45:
        Col(15, 7, console)
        console.write(VisibleTiles.Chance)
    elif int_thing in [58, 59, 60]:
        Col(11, 7, console)
        console.write(VisibleTiles.OSpell1)
    elif int_thing == 66:
        Col(12, 0, console)
        Bak(4, 7, console)
        console.write(VisibleTiles.EWall)
        Bak(0, 0, console)
    elif int_thing in [47, 55, 56, 57, 61, 62, 63, 68, 69, 70, 71, 72, 73, 74]:
        console.write(' ')
    elif int_thing in [76, 77, 78, 79, 80]:
        Col(7, 7, console)
        console.write(VisibleTiles.DropRope)
    elif int_thing == 75:
        Col(7, 7, console)
        console.write(VisibleTiles.Rope)
    elif int_thing == 81:
        Col(31, 31, console)
        console.write(VisibleTiles.Amulet)
    elif int_thing == 82:
        Col(7, 7, console)
        console.write(VisibleTiles.ShootRight)
    elif int_thing == 83:
        Col(7, 7, console)
        console.write(VisibleTiles.ShootLeft)
    elif int_thing in [38, 43, 64]: # Breakable Walls?
        if randint(7) < level.WhipPower:
            console.write(' ')
            level.Pf[x, y] = 0
            console.sounds(sounds.Whip_Breakable_Destroy())
            AddScore(38)
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if int_thing == 64:
                Col(7, 7, console)
            else:
                Col(6, 7, console)
            console.write(VisibleTiles.Block)
    elif int_thing == 0:
        console.write(' ')
    else:
        Col(15, 0, console)
        Bak(6, 7, console)
        console.write(ASCII.Char[level.Pf[x, y]].upper())
        Bak(0, 0, console)

def Secret_Message():
    pass

def Shoot_Right(x_way: int, y_way: int, Human: bool):
    pass

def Shoot_Left(x_way: int, y_way: int, Human: bool):
    pass

def Tome_Message(level: Level, console: Crt):
    Flash(6, 25, ' You reach out to grab the object of your long quest... ', level, console)
    Flash(19, 25, ' the Magical Staff of Kroz. ', level, console)
    Flash(7, 25, ' Your budy surges with electricity as you clutch it! ')

def Tome_Effects(level: Level, console: Crt):
    Bak(0, 0, console)
    for b in range(14, 0, -1):
        for x in range (XBOT, XTOP):
            for y in range(YBOT, YTOP):
                if level.Pf[x, y] == 0:
                    console.sounds(sounds.Victory_MacGuffin_2(b, x, y))
                    console.gotoxy(x, y)
                    Col(b * 2, 7 if b % 2 == 1 else 0, console)
                    console.write(VisibleTiles.Wall)