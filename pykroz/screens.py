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
            level.Pf[x, y] = 0
    level.Pf[level.Px, level.Py] = 40
    Parse_Field(game, level)
    for obj in range(TOTOBJECTS):
        if level.Parsed[obj] > 0:
            for _ in range(level.Parsed[obj]):
                done = False
                while not done:
                    x_spot = randrange(XSIZE) + XBOT
                    y_spot = randrange(YSIZE) + YBOT
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
    console.reset_colors()
    for x_loop in range(XBOT, XTOP):
        for y_loop in range(YBOT, YTOP):
            if (level.Pf[x_loop, y_loop] > 0 or level.FloorPattern) and (not level.HideLevel):
                console.gotoxy(x_loop, y_loop)
                if level.Pf[x_loop, y_loop] == 0: # Floor
                    console.write(VisibleTiles.Tile, Colors.Code[level.Cf1], Colors.Code[level.Bf1])
                elif level.Pf[x_loop, y_loop] == 1: # Slow Monster
                    console.write(VisibleTiles.SMonster_1, Colors.LightRed)
                elif level.Pf[x_loop, y_loop] == 2: # Medium Monster
                    console.write(VisibleTiles.MMonster_1, Colors.LightGreen)
                elif level.Pf[x_loop, y_loop] == 3: # Fast Monster
                    console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
                elif level.Pf[x_loop, y_loop] == 4: # Block
                    if level.Level != 71:
                        console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
                elif level.Pf[x_loop, y_loop] == 5: # Whip
                    console.write(VisibleTiles.Whip, Colors.White)
                elif level.Pf[x_loop, y_loop] == 6: # Stairs
                    if not level.HideStairs:
                        console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing, when possible
                elif level.Pf[x_loop, y_loop] == 7: # Chest
                    if randrange(20) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
                elif level.Pf[x_loop, y_loop] == 8: # Slow Time
                    if randrange(35) == 0:
                        console.write(VisibleTiles.Chance, Colors.Yellow)
                    else:
                        console.write(VisibleTiles.SlowTime, Colors.LightCyan)
                elif level.Pf[x_loop, y_loop] == 9: # Gem
                    if not level.HideGems:
                        console.write(VisibleTiles.Gem, Colors.Code[level.GemColor])
                elif level.Pf[x_loop, y_loop] == 10: # Invisible
                    console.write(VisibleTiles.Invisible, Colors.Blue)
                elif level.Pf[x_loop, y_loop] == 11: # Teleport
                    console.write(VisibleTiles.Teleport, Colors.LightMagenta)
                elif level.Pf[x_loop, y_loop] == 12: # Key
                    if randrange(25) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Key, Colors.LightRed)
                elif level.Pf[x_loop, y_loop] == 13: # Door
                    console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
                elif level.Pf[x_loop, y_loop] == 14: # Wall
                    console.write(VisibleTiles.Wall, Colors.Brown)
                elif level.Pf[x_loop, y_loop] == 15: # SpeedTime
                    if randrange(10) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.SpeedTime, Colors.LightCyan)
                elif level.Pf[x_loop, y_loop] == 16: # Trap
                    if not level.HideTrap:
                        console.write(VisibleTiles.Trap, Colors.LightGrey)
                elif level.Pf[x_loop, y_loop] == 17: # River
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Lava, Colors.White, Colors.Red)
                    else:
                        console.write(VisibleTiles.River, Colors.LightBlue, Colors.Blue)
                elif level.Pf[x_loop, y_loop] == 18: # Power
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Power, Colors.White)
                elif level.Pf[x_loop, y_loop] == 19: # Forest
                    console.write(VisibleTiles.Forest, Colors.Green)
                elif level.Pf[x_loop, y_loop] == 20 or level.Pf[x_loop, y_loop] == 252: # Tree
                    console.write(VisibleTiles.Tree, Colors.Brown, Colors.Green)
                elif level.Pf[x_loop, y_loop] == 21: # Bomb
                    if randrange(40) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                    else:
                        console.write(VisibleTiles.Bomb, Colors.White)
                elif level.Pf[x_loop, y_loop] == 22: # Lava
                    console.write(VisibleTiles.Lava, Colors.LightRed, Colors.Red)
                elif level.Pf[x_loop, y_loop] == 23: # Pit
                    console.write(VisibleTiles.Pit, Colors.LightGrey)
                elif level.Pf[x_loop, y_loop] == 24: # Tome
                    console.write(VisibleTiles.Tome, Colors.White, Colors.Magenta) # Flashing when possible
                elif level.Pf[x_loop, y_loop] == 25: # Tunnel
                    console.write(VisibleTiles.Tunnel, Colors.White)
                elif level.Pf[x_loop, y_loop] == 26: # Freeze
                    console.write(VisibleTiles.Freeze, Colors.LightGreen)
                elif level.Pf[x_loop, y_loop] == 27: # Nugget
                    console.write(VisibleTiles.Nugget, Colors.Yellow)
                elif level.Pf[x_loop, y_loop] == 28: # Quake
                    if randrange(15) == 0:
                        console.write(VisibleTiles.Chance, Colors.White)
                # 29: IBlock
                # 30: IWall
                # 31: IDoor
                # 32: Stop
                # 33: Trap2
                elif level.Pf[x_loop, y_loop] == 34: # Zap
                    console.write(VisibleTiles.Zap, Colors.LightRed)
                elif level.Pf[x_loop, y_loop] == 35: # Create
                    if not level.HideCreate:
                        console.write(VisibleTiles.Chance, Colors.White)
                elif level.Pf[x_loop, y_loop] == 36: # Generator
                    console.write(VisibleTiles.Generator, Colors.Yellow) # Flashing when possible
                # 37: Trap3
                elif level.Pf[x_loop, y_loop] == 38: # MBlock
                    if not level.HideMBlock:
                        console.write(VisibleTiles.MBlock, Colors.Brown)
                # 39: Trap4
                elif level.Pf[x_loop, y_loop] == 40: # Player
                    console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing when possible
                # 41: ShowGems
                # 42:
                elif level.Pf[x_loop, y_loop] == 43: # ZBlock
                    console.write(VisibleTiles.ZBlock, Colors.Brown)
                # 44: BlockSpell
                elif level.Pf[x_loop, y_loop] == 45: # Chance
                    console.write(VisibleTiles.Chance, Colors.White)
                elif level.Pf[x_loop, y_loop] == 46: # Statue
                    console.write(VisibleTiles.Statue, Colors.White) # Flashing, when possible
                # 67: Trap5
                elif level.Pf[x_loop, y_loop] == 222: # ??
                    console.write('!', Colors.White, Colors.Brown)
                # 224...231: Traps
                elif level.Pf[x_loop, y_loop] in [29, 30, 31, 32, 33, 37, 39, 41, 42, 44, 67, 224, 225, 226, 227, 228, 229, 230, 231]:
                    # Explained in comments above
                    pass
                else:
                    console.write(ASCII.Char[level.Pf[x_loop, y_loop]].upper(), Colors.White, Colors.Brown)
    level.FloorPattern = False

