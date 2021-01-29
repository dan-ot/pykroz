from random import choice, randrange

from engine.colors import Colors
from engine.crt import Crt
from playerstate import PlayerState
from playfield import Playfield
from pieces import What, WhatSets
from levels import AddScore, Border, LiteralLevel, Load_Literal_Level, Load_Random_Level, Dead, End_Routine, Game, Go, Level, RandomLevel, Update_Info, VisibleTiles, YBOT, YTOP
from screens import Display_Playfield, Tome_Effects, Tome_Message
from layouts import DungeonsLayouts
import sounds

def Prayer():
    pass

def Tablet_Message(level: int):
    pass

def Next_Level(player: PlayerState, playfield: Playfield, level: Level):
    definition = DungeonsLayouts[player.level]

    if isinstance(definition, LiteralLevel):
        Load_Literal_Level(definition, player, level, playfield)
    elif isinstance(definition, RandomLevel):
        Load_Random_Level(definition, player, playfield, level)

def Move(x_way: int, y_way: int, Human: bool, game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    future_player_position = player.future_pos(x_way, y_way)
    if level.Sideways and y_way == -1 and playfield.replacement != What.Rope and (not playfield[future_player_position] in WhatSets.becomes_replacement_with_sideways):
        game.OneMove = False
        return
    if not playfield.bounds().collidepoint(future_player_position):
        if Human:
            console.sounds(sounds.Static())
            AddScore(What.Tree, level, console)
            console.clearkeys()
            if not What.Nothing in game.FoundSet:
                game.FoundSet.add(What.Nothing)
                console.alert(YTOP + 1, 'An Electrified Wall blocks your way.', level.Bc, level.Bb)
    onto = playfield[future_player_position]
    if onto == What.Nothing:
        Go(x_way, y_way, Human, game, playfield, player, level, console)
    elif onto in WhatSets.monsters: # Monsters
        AddScore(onto, player, console)
        if onto == What.SlowMonster:
            player.gems -= 1
            console.sounds(sounds.Step_On_Monster(1))
        elif onto == What.MediumMonster:
            player.gems -= 2
            console.sounds(sounds.Step_On_Monster(2))
        elif onto == What.FastMonster:
            player.gems -= 3
            console.sounds(sounds.Step_On_Monster(3))
        if player.gems < 0:
            Dead(True, game, player, level, console)
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        if console.keypressed():
            _ = console.read()
    elif onto in WhatSets.blocks: # Block
        console.sounds(sounds.BlockSound())
        AddScore(What.Breakable_Wall, player, console)
        console.clearkeys()
        if not What.Breakable_Wall in game.FoundSet:
            game.FoundSet.add(What.Breakable_Wall)
            console.alert(YTOP + 1, 'A Breakable Wall blocks your way.', level.Bc, level.Bb)
    elif onto == What.Whip: # Whip
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.sounds(sounds.GrabSound())
        player.whips += 1
        AddScore(What.Whip, player, console)
        if not What.Whip in game.FoundSet:
            game.FoundSet.add(What.Whip)
            console.alert(YTOP + 1, 'You found a Whip.', level.Bc, level.Bb)
    elif onto == What.Stairs: # Stairs
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.clearkeys()
        if player.level == 30:
            End_Routine(game, player, level, console)
        if game.MixUp:
            player.level = randrange(27) + 2
        else:
            player.level += 1
        AddScore(What.Stairs, player, console)
        if not What.Stairs in game.FoundSet:
            game.FoundSet.add(What.Stairs)
            console.alert(YTOP + 1, 'Stairs take you to the next lower level.', level.Bc, level.Bb)
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
        playfield.replacement = What.Nothing

        Next_Level(player, playfield, level)

        console.sounds(sounds.FootStep)
        for x in range(1, 30):
            console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
            console.clrscr(level.GemColor)
        for x in range(1, 30):
            console.window(32 - x, 12 - x // 3, 35 + x, 14 + x // 3)
            console.clrscr(level.GemColor)
            console.sound(x * 45, 3)
        console.window(2, 2, 65, 24)
        console.clrscr(level.GemColor)
        console.window(1, 1, 80, 25)
        Border(level, console)
        console.sounds(sounds.FootStep())
        Display_Playfield(playfield, level, console)
        console.sounds(sounds.FootStep())
        for x in range(1, 600):
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
            console.sound(x // 2, 1) # sounds.Enter_Level()
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Yellow)
        level.I_Score = player.score
        level.I_Gems = player.gems
        level.I_Whips = player.whips
        level.I_Teleports = player.teleports
        level.I_Keys = player.keys
        level.I_WhipPower = player.whip_power
        level.I_Difficulty = game.Difficulty
        level.I_Px = player.position[0]
        level.I_Py = player.position[1]
        level.I_FoundSet = game.FoundSet.copy()
        if player.level == 30:
            console.alert(YTOP + 1, 'You have finally reached the last dungeon of Kroz!', level.Bc, level.Bb)
    elif onto == What.Chest: # Chest
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.sounds(sounds.Open_Chest())
        whips = randrange(3) + 2
        gems = randrange(game.Difficulty) + 2
        player.whips += whips
        player.gems += gems
        AddScore(What.Chest, player, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'You found {0} gems and {1} whips inside the chest!'.format(gems, whips), level.Bc, level.Bb)
    elif onto == What.SlowTime: # SlowTime
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.SlowTime, player, console)
        console.sounds(sounds.Slow())
        level.T[4] = 70 # 100 for FastPC
        level.T[6] = 0
        if What.SlowTime not in game.FoundSet:
            game.FoundSet.add(What.SlowTime)
            console.alert(YTOP + 1, 'You activated a Slow Creature spell.', level.Bc, level.Bb)
    elif onto == What.Gem: # Gem
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.sounds(sounds.GrabSound())
        player.gems += 1
        AddScore(What.Gem, player, console)
        if What.Gem not in game.FoundSet:
            game.FoundSet.add(What.Gem)
            console.alert(YTOP + 1, 'Gems give you both points and strength.', level.Bc, level.Bb)
    elif onto == What.Invisibility: # Invisible
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.Invisibility, player, console)
        console.sounds(sounds.Invisible())
        console.gotoxy(*player.position)
        console.write(' ')
        level.T[5] = 35 # 120 on FastPC
        if What.Invisibility not in game.FoundSet:
            game.FoundSet.add(What.Invisibility)
            console.alert(YTOP + 1, 'Oh no, a temporary Blindness Potion!', level.Bc, level.Bb)
    elif onto == What.TeleportScroll: # Teleport
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.sounds(sounds.GrabSound())
        player.teleports += 1
        AddScore(What.TeleportScroll, player, console)
        if What.TeleportScroll not in game.FoundSet:
            game.FoundSet.add(What.TeleportScroll)
            console.alert(YTOP + 1, 'You found a Teleport scroll.', level.Bc, level.Bb)
    elif onto == What.Key: # Key
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.sounds(sounds.GrabSound())
        player.keys += 1
        Update_Info(player, console)
        if What.Key not in game.FoundSet:
            game.FoundSet.add(What.Key)
            console.alert(YTOP + 1, 'Use Keys to unlock doors.', level.Bc, level.Bb)
    elif onto == What.Door: # Door
        if Human:
            if player.keys < 1:
                console.sounds(sounds.Door_No_Keys())
                console.alert(YTOP + 1, 'To pass the Door you need a Key.', level.Bc, level.Bb)
            else:
                player.keys -= 1
                AddScore(What.TeleportScroll, player, console)
                console.sounds(sounds.Open_Door())
                Go(x_way, y_way, Human, game, playfield, player, level, console)
                console.clearkeys()
                if What.Door not in game.FoundSet:
                    game.FoundSet.add(What.Door)
                    console.alert(YTOP + 1, 'The Door opens!  (One of your Keys is used.)', level.Bc, level.Bb)
                else:
                    console.clearkeys()
                if player.level == 75 and player.position == (33, 14):
                    console.alert(YTOP + 1, 'You unlock the door to the Sacred Temple!', level.Bc, level.Bb)
    elif onto == What.Wall or onto == What.River: # Wall, River
        if Human:
            if onto == What.Wall:
                console.sounds(sounds.BlockSound())
            else:
                console.sounds(sounds.River_Splash())
            AddScore(What.Wall, player, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.add(onto)
                if onto == What.Wall:
                    console.alert(YTOP + 1, 'A Solid Wall blocks your way.', level.Bc, level.Bb)
                else:
                    console.alert(YTOP + 1, 'You cannot travel through water.', level.Bc, level.Bb)
    elif onto == What.SpeedTime: # SpeedTime
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.SpeedTime, player, console)
        console.sounds(sounds.Speed())
        level.T[6] = 50 # 80 on FastPC
        level.T[4] = 0
        if What.SpeedTime not in game.FoundSet:
            game.FoundSet.add(What.SpeedTime)
            console.alert(YTOP + 1, 'You activated a Speed Creature spell.', level.Bc, level.Bb)
    elif onto == What.TeleportTrap: # Trap
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.TeleportTrap, player, console)
        for x in range(1, 500):
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
        console.gotoxy(*player.position)
        console.write(' ')
        console.sounds(sounds.Teleport_Trap())
        playfield[player.position] = What.Nothing
        nothings = playfield.coords_of(What.Nothing)
        (empty_x, empty_y, _) = choice(nothings)
        player.position = (empty_x, empty_y)
        playfield[empty_x, empty_y] = What.Player
        for x in range(1, 500): # 3000 on FastPC
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
        if level.T[5] < 1:
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Yellow)
        else:
            console.gotoxy(*player.position)
            console.write(' ')
        console.clearkeys()
        if What.TeleportTrap not in game.FoundSet:
            game.FoundSet.add(What.TeleportTrap)
            console.alert(YTOP + 1, 'You activated a Teleport trap!', level.Bc, level.Bb)
    elif onto == What.WhipPower: # Power
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        player.whip_power += 1
        for x in range(3, 35):
            for y in range(45, 52):
                console.sounds([(x * y, 7), (None, 15)]) # sounds.Whip_Power()
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.RandomDark())
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Yellow)
        AddScore(What.SpeedTime, level, console)
        console.alert(YTOP + 1, 'A Power Ring--your whip is now a little stronger!', level.Bc, level.Bb)
    elif onto == What.Forest or onto == What.Tree: # Forest, Tree
        if Human:
            console.sounds(sounds.BlockSound())
            AddScore(What.Breakable_Wall, level, console)
            console.clearkeys()
            if onto not in game.FoundSet:
                game.FoundSet.add(onto)
                if onto == What.Forest:
                    console.alert(YTOP + 1, 'You cannot travel through forest terrain.', level.Bc, level.Bb)
                else:
                    console.alert(YTOP + 1, 'A tree blocks your way.', level.Bc, level.Bb)
    elif onto == What.Bomb: # Bomb
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        xr = 0
        xl = 0
        yr = 0
        yl = 0
        console.sounds(sounds.Bomb_Windup())
        for i in range(5000, 20, -1): # 8230 for FastPC
            console.sound(randrange(i), 0.3)
            for width in range(1, 4):
                console.sound(30, 0.3)
                (px, py) = player.position
                if px - width > 1:
                    xl = width
                if px + width < 66:
                    xr = width
                if py - width > 1:
                    yl = width
                if py + width < 66:
                    yr = width
                for x in range(px - xl, px + xr):
                    for y in range(py - yl, py + yr):
                        # Things that get destroyed by a bomb...
                        if playfield[x, y] in WhatSets.destroyed_by_bomb:
                            console.gotoxy(x, y)
                            console.write(219, Colors.LightRed)
            Update_Info(player, console)
            console.clearkeys()
            if What.Bomb not in game.FoundSet:
                game.FoundSet.add(What.Bomb)
                console.alert(YTOP + 1, 'You activated a Magic Bomb!', level.Bc, level.Bb)
    elif onto == What.Lava: # Lava
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        player.gems -= 10
        console.sounds(sounds.Lava())
        if player.gems < 0:
            player.gems = 0
            AddScore(What.Lava, player, console)
            Dead(True, game, player, level, console)
        else:
            AddScore(What.Lava, player, console)
        console.clearkeys()
        if What.Lava not in game.FoundSet:
            game.FoundSet.add(What.Lava)
            console.alert(YTOP + 1, 'Oooooooooooooooooooh!  Lava hurts!  (Lose 10 Gems.)', level.Bc, level.Bb)
    elif onto == What.Pit: # Pit
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'Oh no, a Bottomless Pit!', level.Bc, level.Bb)
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
        console.alert(YBOT - 1, '* SPLAT!! *', level.Bc, level.Bb)
        Dead(False, game, player, level, console)
    elif onto == What.Tome: # Tome
        Tome_Message(level, console)
        for _ in range(1, 5):
            Tome_Effects(level, console)
        for x in range(1, 24):
            for y in range(5, 1, -1):
                console.sounds([(x * 45 + y * 10, y * 3), (None, 40)]) # sounds.Victory_MacGuffin()
                console.gotoxy(51, 13)
                console.write(VisibleTiles.Tome, Colors.Random())
        console.gotoxy(51, 13)
        console.write(VisibleTiles.Stairs, Colors.Black, Colors.Green) # Flashing when possible
        playfield[future_player_position] = What.Stairs
        player.score += 5000
        Update_Info(level, console)
        console.clearkeys()
        console.alert(YTOP + 1, 'The Magical Staff of Kroz is finally yours--50,000 points!', level.Bc, level.Bb)
        console.alert(YTOP + 1, 'Congratulations, Adventurer, you finally did it!!!', level.Bc, level.Bb)
    elif onto == What.Tunnel: # Tunnel
        (px_old, py_old) = player.position if player.position is not None else (0, 0)
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        console.delay(350)
        console.sounds(sounds.FootStep())
        console.delay(500)
        console.sounds(sounds.FootStep())
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Tunnel, Colors.White)
        # After Go() above...
        (x, y) = player.position
        # Find a different tunnel
        tunnels = playfield.coords_of(What.Tunnel)
        # Fewer tunnels, longer sound
        console.sounds(sounds.Tunnelling(10000.0 / len(tunnels)))
        playfield[player.position] = What.Tunnel
        (tx, ty, _) = choice(tunnels)
        done = False
        # Find a space adjacent to that tunnel
        for i in range(1, 100):
            console.sound(randrange(3000) + 100, 0.2) # sounds.Tunnelling()
            a = randrange(3) - 1
            b = randrange(3) - 1
            if playfield[tx + a, ty + b] in WhatSets.doesnt_block_tunnel_exit and not done:
                if playfield.bounds().collidepoint(tx + a, ty + b):
                    done = True
                    x = tx + a
                    y = ty + b
        # If we couldn't, Player goes back where they started (not the tunnel they stepped on, the space they stepped from)
        if not done:
            x = px_old
            y = py_old
        player.position = (x, y)
        if playfield[player.position] in WhatSets.becomes_replacement_with_tunnelling:
            playfield.replacement = playfield[player.position]
        else:
            playfield.replacement = What.Nothing
        playfield[player.position] = What.Player
        for x in range(1, 400): # 2100 on FastPC
            console.sound(randrange(1000), 0.2) # sounds.TunnelExit()
            console.gotoxy(*player.position)
            console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
        console.gotoxy(*player.position)
        if level.T[5] < 1:
            console.write(VisibleTiles.Player, Colors.Yellow)
        else:
            console.write(' ')
        console.clearkeys()
        if What.Tunnel not in game.FoundSet:
            game.FoundSet.add(What.Tunnel)
            console.alert(YTOP + 1, 'You passed through a secret Tunnel!', level.Bc, level.Bb)
    elif onto == What.Freeze: # Freeze
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.TeleportScroll, player, console)
        console.sounds(sounds.GrabSound())
        console.sounds(sounds.Freeze())
        level.T[7] = 55 # 60 on FastPC
        if What.Freeze not in game.FoundSet:
            game.FoundSet.add(What.Freeze)
            console.alert(YTOP + 1, 'You have actiavted a Freeze Creature spell!', level.Bc, level.Bb)
    elif onto == What.Nugget: # Nugget
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        AddScore(What.Nugget, player, console)
        console.sounds(sounds.GrabSound())
        if What.Freeze not in game.FoundSet:
            game.FoundSet.add(What.Freeze)
            console.alert(YTOP + 1, 'You found a Gold Nugget...500 points!', level.Bc, level.Bb)
    elif onto == What.Quake: # Quake
        Go(x_way, y_way, Human, game, playfield, player, level, console)
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
            console.alert(YTOP + 1, 'Oh no, you set off an Earthquake trap!', level.Bc, level.Bb)
    elif onto == What.Invisible_Breakable_Wall: # IBlock
        console.gotoxy(*future_player_position)
        console.write(VisibleTiles.Breakable_Wall, Colors.Brown)
        playfield[future_player_position] = What.Breakable_Wall
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Breakable_Wall not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Breakable_Wall)
            console.alert(YTOP + 1, 'An Invisible Crumbled Wall blocks your way.', level.Bc, level.Bb)
    elif onto == What.Invisible_Wall: # IWall
        console.gotoxy(*future_player_position)
        console.write(VisibleTiles.Wall, Colors.Brown)
        playfield[future_player_position] = What.Wall
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Wall not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Wall)
            console.alert(YTOP + 1, 'An Invisible Wall blocks your way.', level.Bc, level.Bb)
    elif onto == What.Invisible_Door: # IDoor
        console.gotoxy(*future_player_position)
        console.write(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
        playfield[future_player_position] = What.Door
        console.sounds(sounds.BlockSound())
        console.clearkeys()
        if What.Invisible_Door not in game.FoundSet:
            game.FoundSet.add(What.Invisible_Door)
            console.alert(YTOP + 1, 'An Invisible Door blocks your way.', level.Bc, level.Bb)
    elif onto == What.Stop: # Stop
        Go(x_way, y_way, Human, game, playfield, player, level, console)
    elif onto == What.Trap_2: # Trap2
        Go(x_way, y_way, Human, game, playfield, player, level, console)
        for x in range(playfield.bounds().width):
            for y in range(playfield.bounds().height):
                if playfield[x, y] == What.Trap_2:
                    playfield[x, y] = What.Nothing
    else:
        if Human:
            console.sounds(sounds.BlockSound())
    game.OneMove = False
