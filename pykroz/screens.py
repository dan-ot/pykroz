from pieces import What, WhatSets
from colors import Colors
from random import randrange
import pygame.locals

from ascii import ASCII
from levels import AddScore, Game, Level, New_Gem_Color, TMAX, TOTOBJECTS, VisibleTiles, XBOT, XSIZE, XTOP, YBOT, YSIZE, YTOP
from crt import ColorMode, Crt
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
    if ch == pygame.locals.K_m:
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
        game.FoundSet = set([w for w in What])
    else:
        game.FoundSet = set()
    level.GenNum = 0
    level.Sideways = False
    game.OneMove = False
    level.GenFactor = 17 # 28 for FastPC?
    if game.MixUp:
        level.Gems = 60
        level.Whips = 30
        level.Teleports = 15
        level.Keys = 2
        game.FoundSet = WhatSets.auto_discover_on_mixup.copy()
    level.Px = randrange(XSIZE) + XBOT
    level.Py = randrange(YSIZE) + YBOT
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
            level.Pf[x][y] = What.Nothing
    level.Pf[level.Px][level.Py] = What.Player
    Parse_Field(game, level)
    for obj in range(TOTOBJECTS):
        if level.Parsed[obj] > 0:
            for _ in range(level.Parsed[obj]):
                done = False
                while not done:
                    x_spot = randrange(XSIZE) + XBOT
                    y_spot = randrange(YSIZE) + YBOT
                    if level.Pf[x_spot][y_spot] == What.Nothing:
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
    console.reset_colors()
    for x_loop in range(XBOT, XTOP):
        for y_loop in range(YBOT, YTOP):
            if (level.Pf[x_loop][y_loop] is not What.Nothing or level.FloorPattern) and (not level.HideLevel):
                console.gotoxy(x_loop, y_loop)
                if level.Pf[x_loop][y_loop] == What.Nothing: # Floor
                    console.write(VisibleTiles.Tile, Colors.Code[level.Cf1], Colors.Code[level.Bf1])
                elif level.Pf[x_loop][y_loop] == What.SlowMonster: # Slow Monster
                    console.write(VisibleTiles.SMonster_1, Colors.LightRed)
                elif level.Pf[x_loop][y_loop] == What.MediumMonster: # Medium Monster
                    console.write(VisibleTiles.MMonster_1, Colors.LightGreen)
                elif level.Pf[x_loop][y_loop] == What.FastMonster: # Fast Monster
                    console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
                elif level.Pf[x_loop][y_loop] == What.Breakable_Wall: # Block
                    if level.Level != 71:
                        console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
                elif level.Pf[x_loop][y_loop] == What.Whip: # Whip
                    console.write(VisibleTiles.Whip, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Stairs: # Stairs
                    if not level.HideStairs:
                        console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing, when possible
                elif level.Pf[x_loop][y_loop] == What.Chest: # Chest
                    if randrange(20) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
                elif level.Pf[x_loop][y_loop] == What.SlowTime: # Slow Time
                    if randrange(35) == 0:
                        console.write(VisibleTiles.Chance, Colors.Yellow)
                    else:
                        console.write(VisibleTiles.SlowTime, Colors.LightCyan)
                elif level.Pf[x_loop][y_loop] == What.Gem: # Gem
                    if not level.HideGems:
                        console.write(VisibleTiles.Gem, Colors.Code[level.GemColor])
                elif level.Pf[x_loop][y_loop] == What.Invisibility: # Invisible
                    console.write(VisibleTiles.Invisible, Colors.Blue)
                elif level.Pf[x_loop][y_loop] == What.TeleportScroll: # Teleport
                    console.write(VisibleTiles.Teleport, Colors.LightMagenta)
                elif level.Pf[x_loop][y_loop] == What.Key: # Key
                    if randrange(25) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Key, Colors.LightRed)
                elif level.Pf[x_loop][y_loop] == What.Door: # Door
                    console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
                elif level.Pf[x_loop][y_loop] == What.Wall: # Wall
                    console.write(VisibleTiles.Wall, Colors.Brown)
                elif level.Pf[x_loop][y_loop] == What.SpeedTime: # SpeedTime
                    if randrange(10) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.SpeedTime, Colors.LightCyan)
                elif level.Pf[x_loop][y_loop] == What.TeleportTrap: # Trap
                    if not level.HideTrap:
                        console.write(VisibleTiles.Trap, Colors.LightGrey)
                elif level.Pf[x_loop][y_loop] == What.River: # River
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Lava, Colors.White, Colors.Red)
                    else:
                        console.write(VisibleTiles.River, Colors.LightBlue, Colors.Blue)
                elif level.Pf[x_loop][y_loop] == What.WhipPower: # Power
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Power, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Forest: # Forest
                    console.write(VisibleTiles.Forest, Colors.Green)
                elif level.Pf[x_loop][y_loop] == What.Tree or level.Pf[x_loop, y_loop] == What.Tree_2: # Tree
                    console.write(VisibleTiles.Tree, Colors.Brown, Colors.Green)
                elif level.Pf[x_loop][y_loop] == What.Bomb: # Bomb
                    if randrange(40) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Bomb, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Lava: # Lava
                    console.write(VisibleTiles.Lava, Colors.LightRed, Colors.Red)
                elif level.Pf[x_loop][y_loop] == What.Pit: # Pit
                    console.write(VisibleTiles.Pit, Colors.LightGrey)
                elif level.Pf[x_loop][y_loop] == What.Tome: # Tome
                    console.write(VisibleTiles.Tome, Colors.White, Colors.Magenta) # Flashing when possible
                elif level.Pf[x_loop][y_loop] == What.Tunnel: # Tunnel
                    console.write(VisibleTiles.Tunnel, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Freeze: # Freeze
                    console.write(VisibleTiles.Freeze, Colors.LightGreen)
                elif level.Pf[x_loop][y_loop] == What.Nugget: # Nugget
                    console.write(VisibleTiles.Nugget, Colors.Yellow)
                elif level.Pf[x_loop][y_loop] == What.Quake: # Quake
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                # 29: IBlock
                # 30: IWall
                # 31: IDoor
                # 32: Stop
                # 33: Trap2
                elif level.Pf[x_loop][y_loop] == What.Zap: # Zap
                    console.write(VisibleTiles.Zap, Colors.LightRed)
                elif level.Pf[x_loop][y_loop] == What.Create: # Create
                    if not level.HideCreate:
                        console.write(VisibleTiles.Chance, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Generator: # Generator
                    console.write(VisibleTiles.Generator, Colors.Yellow) # Flashing when possible
                # 37: Trap3
                elif level.Pf[x_loop][y_loop] == What.MBlock: # MBlock
                    if not level.HideMBlock:
                        console.write(VisibleTiles.MBlock, Colors.Brown)
                # 39: Trap4
                elif level.Pf[x_loop][y_loop] == What.Player: # Player
                    console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing when possible
                # 41: ShowGems
                # 42:
                elif level.Pf[x_loop][y_loop] == What.ZBlock: # ZBlock
                    console.write(VisibleTiles.ZBlock, Colors.Brown)
                # 44: BlockSpell
                elif level.Pf[x_loop][y_loop] == What.Chance: # Chance
                    console.write(VisibleTiles.Chance, Colors.White)
                elif level.Pf[x_loop][y_loop] == What.Statue: # Statue
                    console.write(VisibleTiles.Statue, Colors.White) # Flashing, when possible
                # 67: Trap5
                elif level.Pf[x_loop][y_loop] == What.ExclamationPoint: # ??
                    console.write('!', Colors.White, Colors.Brown)
                # 224...231: Traps
                elif level.Pf[x_loop][y_loop] in WhatSets.invisible:
                    # Explained in comments above
                    pass
                else:
                    console.write(ASCII.Char[int(level.Pf[x_loop][y_loop])].upper(), Colors.White, Colors.Brown)
    level.FloorPattern = False

def Hit(x: int, y: int, ch: str, level: Level, console: Crt):
    # Remember what we're overwriting
    what_thing = level.Pf[x][y]
    char_thing = ASCII.Char[int(what_thing)]

    # Swing the whip
    console.reset_colors()
    for _ in range(45):
        console.gotoxy(x, y)
        console.write(ch, Colors.Code[Colors.Random()])

    # React to the hit, or restore the original, as appropriate
    console.gotoxy(x, y)
    if what_thing in WhatSets.monsters: # Monsters, they get killed
        level.Pf[x][y] = What.Nothing
        console.write(' ')
        level.Score += int(what_thing)
        console.sounds(sounds.Whip_Hit())
    elif what_thing in WhatSets.breakable_obstacles: # Impediments, they might break
        i = level.WhipPower if what_thing != What.Forest else 8
        if what_thing == What.Breakable_Wall:
            char_thing = VisibleTiles.Breakable_Wall
        elif what_thing == What.Forest:
            char_thing = VisibleTiles.Forest
        elif what_thing == What.Tree or what_thing == What.Tree_2:
            char_thing = VisibleTiles.Tree
        if randrange(7) < i: # A whip-power in 7 chance...
            console.write(' ')
            level.Pf[x][y] = What.Nothing
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
        level.Pf[x][y] = What.Nothing
        console.write(' ')
        console.sounds(sounds.Whip_Breakable_Hit())
        if what_thing == What.Generator:
            console.sounds(sounds.Whip_Breakable_Destroy())
            AddScore(What.Generator, level, console)
            level.GenNum -= 1

    # Things that don't break - if any were hidden under Chance symbols, they're revealed
    elif what_thing == What.Whip:
        console.write(VisibleTiles.Whip, Colors.White)
    elif what_thing == What.Chest:
        console.write(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
    elif what_thing == What.SlowTime:
        console.write(VisibleTiles.SlowTime, Colors.LightCyan)
    elif what_thing == What.Gem:
        console.write(VisibleTiles.Gem, Colors.Code[level.GemColor])
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
        level.Pf[x][y] = What.Nothing
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
        if randrange(7) < level.WhipPower:
            console.write(' ')
            level.Pf[x][y] = What.Nothing
            console.sounds(sounds.Whip_Breakable_Destroy())
            AddScore(What.MBlock, level, console)
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if what_thing == What.Breakable_Wall_Grey:
                console.write(VisibleTiles.Breakable_Wall, Colors.LightGrey)
            else:
                console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
    elif what_thing == What.Nothing:
        console.write(' ')
    else:
        console.write(ASCII.Char[int(level.Pf[x][y])].upper(), Colors.White, Colors.Brown)

def Secret_Message():
    pass

def Shoot_Right(x_way: int, y_way: int, Human: bool):
    pass

def Shoot_Left(x_way: int, y_way: int, Human: bool):
    pass

def Tome_Message(level: Level, console: Crt):
    console.alert(YTOP + 1, ' You reach out to grab the object of your long quest... ', Colors.Code[level.Bc], Colors.Code[level.Bb])
    console.alert(YTOP + 1, ' the Magical Staff of Kroz. ', Colors.Code[level.Bc], Colors.Code[level.Bb])
    console.alert(YTOP + 1, ' Your budy surges with electricity as you clutch it! ')

def Tome_Effects(level: Level, console: Crt):
    console.reset_colors()
    for b in range(14, 0, -1):
        for x in range (XBOT, XTOP):
            for y in range(YBOT, YTOP):
                if level.Pf[x][y] == What.Nothing:
                    console.sounds(sounds.Victory_MacGuffin_2(b, x, y))
                    console.gotoxy(x, y)
                    console.write(VisibleTiles.Wall, Colors.Code[(b * 2) % len(Colors.Code)])