def Hit(x: int, y: int, ch: str, level: Level, console: Crt):
    # Remember what we're overwriting
    int_thing = level.Pf[x, y]
    char_thing = ASCII.Char[int_thing]

    # Swing the whip
    console.reset_colors()
    for _ in range(45):
        console.gotoxy(x, y)
        console.write(ch, Colors.Code[Colors.Random()])

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
            char_thing = VisibleTiles.Breakable_Wall
        elif int_thing == 19:
            char_thing = VisibleTiles.Forest
        elif int_thing == 20 or int_thing == 252:
            char_thing = VisibleTiles.Tree
        if randrange(7) < i: # A whip-power in 7 chance...
            console.write(' ')
            level.Pf[x, y] = 0
            console.sounds(sounds.Whip_Breakable_Destroy())
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if char_thing == VisibleTiles.Tree:
                console.write(char_thing, Colors.Brown, Colors.Green)
            elif char_thing == VisibleTiles.Forest:
                console.write(char_thing, Colors.Green)
    elif int_thing == 6: # Stairs
        console.write(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey) # Flashing when possible
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
        console.write(VisibleTiles.Whip, Colors.White)
    elif int_thing == 7:
        console.write(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
    elif int_thing == 8:
        console.write(VisibleTiles.SlowTime, Colors.LightCyan)
    elif int_thing == 9:
        console.write(VisibleTiles.Gem, Colors.Code[level.GemColor])
    elif int_thing == 11:
        console.write(VisibleTiles.Teleport, Colors.LightMagenta)
    elif int_thing == 12:
        console.write(VisibleTiles.Key, Colors.LightRed)
    elif int_thing == 13:
        console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
    elif int_thing in [14, 52, 53]: # Invisible walls become visible?
        console.write(VisibleTiles.Wall, Colors.Brown)
    elif int_thing == 54:
        console.write(VisibleTiles.Wall, Colors.LightGrey)
    elif int_thing == 17:
        console.write(VisibleTiles.River, Colors.LightBlue, Colors.Blue)
    elif int_thing == 21:
        console.write(VisibleTiles.Bomb, Colors.White)
    elif int_thing == 22:
        console.write(VisibleTiles.Lava, Colors.LightRed, Colors.Red)
    elif int_thing == 23:
        console.write(VisibleTiles.Wall, Colors.LightGrey)
    elif int_thing == 24:
        console.write(VisibleTiles.Tome, Colors.White, Colors.Magenta) # Flashing when possible
    elif int_thing == 25:
        console.write(VisibleTiles.Tunnel, Colors.White)
    elif int_thing == 26:
        console.write(VisibleTiles.Freeze, Colors.LightCyan)
    elif int_thing == 27:
        console.write(VisibleTiles.Nugget, Colors.Yellow)
    elif int_thing in [28, 29, 30, 31, 33, 37, 39, 41, 44, 67, 224, 225, 226, 227, 228, 229, 230, 231]:
        # Invisible things that stay invisible?
        console.write(' ', Colors.Black, Colors.Black)
    elif int_thing == 32:
        level.Pf[x, y] = 0
        console.write(' ')
    elif int_thing == 34:
        console.write(VisibleTiles.Zap, Colors.LightRed)
    elif int_thing == 35:
        console.write(VisibleTiles.Create, Colors.Yellow)
    elif int_thing == 45:
        console.write(VisibleTiles.Chance, Colors.White)
    elif int_thing in [58, 59, 60]:
        console.write(VisibleTiles.OSpell1, Colors.LightCyan)
    elif int_thing == 66:
        console.write(VisibleTiles.EWall, Colors.LightRed, Colors.Red)
    elif int_thing in [47, 55, 56, 57, 61, 62, 63, 68, 69, 70, 71, 72, 73, 74]:
        console.write(' ')
    elif int_thing in [76, 77, 78, 79, 80]:
        console.write(VisibleTiles.DropRope, Colors.LightGrey)
    elif int_thing == 75:
        console.write(VisibleTiles.Rope, Colors.LightGrey)
    elif int_thing == 81:
        console.write(VisibleTiles.Amulet, Colors.White) # Flashing when possible
    elif int_thing == 82:
        console.write(VisibleTiles.ShootRight, Colors.LightGrey)
    elif int_thing == 83:
        console.write(VisibleTiles.ShootLeft, Colors.LightGrey)
    elif int_thing in [38, 43, 64]: # Breakable Walls?
        if randrange(7) < level.WhipPower:
            console.write(' ')
            level.Pf[x, y] = 0
            console.sounds(sounds.Whip_Breakable_Destroy())
            AddScore(38)
        else:
            console.sounds(sounds.Whip_Breakable_Hit())
            if int_thing == 64:
                console.write(VisibleTiles.Breakable_Wall, Colors.LightGrey)
            else:
                console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
    elif int_thing == 0:
        console.write(' ')
    else:
        console.write(ASCII.Char[level.Pf[x, y]].upper(), Colors.White, Colors.Brown)

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
                if level.Pf[x, y] == 0:
                    console.sounds(sounds.Victory_MacGuffin_2(b, x, y))
                    console.gotoxy(x, y)
                    console.write(VisibleTiles.Wall, Colors.Code[(b * 2) % len(Colors.Code)])