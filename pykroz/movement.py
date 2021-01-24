from colors import Colors
from random import randrange

from crt import Crt
from levels import AddScore, Border, Dead, End_Routine, Game, Go, Level, Restore_Border, Update_Info, VisibleTiles, XBOT, XSIZE, XTOP, YBOT, YSIZE, YTOP
from screens import Create_Playfield, Display_Playfield, Display_Playfield, Tome_Effects, Tome_Message
from layouts import Level1, Level11, Level13, Level15, Level17, Level19, Level21, Level23, Level25, Level27, Level29, Level3, Level30, Level5, Level7, Level9
import sounds

def Prayer():
    pass

def Tablet_Message(level: int):
    pass

def Next_Level(game: Game, level: Level):
    if level.Level == 1:
        Level1(level)
    elif level.Level == 3:
        Level3(level)
    elif level.Level == 5:
        Level5(level)
    elif level.Level == 7:
        Level7(level)
    elif level.Level == 9:
        Level9(level)
    elif level.Level == 11:
        Level11(level)
    elif level.Level == 13:
        Level13(level)
    elif level.Level == 15:
        Level15(level)
    elif level.Level == 17:
        Level17(level)
    elif level.Level == 19:
        Level19(level)
    elif level.Level == 21:
        Level21(level)
    elif level.Level == 23:
        Level23(level)
    elif level.Level == 25:
        Level25(level)
    elif level.Level == 27:
        Level27(level)
    elif level.Level == 29:
        Level29(level)
    elif level.Level == 30:
        Level30(level)
    else:
        Create_Playfield(game, level)

