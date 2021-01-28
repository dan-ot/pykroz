from playfield import Playfield
from pieces import What, WhatSets
from colors import Colors
from random import choice, randrange

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

def Move(x_way: int, y_way: int, Human: bool, game: Game, playfield: Playfield, level: Level, console: Crt):
    if level.Sideways and y_way == -1 and level.Replacement != What.Rope and (not playfield[level.Px + x_way, level.Py + y_way] in WhatSets.becomes_replacement_with_sideways):
        game.OneMove = False
        return
    if not playfield.bounds().collidepoint(level.Px + x_way, level.Py + y_way):  # level.Px + x_way < XBOT or level.Px + x_way > XTOP or level.Py + y_way < YBOT or level.Py + y_way > YTOP:
        if Human:
            console.sounds(sounds.Static())
            AddScore(What.Tree, level, console)
            console.clearkeys()
            if not What.Nothing in game.FoundSet:
                game.FoundSet.add(What.Nothing)
                console.alert(YTOP + 1, 'An Electrified Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    onto = playfield[level.Px + x_way, level.Py + y_way]
    if onto == What.Nothing:
        Go(x_way, y_way, Human, game, playfield, level, console)
    elif onto in WhatSets.monsters: # Monsters
        AddScore(onto, level, console)
        if onto == What.SlowMonster:
            level.Gems -= 1
            console.sounds(sounds.Step_On_Monster(1))
        elif onto == What.MediumMonster:
            level.Gems -= 2
            console.sounds(sounds.Step_On_Monster(2))
        elif onto == What.FastMonster:
            level.Gems -= 3
            console.sounds(sounds.Step_On_Monster(3))
        if level.Gems < 0:
            Dead(True, game, level, console)
        Go(x_way, y_way, Human, game, playfield, level, console)
        if console.keypressed():
            _ = console.read()
    elif onto in WhatSets.blocks: # Block
        console.sounds(sounds.BlockSound())
        AddScore(What.Breakable_Wall, level, console)
        console.clearkeys()
        if not What.Breakable_Wall in game.FoundSet:
            game.FoundSet.add(What.Breakable_Wall)
            console.alert(YTOP + 1, 'A Breakable Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Whip: # Whip
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.sounds(sounds.GrabSound())
        level.Whips += 1
        AddScore(What.Whip, level, console)
        if not What.Whip in game.FoundSet:
            game.FoundSet.add(What.Whip)
            console.alert(YTOP + 1, 'You found a Whip.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Stairs: # Stairs
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.clearkeys()
        if level.Level == 30:
            End_Routine(level, console)
        if game.MixUp:
            level.Level = randrange(27) + 2
        else:
            level.Level += 1
        AddScore(What.Stairs, level, console)
        if not What.Stairs in game.FoundSet:
            game.FoundSet.add(What.Stairs)
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
        game.FoundSet -= WhatSets.cleared_by_stairs
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
        level.I_FoundSet = game.FoundSet.copy()
        if level.Level == 30:
            console.alert(YTOP + 1, 'You have finally reached the last dungeon of Kroz!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Chest: # Chest
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.sounds(sounds.Open_Chest())
        whips = randrange(3) + 2
        gems = randrange(game.Difficulty) + 2
        level.Whips += whips
        level.Gems += gems
        AddScore(What.Chest, level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'You found {0} gems and {1} whips inside the chest!'.format(gems, whips), Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.SlowTime: # SlowTime
        Go(x_way, y_way, Human, game, playfield, level, console)
        AddScore(What.SlowTime, level, console)
        console.sounds(sounds.Slow())
        level.T[4] = 70 # 100 for FastPC
        level.T[6] = 0
        if What.SlowTime not in game.FoundSet:
            game.FoundSet.add(What.SlowTime)
            console.alert(YTOP + 1, 'You activated a Slow Creature spell.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Gem: # Gem
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.sounds(sounds.GrabSound())
        level.Gems += 1
        AddScore(What.Gem, level, console)
        if What.Gem not in game.FoundSet:
            game.FoundSet.add(What.Gem)
            console.alert(YTOP + 1, 'Gems give you both points and strength.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Invisibility: # Invisible
        Go(x_way, y_way, Human, game, playfield, level, console)
        AddScore(What.Invisibility, level, console)
        console.sounds(sounds.Invisible())
        console.gotoxy(level.Px, level.Py)
        console.write(' ')
        level.T[5] = 35 # 120 on FastPC
        if What.Invisibility not in game.FoundSet:
            game.FoundSet.add(What.Invisibility)
            console.alert(YTOP + 1, 'Oh no, a temporary Blindness Potion!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.TeleportScroll: # Teleport
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.sounds(sounds.GrabSound())
        level.Teleports += 1
        AddScore(What.TeleportScroll, level, console)
        if What.TeleportScroll not in game.FoundSet:
            game.FoundSet.add(What.TeleportScroll)
            console.alert(YTOP + 1, 'You found a Teleport scroll.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Key: # Key
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.sounds(sounds.GrabSound())
        level.Keys += 1
        Update_Info(level, console)
        if What.Key not in game.FoundSet:
            game.FoundSet.add(What.Key)
            console.alert(YTOP + 1, 'Use Keys to unlock doors.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Door: # Door
        if Human:
            if level.Keys < 1:
                console.sounds(sounds.Door_No_Keys())
                console.alert(YTOP + 1, 'To pass the Door you need a Key.', Colors.Code[level.Bc], Colors.Code[level.Bb])
            else:
                level.Keys -= 1
                AddScore(What.TeleportScroll, level, console)
                console.sounds(sounds.Open_Door())
                Go(x_way, y_way, Human, game, playfield, level, console)
                console.clearkeys()
                if What.Door not in game.FoundSet:
                    game.FoundSet.add(What.Door)
                    console.alert(YTOP + 1, 'The Door opens!  (One of your Keys is used.)', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.clearkeys()
                if level.Level == 75 and level.Px == 33 and level.Py == 14:
                    console.alert(YTOP + 1, 'You unlock the door to the Sacred Temple!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Wall or onto == What.River: # Wall, River
        if Human:
            if onto == What.Wall:
                console.sounds(sounds.BlockSound())
            else:
                console.sounds(sounds.River_Splash())
            AddScore(What.Wall, level, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.add(onto)
                if onto == What.Wall:
                    console.alert(YTOP + 1, 'A Solid Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.alert(YTOP + 1, 'You cannot travel through water.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.SpeedTime: # SpeedTime
        Go(x_way, y_way, Human, game, playfield, level, console)
        AddScore(What.SpeedTime, level, console)
        console.sounds(sounds.Speed())
        level.T[6] = 50 # 80 on FastPC
        level.T[4] = 0
        if What.SpeedTime not in game.FoundSet:
            game.FoundSet.add(What.SpeedTime)
            console.alert(YTOP + 1, 'You activated a Speed Creature spell.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.TeleportTrap: # Trap
        Go(x_way, y_way, Human, game, playfield, level, console)
        AddScore(What.TeleportTrap, level, console)
        for x in range(1, 500):
            console.gotoxy(level.Px, level.Py)
            console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        console.gotoxy(level.Px, level.Py)
        console.write(' ')
        console.sounds(sounds.Teleport_Trap())
        playfield[level.Px, level.Py] = What.Nothing
        nothings = playfield.coords_of(What.Nothing)
        (empty_x, empty_y, _) = choice(nothings)
        level.Px = empty_x
        level.Py = empty_y
        playfield[empty_x, empty_y] = What.Player
        # level.Px = 0
        # while level.Px == 0:
        #     x = randrange(XSIZE) + XBOT
        #     y = randrange(YSIZE) + YBOT
        #     if level.Pf[x][y] == What.Nothing:
        #         level.Px = x
        #         level.Py = y
        #         level.Pf[x][y] = What.Player
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
        if What.TeleportTrap not in game.FoundSet:
            game.FoundSet.add(What.TeleportTrap)
            console.alert(YTOP + 1, 'You activated a Teleport trap!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.WhipPower: # Power
        Go(x_way, y_way, Human, game, playfield, level, console)
        level.WhipPower += 1
        for x in range(3, 35):
            for y in range(45, 52):
                console.sounds([(x * y, 7), (None, 15)]) # sounds.Whip_Power()
                console.gotoxy(level.Px, level.Py)
                console.write(VisibleTiles.Player, Colors.Code[Colors.RandomDark()])
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Player, Colors.Yellow)
        AddScore(What.SpeedTime, level, console)
        console.alert(YTOP + 1, 'A Power Ring--your whip is now a little stronger!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Forest or onto == What.Tree: # Forest, Tree
        if Human:
            console.sounds(sounds.BlockSound())
            AddScore(What.Breakable_Wall, level, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.add(onto)
                if onto == What.Forest:
                    console.alert(YTOP + 1, 'You cannot travel through forest terrain.', Colors.Code[level.Bc], Colors.Code[level.Bb])
                else:
                    console.alert(YTOP + 1, 'A tree blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Bomb: # Bomb
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
                        if playfield[x, y] in WhatSets.destroyed_by_bomb:
                            console.gotoxy(x, y)
                            console.write(219, Colors.LightRed)
            Update_Info(level, console)
            console.clearkeys()
            if What.Bomb not in game.FoundSet:
                game.FoundSet.add(What.Bomb)
                console.alert(YTOP + 1, 'You activated a Magic Bomb!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Lava: # Lava
        Go(x_way, y_way, Human, game, playfield, level, console)
        level.Gems -= 10
        console.sounds(sounds.Lava())
        if level.Gems < 0:
            level.Gems = 0
            AddScore(What.Lava, level, console)
            Dead(True, game, level, console)
        else:
            AddScore(What.Lava, level, console)
        console.clearkeys()
        if What.Lava not in game.FoundSet:
            game.FoundSet.add(What.Lava)
            console.alert(YTOP + 1, 'Oooooooooooooooooooh!  Lava hurts!  (Lose 10 Gems.)', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Pit: # Pit
        Go(x_way, y_way, Human, game, playfield, level, console)
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
    elif onto == What.Tome: # Tome
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
        playfield[level.Px + x_way, level.Py + y_way] = What.Stairs
        level.Score += 5000
        Update_Info(level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'The Magical Staff of Kroz is finally yours--50,000 points!', Colors.Code[level.Bc], Colors.Code[level.Bb])
        console.alert(YTOP + 1, 'Congratulations, Adventurer, you finally did it!!!', Colors.Code[level.Bc], Colors.Code[level.bb])
    elif onto == What.Tunnel: # Tunnel
        px_old = level.Px
        py_old = level.Py
        Go(x_way, y_way, Human, game, playfield, level, console)
        console.delay(350)
        console.sounds(sounds.FootStep())
        console.delay(500)
        console.sounds(sounds.FootStep())
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Tunnel, Colors.White)
        # After Go() above...
        x = level.Px
        y = level.Py
        # Find a different tunnel
        tunnels = playfield.coords_of(What.Tunnel)
        playfield[level.Px, level.Py] = What.Tunnel
        (tx, ty, _) = choice(tunnels)
        # while level.Pf[x][y] != What.Tunnel and px_old + x_way != x or py_old + y_way != y:
        #     console.sound(randrange(3000) + 100, 0.2) # sounds.Tunnelling()
        #     x = randrange(XSIZE) + XBOT
        #     y = randrange(YSIZE) + YBOT
        done = False
        # Find a space adjacent to that tunnel
        for i in range(1, 100):
            console.sound(randrange(3000) + 100, 0.2) # sounds.Tunnelling()
            a = randrange(3) - 1
            b = randrange(3) - 1
            if playfield[tx + a][ty + b] in WhatSets.doesnt_block_tunnel_exit and not done:
                if playfield.bounds().collidepoint(tx + a, ty + b):
                    done = True
                    x = tx + a
                    y = ty + b
        # If we couldn't, Player goes back where they started (not the tunnel they stepped on, the space they stepped from)
        if done == False:
            x = px_old
            y = py_old
        level.Px = x
        level.Py = y
        if playfield[level.Px, level.Py] in WhatSets.becomes_replacement_with_tunnelling:
            level.Replacement = playfield[level.Px, level.Py]
        else:
            level.Replacement = What.Nothing
        playfield[level.Px, level.Py] = What.Player
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
        if What.Tunnel not in game.FoundSet:
            game.FoundSet.add(What.Tunnel)
            console.alert(YTOP + 1, 'You passed through a secret Tunnel!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Freeze: # Freeze
        Go(x_way, y_way, Human, game, level, console)
        AddScore(What.TeleportScroll, level, console)
        console.sounds(sounds.GrabSound())
        console.sounds(sounds.Freeze())
        level.T[7] = 55 # 60 on FastPC
        if What.Freeze not in game.FoundSet:
            game.FoundSet.add(What.Freeze)
            console.alert(YTOP + 1, 'You have actiavted a Freeze Creature spell!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Nugget: # Nugget
        Go(x_way, y_way, Human, game, level, console)
        AddScore(What.Nugget, level, console)
        console.sounds(sounds.GrabSound())
        if What.Freeze not in game.FoundSet:
            game.FoundSet.add(What.Freeze)
            console.alert(YTOP + 1, 'You found a Gold Nugget...500 points!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Quake: # Quake
        Go(x_way, y_way, Human, game, level, console)
        console.sounds(sounds.Quake_Start())
        for _ in range(1, 50):
            done = False
            while randrange(100) != 0 or not done:
                x = randrange(playfield.bounds().width)
                y = randrange(playfield.bounds().height)
                if playfield[x, y] in WhatSets.crushed_in_an_earthquake:
                    done = True
                    playfield[x, y] = What.Breakable_Wall
                    console.gotoxy(x, y)
                    console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
            console.sounds(sounds.Quake_Block_Drop())
        console.sounds(sounds.Quake_Finish())
        if What.Quake not in game.FoundSet:
            game.FoundSet.add(What.Quake)
            console.clearkeys()
            console.alert(YTOP + 1, 'Oh no, you set off an Earthquake trap!', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Invisible_Breakable_Wall: # IBlock
        console.gotoxy(level.Px + x_way, level.Py + y_way)
        console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
        playfield[level.Px + x_way, level.Py + y_way] = What.Breakable_Wall
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Breakable_Wall not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Breakable_Wall)
            console.alert(YTOP + 1, 'An Invisible Crumbled Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Invisible_Wall: # IWall
        console.gotoxy(level.Px + x_way, level.Py + y_way)
        console.write(VisibleTiles.Wall, Colors.Brown)
        playfield[level.Px + x_way, level.Py + y_way] = What.Wall
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Wall not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Wall)
            console.alert(YTOP + 1, 'An Invisible Wall blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Invisible_Door: # IDoor
        console.gotoxy(level.Px + x_way, level.Py+y_way)
        console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
        playfield[level.Px + x_way, level.Py + y_way] = What.Door
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Door not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Door)
            console.alert(YTOP + 1, 'An Invisible Door blocks your way.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    elif onto == What.Stop: # Stop
        Go(x_way, y_way, Human, game, level, console)
    elif onto == What.Trap_2: # Trap2
        Go(x_way, y_way, Human, game, level, console)
        for x in range(playfield.bounds().width):
            for y in range(playfield.bounds().height):
                if playfield[x, y] == What.Trap_2:
                    playfield[x, y] = What.Nothing
    else:
        if Human:
            console.sounds(sounds.BlockSound())
    game.OneMove = False