def Move(x_way: int, y_way: int, Human: bool, game: Game, level: Level, console: Crt):
    if level.Sideways and y_way == -1 and level.Replacement != 75 and (not level.Pf[level.Px + x_way, level.Py + y_way] in [75, 76, 77, 78, 79, 80]):
        game.OneMove = False
        return
    if level.Px + x_way < XBOT or level.Px + x_way > XTOP or level.Py + y_way < YBOT or level.Py + y_way > YTOP:
        if Human:
            console.sounds(sounds.Static())
            AddScore(20, level, console)
            console.clearkeys()
            if not 0 in game.FoundSet:
                game.FoundSet.append(0)
                console.alert(YTOP + 1, 'An Electrified Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    onto = level.Pf[level.Px + x_way, level.Py + y_way]
    if onto == 0:
        Go(x_way, y_way, Human)
    elif onto in [1, 2, 3]: # Monsters
        level.Gems -= onto
        if level.Gems < 0:
            Dead(True, game, level, console)
        AddScore(onto, level, console)
        console.sounds(sounds.Step_On_Monster(onto))
        Go(x_way, y_way, Human)
        if console.keypressed():
            _ = console.read()
    elif onto in [4, 43, 64]: # Block
        console.sounds(sounds.BlockSound())
        AddScore(4, level, console)
        console.clearkeys()
        if not 4 in game.FoundSet:
            game.FoundSet.append(4)
            console.alert(YTOP + 1, 'A Breakable Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 5: # Whip
        Go(x_way, y_way, Human)
        console.sounds(sounds.GrabSound())
        level.Whips += 1
        AddScore(5)
        if not 5 in game.FoundSet:
            game.FoundSet.append(5)
            console.alert(YTOP + 1, 'You found a Whip.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 6: # Stairs
        Go(x_way, y_way, Human)
        console.clearkeys()
        if level.Level == 30:
            End_Routine(level, console)
        if game.MixUp:
            level.Level = randrange(27) + 2
        else:
            level.Level += 1
        AddScore(6, level, console)
        if not 6 in game.FoundSet:
            game.FoundSet.append(6)
            console.alert(YTOP + 1, 'Stairs take you to the next lower level.', Colors.Code[level.Bc], Colors.Code[level.Bb])
            console.clearkeys()
        console.sounds(sounds.FootStep())
        level.T[1] = 5
        level.T[2] = 6
        level.T[3] = 7
        level.T[4] = 0 # cancel SlowTime
        level.T[5] = 0 # cancel Invisibility
        level.T[6] = 0 # cancel SpeedTime
        level.T[8] = 7
        for n in [0, 8, 15, 17, 19, 20, 21, 22, 26, 28, 36, 66]:
            game.FoundSet.remove(n)
        level.GenNum = 0
        level.TreeRate = -1
        level.LavaFlow = False
        level.Evaporate = 0
        level.MagicEWalls = False
        level.HideLevel = False
        level.HideOpenWall = False
        level.HideRock = False
        level.HideStairs = False
        level.HideGems = False
        level.HideMBlock = False
        level.HideTrap = False
        level.HideCreate = False
        level.GravOn = False
        level.GravRate = 0
        level.GravCounter = 0
        level.Bonus = 0
        level.Sideways = False
        level.Replacement = None
        
        Next_Level(game, level)

        console.sounds(sounds.FootStep)
        for x in range(1, 30):
            console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
            console.clrscr(Colors.Code[level.GemColor])
        for x in range(1, 30):
            console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
            console.clrscr(Colors.Code[level.GemColor])
            console.sound(x * 45, 3)
        console.window(2, 2, 65, 24)
        console.clrscr(Colors.Code[level.GemColor])
        console.window(1, 1, 80, 25)
        Border(level, console)
        console.sounds(sounds.FootStep())
        Display_Playfield(level, console)
        console.sounds(sounds.FootStep())
        for x in range(1, 600):
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
            console.sound(x // 2, 1) # sounds.Enter_Level()
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Player, Colors.Yellow)
        level.I_Score = level.Score
        level.I_Gems = level.Gems
        level.I_Whips = level.Whips
        level.I_Teleports = level.Teleports
        level.I_Keys = level.Keys
        level.I_WhipPower = level.WhipPower
        level.I_Difficulty = game.Difficulty
        level.I_Px = level.Px
        level.I_Py = level.Py
        level.I_FoundSet = game.FoundSet[:]
        if level.Level == 30:
            console.alert(YTOP + 1, 'You have finally reached the last dungeon of Kroz!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 7: # Chest
        Go(x_way, y_way, Human)
        console.sounds(sounds.Open_Chest())
        whips = randrange(3) + 2
        gems = randrange(game.Difficulty) + 2
        level.Whips += whips
        level.Gems += gems
        AddScore(7, level, console)
        console.clearkeys()
        while not console.keypressed():
            console.gotoxy(11, 25)
            console.write('You found {0} gems and {1} whips inside the chest!'.format(gems, whips), Colors.Code[randrange(2) + 14])
        Restore_Border(level, console)
    elif onto == 8: # SlowTime
        Go(x_way, y_way, Human)
        AddScore(5, level, console)
        console.sounds(sounds.Slow())
        level.T[4] = 70 # 100 for FastPC
        level.T[6] = 0
        if 8 not in game.FoundSet:
            game.FoundSet.append(8)
            console.alert(YTOP + 1, 'You activated a Slow Creature spell.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 9: # Gem
        Go(x_way, y_way, Human)
        console.sounds(sounds.GrabSound())
        level.Gems += 1
        AddScore(9, level, console)
        if 9 not in game.FoundSet:
            game.FoundSet.append(9)
            console.alert(YTOP + 1, 'Gems give you both points and strength.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 10: # Invisible
        Go(x_way, y_way, Human)
        AddScore(10, level, console)
        console.sounds(sounds.Invisible())
        console.gotoxy(level.Px, level.Py)
        console.write(' ')
        level.T[5] = 35 # 120 on FastPC
        if 10 not in game.FoundSet:
            game.FoundSet.append(10)
            console.alert(YTOP + 1, 'Oh no, a temporary Blindness Potion!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 11: # Teleport
        Go(x_way, y_way, Human)
        console.sounds(sounds.GrabSound())
        level.Teleports += 1
        AddScore(11, level, console)
        if 11 not in game.FoundSet:
            game.FoundSet.append(11)
            console.alert(YTOP + 1, 'You found a Teleport scroll.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 12: # Key
        Go(x_way, y_way, Human)
        console.sounds(sounds.GrabSound())
        level.Keys += 1
        Update_Info(level, console)
        if 12 not in game.FoundSet:
            game.FoundSet.append(12)
            console.alert(YTOP + 1, 'Use Keys to unlock doors.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 13: # Door
        if Human:
            if level.Keys < 1:
                console.sounds(sounds.Door_No_Keys())
                console.alert(YTOP + 1, 'To pass the Door you need a Key.', Colors.Code[level.Bc], Colors.Code[level.Bb])
            else:
                level.Keys -= 1
                AddScore(11, level, console)
                console.sounds(sounds.Open_Door())
                Go(x_way, y_way, Human)
                console.clearkeys()
                if 13 not in game.FoundSet:
                    game.FoundSet.append(13)
                    console.alert(YTOP + 1, 'The Door opens!  (One of your Keys is used.)', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.clearkeys()
                if level.Level == 75 and level.Px == 33 and level.Py == 14:
                    console.alert(YTOP + 1, 'You unlock the door to the Sacred Temple!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 14 or onto == 17: # Wall, River
        if Human:
            if onto == 14:
                console.sounds(sounds.BlockSound())
            else:
                console.sounds(sounds.River_Splash())
            AddScore(14, level, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.append(onto)
                if onto == 14:
                    console.alert(YTOP + 1, 'A Solid Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.alert(YTOP + 1, 'You cannot travel through water.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 15: # SpeedTime
        Go(x_way, y_way, Human)
        AddScore(15, level, console)
        console.sounds(sounds.Speed())
        level.T[6] = 50 # 80 on FastPC
        level.T[4] = 0
        if 15 not in game.FoundSet:
            game.FoundSet.append(15)
            console.alert(YTOP + 1, 'You activated a Speed Creature spell.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 16: # Trap
        Go(x_way, y_way, Human)
        AddScore(16, level, console)
        for x in range(1, 500):
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        console.gotoxy(level.Px, level.Py)
        console.write(' ')
        console.sounds(sounds.Teleport_Trap())
        level.Pf[level.Px, level.Py] = 0
        level.Px = 0
        while level.Px == 0:
            x = randrange(XSIZE) + XBOT
            y = randrange(YSIZE) + YBOT
            if level.Pf[x, y] == 0:
                level.Px = x
                level.Py = y
                level.Pf[x, y] = 40
        for x in range(1, 500): # 3000 on FastPC
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        if level.T[5] < 1:
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Yellow)
        else:
            console.gotoxy(level.Px, level.Py)
            console.write(' ')
        console.clearkeys()
        if 16 not in game.FoundSet:
            game.FoundSet.append(16)
            console.alert(YTOP + 1, 'You activated a Teleport trap!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 18: # Power
        Go(x_way, y_way, Human)
        level.WhipPower += 1
        for x in range(3, 35):
            for y in range(45, 52):
                console.sounds([(x * y, 7), (None, 15)]) # sounds.Whip_Power()
                console.gotoxy(level.Px, level.Py)
                console.write(VisibleTiles.Player, Colors.Code[Colors.RandomDark()])
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Player, Colors.Yellow)
        AddScore(15, level, console)
        console.alert(YTOP + 1, 'A Power Ring--your whip is now a little stronger!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 19 or onto == 20: # Forest, Tree
        if Human:
            console.sounds(sounds.BlockSound())
            AddScore(4, level, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.append(onto)
                if onto == 19:
                    console.alert(YTOP + 1, 'You cannot travel through forest terrain.', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.alert(YTOP + 1, 'A tree blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 21: # Bomb
        Go(x_way, y_way, Human, game, level, console)
        xr = 0
        xl = 0
        yr = 0
        yl = 0
        console.sounds(sounds.Bomb_Windup())
        for i in range(5000, 20, -1): # 8230 for FastPC
            console.sound(randrange(i), 0.3)
            for width in range(1, 4):
                console.sound(30, 0.3)
                if level.Px - width > 1:
                    xl = width
                if level.Px + width < 66:
                    xr = width
                if level.Py - width > 1:
                    yl = width
                if level.Py + width < 66:
                    yr = width
                for x in range(level.Px - xl, level.Px + xr):
                    for y in range(level.Py - yl, level.Py + yr):
                        # Things that get destroyed by a bomb...
                        if level.Pf[x, y] in [0, 1, 2, 3, 4, 13, 16, 19, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 43, 45, 48, 49, 50, 51, 64, 67, 68, 69, 70, 71, 72, 73, 74, 224, 225, 226, 227, 228, 229, 230, 231]:
                            console.gotoxy(x, y)
                            console.write(219, Colors.LightRed)
            Update_Info(level, console)
            console.clearkeys()
            if 21 not in game.FoundSet:
                game.FoundSet.append(21)
                console.alert(YTOP + 1, 'You activated a Magic Bomb!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 22: # Lava
        Go(x_way, y_way, Human, game, level, console)
        level.Gems -= 10
        console.sounds(sounds.Lava())
        if level.Gems < 0:
            level.Gems = 0
            AddScore(22, level, console)
            Dead(True, game, level, console)
        else:
            AddScore(22, level, console)
        console.clearkeys()
        if 22 not in game.FoundSet:
            game.FoundSet.append(22)
            console.alert(YTOP + 1, 'Oooooooooooooooooooh!  Lava hurts!  (Lose 10 Gems.)', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 23: # Pit
        Go(x_way, y_way, Human, game, level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'Oh no, a Bottomless Pit!', Colors.Code[level.Bc], Colors.Code[level.Bb])
        console.window(2, 2, 65, 24)
        console.clrscr(Colors.Brown)
        console.window(32, 2, 36, 24)
        console.clrscr(Colors.Black)
        console.window(1, 1, 80, 25)
        x = 3000
        for i in range(1, 16):
            if i == 8:
                console.gotoxy(38, 12)
                console.write('<--- HALF WAY!!!', Colors.Yellow, Colors.Brown) # Flashing when possible
            if i == 9:
                console.gotoxy(38, 12)
                console.write('                ', back = Colors.Brown)
            for y in range(2, 24):
                x = x - 8
                console.sound(x, 52 - 3 * i) # sounds.Pit_Falling()
                console.gotoxy(34, y)
                console.write(VisibleTiles.Player, Colors.Yellow)
                console.delay(52 - 3 * i)
                console.gotoxy(34, y)
                console.write(' ')
        console.gotoxy(34, 24)
        console.write('_', Colors.Yellow)
        console.sounds(sounds.Pit_Splat())
        console.clearkeys()
        console.alert(YBOT - 1, '* SPLAT!! *', Colors.Code[level.Bc], Colors.Code[level.Bb])
        Dead(False, game, level, console)
    elif onto == 24: # Tome
        Tome_Message(level, console)
        for _ in range(1, 5):
            Tome_Effects(level, console)
        for x in range(1, 24):
            for y in range(5, 1, -1):
                console.sounds([(x * 45 + y * 10, y * 3), (None, 40)]) # sounds.Victory_MacGuffin()
                console.gotoxy(51, 13)
                console.write(VisibleTiles.Tome, Colors.Code[Colors.Random()])
        console.gotoxy(51, 13)
        console.write(VisibleTiles.Stairs, Colors.Black, Colors.Green) # Flashing when possible
        level.Pf[level.Px + x_way, level.Py + y_way] = 6
        level.Score += 5000
        Update_Info(level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'The Magical Staff of Kroz is finally yours--50,000 points!', Colors.Code[level.Bc], Colors.Code[level.Bb])
        console.alert(YTOP + 1, 'Congratulations, Adventurer, you finally did it!!!', Colors.Code[level.Bc], Colors.Code[level.bb])
    elif onto == 25: # Tunnel
        px_old = level.Px
        py_old = level.Py
        Go(x_way, y_way, Human, game, level, console)
        console.delay(350)
        console.sounds(sounds.FootStep())
        console.delay(500)
        console.sounds(sounds.FootStep())
        level.Pf[level.Px, level.Py] = 25
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Tunnel, Colors.White)
        # After Go() above...
        x = level.Px
        y = level.Py
        # Find a different tunnel
        while level.Pf[x, y] != 25 and px_old + x_way != x or py_old + y_way != y:
            console.sound(randrange(3000) + 100, 0.2) # sounds.Tunnelling()
            x = randrange(XSIZE) + XBOT
            y = randrange(YSIZE) + YBOT
        done = False
        # Find a space adjacent to that tunnel
        for i in range(1, 100):
            console.sound(randrange(3000) + 100, 0.2) # sounds.Tunnelling()
            a = randrange(3) - 1
            b = randrange(3) - 1
            if level.Pf[x + a, y + b] in [0, 32, 33, 37, 39, 55, 56, 57, 67, 224, 225, 226, 227, 228, 229, 230, 231] and not done:
                if not x + a < XBOT or x + a > XTOP or y + b < YBOT or y + b > YTOP:
                    done = True
                    x = x + a
                    y = y + b
        # If we couldn't, Player goes back where they started (not the tunnel they stepped on, the spacd they stepped from)
        if done == False:
            x = px_old
            y = py_old
        level.Px = x
        level.Py = y
        if level.Pf[level.Px, level.Py] in [55, 56, 57]:
            level.Replacement = level.Pf[level.Px, level.Py]
        else:
            level.Replacement = None
        level.Pf[level.Px, level.Py] = 40
        for x in range(1, 400): # 2100 on FastPC
            console.sound(randrange(1000), 0.2) # sounds.TunnelExit()
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        console.gotoxy(level.Px, level.Py)
        if level.T[5] < 1:
            console.write(VisibleTiles.Player, Colors.Yellow)
        else:
            console.write(' ')
        console.clearkeys()
        if 25 not in game.FoundSet:
            game.FoundSet.append(25)
            console.alert(YTOP + 1, 'You passed through a secret Tunnel!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 26: # Freeze
        Go(x_way, y_way, Human, game, level, console)
        AddScore(11, level, console)
        console.sounds(sounds.GrabSound())
        console.sounds(sounds.Freeze())
        level.T[7] = 55 # 60 on FastPC
        if 26 not in game.FoundSet:
            game.FoundSet.append(26)
            console.alert(YTOP + 1, 'You have actiavted a Freeze Creature spell!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 27: # Nugget
        Go(x_way, y_way, Human, game, level, console)
        AddScore(27, level, console)
        console.sounds(sounds.GrabSound())
        if 27 not in game.FoundSet:
            game.FoundSet.append(27)
            console.alert(YTOP + 1, 'You found a Gold Nugget...500 points!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 28: # Quake
        Go(x_way, y_way, Human, game, level, console)
        console.sounds(sounds.Quake_Start())
        for _ in range(1, 50):
            done = False
            while randrange(100) != 0 or not done:
                x = randrange(XSIZE) + XBOT
                y = randrange(YSIZE) + YBOT
                if level.Pf[x, y] in [0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 15, 16, 26, 32, 33, 37, 39, 67, 224, 225, 226, 227, 228, 229, 230, 231]:
                    done = True
                    level.Pf[x, y] = 4
                    console.gotoxy(x, y)
                    console.write(VisibleTiles.Block, Colors.Brown)
            console.sounds(sounds.Quake_Block_Drop())
        console.sounds(sounds.Quake_Finish())
        if 28 not in game.FoundSet:
            game.FoundSet.append(28)
            console.clearkeys()
            console.alert(YTOP + 1, 'Oh no, you set off an Earthquake trap!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 29: # IBlock
        console.gotoxy(level.Px + x_way, level.Py + y_way)
        console.write(VisibleTiles.Block, Colors.Brown)
        level.Pf[level.Px + x_way, level.Py + y_way] = 4
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if 29 not in game.FoundSet:
            game.FoundSet.append(29)
            console.alert(YTOP + 1, 'An Invisible Crumbled Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 30: # IWall
        console.gotoxy(level.Px + x_way, level.Py + y_way)
        console.write(VisibleTiles.Wall, Colors.Brown)
        level.Pf[level.Px + x_way, level.Py + y_way] = 14
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if 30 not in game.FoundSet:
            game.FoundSet.append(30)
            console.alert(YTOP + 1, 'An Invisible Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 31: # IDoor
        console.gotoxy(level.Px + x_way, level.Py+y_way)
        console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
        level.Pf[level.Px + x_way, level.Py + y_way] = 13
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if 31 not in game.FoundSet:
            game.FoundSet.append(31)
            console.alert(YTOP + 1, 'An Invisible Door blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == 32: # Stop
        Go(x_way, y_way, Human, game, level, console)
    elif onto == 33: # Trap2
        Go(x_way, y_way, Human, game, level, console)
        for x in range(XBOT, XTOP):
            for y in range(YBOT, YTOP):
                if level.Pf[x, y] == 33:
                    level.Pf[x, y] = 0
    else:
        if Human:
            console.sounds(sounds.BlockSound())
    game.OneMove = False