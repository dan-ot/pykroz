from pathlib import Path
import json
from random import choice, randrange
from typing import cast

import pygame.locals

from playerstate import PlayerState
from pieces import What, WhatSets
from commands import Command, command_from_key_code
from engine.colors import Colors
from engine.crt import Crt
from levels import Border, Dead, Game, Level, PMOVE, Restore_Border, SaveType, Sign_Off, TMAX, Update_Info, VisibleTiles, YTOP
from screens import Display_Playfield, Hit, Init_Screen, Screen
from movement import Move, Next_Level
from titles import Title
from playfield import Playfield
import sounds

def Player_Move(game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    # Handle internal messages
    command = command_from_key_code(console.readkey())
    if command is not None:
        console.reset_colors()
        if command == Command.DISCOVERY_CLEAR:
            game.FoundSet = set()
            console.alert(YTOP + 1, 'Newly found object descriptions are reset.', Colors.Code[level.Bc], Colors.Code[level.Bb])
        elif command == Command.DISCOVERY_FULL:
            game.FoundSet = set(What)
            console.alert(YTOP + 1, 'References to new objects will not be displayed.', Colors.Code[level.Bc], Colors.Code[level.Bb])
        elif command == Command.CREATE_STAIRS:
            (px, py) = player.position
            playfield[px + 1, py] = What.Stairs
            console.sounds(sounds.Generate_Stairs())
        elif command == Command.PAUSE:
            console.sounds(sounds.Pause())
            console.clearkeys()
            console.alert(YTOP + 1, ' Press any key to resume game. ', Colors.Code[level.Bc], Colors.Code[level.Bb])
        elif command == Command.QUIT:
            console.sounds(sounds.Quit())
            console.clearkeys()
            console.alert(YTOP + 1, ' Are you sure you want to quit (Y/N)? ', Colors.Code[level.Bc], Colors.Code[level.Bb])
            ch = console.read()
            if ch == pygame.locals.K_y:
                Sign_Off(console)
        elif command == Command.RESTORE:
            console.alert(YTOP + 1, ' Are you sure you want to RESTORE (Y/N)? ', Colors.Code[level.Bc], Colors.Code[level.Bb])
            ch = console.read()
            if ch == pygame.locals.K_n:
                return
            console.clearkeys()
            console.print(8, 25, ' Pick which letter to RESTORE from: A, B or C?  A  ')
            console.gotoxy(56, 25)
            ch = console.read()
            Restore_Border(level, console)
            which_file = ''
            if ch == pygame.locals.K_ESCAPE:
                return
            elif ch == pygame.locals.K_b:
                which_file = 'B'
            elif ch == pygame.locals.K_c:
                which_file = 'C'
            else:
                which_file = 'A'
            console.print(20, 25, '  Restoring from file {0}...  '.format(which_file))
            file = Path('DUNGEON{0}.SAV'.format(which_file))
            if file.exists():
                with open(file, 'r') as f:
                    save_stuff = cast(SaveType, json.load(f))
                    player.level = save_stuff.S_Level
                    player.score = save_stuff.S_Score
                    player.gems = save_stuff.S_Gems
                    player.whips = save_stuff.S_Whips
                    player.teleports = save_stuff.S_Teleports
                    player.keys = save_stuff.S_Keys
                    player.whip_power = save_stuff.S_WhipPower
                    game.Difficulty = save_stuff.S_Difficulty
                    player.position = (save_stuff.S_Px, save_stuff.S_Py)
                    game.FoundSet = save_stuff.S_FoundSet
                    game.MixUp = save_stuff.S_MixUp
                level.I_Score = player.score
                level.I_Gems = player.gems
                level.I_Whips = player.whips
                level.I_Teleports = player.teleports
                level.I_Keys = player.keys
                level.I_WhipPower = player.whip_power
                level.I_Difficulty = game.Difficulty
                level.I_Px = player.position[0]
                level.I_Py = player.position[1]
                level.I_FoundSet = game.FoundSet
                Update_Info(level, console)
                console.delay(1000)
                level.Sideways = False
                level.Evaporate = 0
                level.GenNum = 0
                level.HideLevel = False
                level.HideCreate = False
                level.HideStairs = False
                level.HideTrap = False
                level.HideRock = False
                level.HideGems = False
                level.HideMBlock = False
                level.HideOpenWall = False
                level.Bonus = 0
                level.GravOn = False
                level.GravCounter = 0
                level.TreeRate = -1
                level.T[1] = 4
                level.T[2] = 6
                level.T[3] = 7
                level.T[8] = 7
                level.T[4] = 0
                level.T[5] = 0
                level.T[6] = 0
                playfield.replacement = What.Nothing

                Next_Level(player, playfield, level)

                console.window(2, 2, playfield.bounds().width, playfield.bounds().height)
                console.clrscr()
                console.window(1, 1, 80, 25)
                Border(level, console)
                Display_Playfield(playfield, level, console)
                for x in range (1, 600):
                    console.gotoxy(*player.position)
                    console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
                    console.sound(x // 2, 0.3) # sounds.Load()
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Yellow)
            else:
                Restore_Border(level, console)
                console.sounds(sounds.Load_Error())
                console.alert(YTOP + 1, ' The SAVE file {0} was not found.'.format(which_file), Colors.Code[level.Bc], Colors.Code[level.Bb])

            console.alert(YTOP + 1, 'Press any key to begin this level.', Colors.Code[level.Bc], Colors.Code[level.Bb])

        elif command == Command.SAVE:
            console.alert(YTOP + 1, ' Are you sure you want to SAVE (Y/N)? ', Colors.Code[level.Bc], Colors.Code[level.Bb])
            ch = console.read()
            console.reset_colors()
            console.clearkeys()
            console.print(11, 25, ' Pick which letter to SAVE to: A, B, or C?  A  ')
            console.gotoxy(54, 25)
            ch = console.read()
            which_file = ''
            Restore_Border(level, console)
            if ch == pygame.locals.K_ESCAPE:
                return
            elif ch == pygame.locals.K_b:
                which_file = 'B'
            elif ch == pygame.locals.K_c:
                which_file = 'C'
            else:
                which_file = 'A'
            save_stuff = SaveType(
                player.level,
                level.I_Score,
                level.I_Gems,
                level.I_Whips,
                level.I_Teleports,
                level.I_Keys,
                level.I_WhipPower,
                level.I_Difficulty,
                level.I_Px,
                level.I_Py,
                level.I_FoundSet,
                game.MixUp
            )
            console.print(22, 25, '  Saving to file {0}...  '.format(which_file))
            file = Path('DUNGEON{0}.SAV'.format(which_file))
            file.touch()
            with open(file, 'w') as f:
                json.dump(save_stuff, f)
            console.delay(1000)
            Restore_Border(level, console)

        elif command == Command.TELEPORT:
            if player.teleports < 1:
                console.sounds(sounds.NoneSound())
                return
            player.teleports -= 1
            Update_Info(level, console)
            for x in range(1, 250):
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
            console.gotoxy(*player.position)
            if playfield.replacement == What.Rope:
                console.write(VisibleTiles.Rope, Colors.LightGrey)
            else:
                console.write(' ')
            i = 0
            console.sound(20, 3) # sound.Teleport_Windup()
            while i <= 700:
                i += 1
                x = randrange(playfield.bounds().width)
                y = randrange(playfield.bounds().height)
                if playfield[x, y] in WhatSets.teleport_animate_through:
                    console.gotoxy(x, y)
                    console.write(1, Colors.Yellow)
                    # We need to render both the symbol above and the empty symbol for 1 frame each
                    # Which causes the player to flicker through many spaces on the playfield
                    console.delay(3)
                    console.gotoxy(x, y)
                    console.write(' ')
            # end Teleport_Windup()
            console.sounds(sounds.Teleport())
            playfield[player.position] = playfield.replacement
            empties = playfield.coords_of(What.Nothing)
            (x, y, _) = choice(empties)
            player.position = (x, y)
            playfield[player.position] = What.Player
            playfield.replacement = What.Nothing
            console.clearkeys()
            for x in range(1, 500): # 3000 on FastPC
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
            if level.T[5] < 1:
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Yellow)
            else:
                console.gotoxy(*player.position)
                console.write(' ')

        elif command == Command.WHIP:
            if player.whips < 1:
                console.sounds(sounds.NoneSound())
                return
            player.whips -= 1
            (px, py) = player.position
            bounds = playfield.bounds()
            # Check for collision with the border - don't try to hit out of bounds
            if px > bounds.left and py > bounds.top:
                console.sounds(sounds.Whip(10))
                Hit(px - 1, py - 1, '\\', playfield, player, level, console)
            if px > bounds.left:
                console.sounds(sounds.Whip(10))
                Hit(px - 1, py, '─', playfield, player, level, console)
            if py < bounds.bottom and px > bounds.left:
                console.sounds(sounds.Whip(10))
                Hit(px - 1, py + 1, '/', playfield, player, level, console)
            if py < bounds.bottom:
                console.sounds(sounds.Whip(10))
                Hit(px, py + 1, '│', playfield, player, level, console)
            if py < bounds.bottom and px < bounds.right:
                console.sounds(sounds.Whip(10))
                Hit(px + 1, py + 1, '\\', playfield, player, level, console)
            if px < bounds.right:
                console.sounds(sounds.Whip(10))
                Hit(px + 1, py, '─', playfield, player, level, console)
            if py > bounds.top and px < bounds.right:
                console.sounds(sounds.Whip(10))
                Hit(px + 1, py - 1, '/', playfield, player, level, console)
            if py > bounds.top:
                console.sounds(sounds.Whip(10))
                Hit(px, py - 1, '│', playfield, player, level, console)
            Update_Info(level, console)
            console.clearkeys()

        elif command == Command.MOVE_NORTH:
            Move(0, -1, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_SOUTH:
            Move(0, 1, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_EAST:
            Move(1, 0, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_WEST:
            Move(-1, 0, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_NORTHWEST:
            Move(-1, -1, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_NORTHEAST:
            Move(1, -1, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_SOUTHWEST:
            Move(-1, 1, PMOVE, game, playfield, player, level, console)
        elif command == Command.MOVE_SOUTHEAST:
            Move(1, 1, PMOVE, game, playfield, player, level, console)
    else: # command is None
        console.sounds(sounds.Bad_Key())

def Move_Slow(game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    if level.T[6] > 0: # FastTime is on
        level.T[1] = 0 # 3 on FastPC
    else:
        if level.T[4] < 1: # SlowTime is off
            level.T[1] = level.STime
        else:
            level.T[1] = level.STime * 5
    if level.SNum < 1: # Number of monsters that started on the level. Not updated as monsters are removed...
        return
    for loop in range(1, level.SNum):
        if level.Sx[loop] == 0:
            if randrange(8) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        if not playfield[level.Sx[loop], level.Sy[loop]] == What.SlowMonster: # There's no slow monster where there's supposed to be one?
            level.Sx[loop] = 0 # Set the current monster's X to 0?
            if randrange(8) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        playfield[level.Sx[loop], level.Sy[loop]] = What.Nothing # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Sx[loop], level.Sy[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        if px < level.Sx[loop]:
            level.Sx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > level.Sx[loop]:
            level.Sx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if py < level.Sy[loop]:
                level.Sy[loop] -= 1
                y_dir = 1
            elif py > level.Sy[loop]:
                level.Sy[loop] += 1
                y_dir = -1
        console.gotoxy(level.Sx[loop], level.Sy[loop]) # After the move!
        occupant = playfield[level.Sx[loop], level.Sy[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[level.Sx[loop], level.Sy[loop]] = What.SlowMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            level.Sx[loop] += x_dir
            level.Sy[loop] += y_dir
            playfield[level.Sx[loop], level.Sy[loop]] = What.SlowMonster # Put the monster back
            console.gotoxy(level.Sx[loop], level.Sy[loop])
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[level.Sx[loop], level.Sy[loop]] = What.Nothing
            level.Sx[loop] = 0
            console.write(' ')
            player.score += 1
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sounds(sounds.Monster1_On_Player())
            level.Sx[loop] = 0
            player.gems -= 1
            if player.gems < 0:
                Dead(True, game, player, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(player.gems)) // 2, 8)
            if player.gems > 9:
                console.write('{0}'.format(player.gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(player.gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in WhatSets.monster_eats:
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
            playfield[level.Sx[loop], level.Sy[loop]] = What.SlowMonster
            console.sounds(sounds.GrabSound())
        else:
            level.Sx[loop] += x_dir
            level.Sy[loop] += y_dir
            playfield[level.Sx[loop], level.Sy[loop]] = What.SlowMonster
            console.gotoxy(level.Sx[loop], level.Sy[loop])
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
        if randrange(8) == 1:
            Player_Move(game, playfield, player, level, console) # player gets a chance to move after each monster?

def Move_Medium(game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    if level.T[6] > 0: # FastTime is on
        level.T[2] = 0 # 3 on FastPC
    else:
        if level.T[4] < 1: # SlowTime is off
            level.T[1] = level.MTime
        else:
            level.T[1] = level.MTime * 5
    if level.MNum < 1: # Number of monsters that started on the level. Not updated as monsters are removed...
        return
    for loop in range(1, level.MNum):
        if level.Mx[loop] == 0:
            if randrange(7) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        if not playfield[level.Mx[loop], level.My[loop]] == What.MediumMonster: # There's no slow monster where there's supposed to be one?
            level.Mx[loop] = 0 # Set the current monster's X to 0?
            if randrange(7) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        playfield[level.Mx[loop], level.My[loop]] = What.Nothing # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Mx[loop], level.My[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        if px < level.Mx[loop]:
            level.Mx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > level.Mx[loop]:
            level.Mx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if py < level.My[loop]:
                level.My[loop] -= 1
                y_dir = 1
            elif py > level.My[loop]:
                level.My[loop] += 1
                y_dir = -1
        console.gotoxy(level.Mx[loop], level.My[loop]) # After the move!
        occupant = playfield[level.Mx[loop], level.My[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[level.Mx[loop], level.My[loop]] = What.MediumMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            level.Mx[loop] += x_dir
            level.My[loop] += y_dir
            playfield[level.Mx[loop], level.My[loop]] = What.MediumMonster # Put the monster back
            console.gotoxy(level.Mx[loop], level.My[loop])
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[level.Mx[loop], level.My[loop]] = What.Nothing
            level.Mx[loop] = 0
            console.write(' ')
            player.score += 2
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sound(sounds.Monster2_On_Player())
            level.Mx[loop] = 0
            player.gems -= 2
            if player.gems < 0:
                Dead(True, game, player, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(player.gems)) // 2, 8)
            if player.gems > 9:
                console.write('{0}'.format(player.gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(player.gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in WhatSets.monster_eats:
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
            playfield[level.Mx[loop], level.My[loop]] = What.MediumMonster
            console.sounds(sounds.GrabSound())
        else:
            level.Mx[loop] += x_dir
            level.My[loop] += y_dir
            playfield[level.Mx[loop], level.My[loop]] = What.MediumMonster
            console.gotoxy(level.Mx[loop], level.My[loop])
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        if randrange(7) == 1:
            Player_Move(game, playfield, player, level, console) # player gets a chance to move after each monster?

def Move_Fast(game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    if level.T[6] > 0: # FastTime is on
        level.T[1] = 0 # 3 on FastPC
    else:
        if level.T[4] < 1: # SlowTime is off
            level.T[3] = level.FTime
        else:
            level.T[3] = level.FTime * 5
    if level.FNum < 1: # Number of monsters that started on the level. Not updated as monsters are removed...
        return
    for loop in range(1, level.FNum):
        if level.Fx[loop] == 0:
            if randrange(6) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        if not playfield[level.Fx[loop], level.Fy[loop]] == What.FastMonster: # There's no slow monster where there's supposed to be one?
            level.Fx[loop] = 0 # Set the current monster's X to 0?
            if randrange(6) == 1:
                Player_Move(game, playfield, player, level, console)
                return
        playfield[level.Fx[loop], level.Fy[loop]] = What.Nothing # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Fx[loop], level.Fy[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        if px < level.Fx[loop]:
            level.Fx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > level.Fx[loop]:
            level.Fx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if py < level.Fy[loop]:
                level.Fy[loop] -= 1
                y_dir = 1
            elif py > level.Fy[loop]:
                level.Fy[loop] += 1
                y_dir = -1
        console.gotoxy(level.Fx[loop], level.Fy[loop]) # After the move!
        occupant = playfield[level.Fx[loop], level.Fy[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[level.Fx[loop], level.Fy[loop]] = What.FastMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            level.Fx[loop] += x_dir
            level.Fy[loop] += y_dir
            playfield[level.Fx[loop], level.Fy[loop]] = What.FastMonster # Put the monster back
            console.gotoxy(level.Fx[loop], level.Fy[loop])
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[level.Fx[loop], level.Fy[loop]] = What.Nothing
            level.Fx[loop] = 0
            console.write(' ')
            player.score += 3
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sounds(sounds.Monster3_On_Player())
            level.Fx[loop] = 0
            player.gems -= 3
            if player.gems < 0:
                Dead(True, game, player, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(player.gems)) // 2, 8)
            if player.gems > 9:
                console.write('{0}'.format(player.gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(player.gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in WhatSets.monster_eats:
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
            playfield[level.Fx[loop], level.Fy[loop]] = What.FastMonster
            console.sounds(sounds.GrabSound())
        else:
            level.Fx[loop] += x_dir
            level.Fy[loop] += y_dir
            playfield[level.Fx[loop], level.Fy[loop]] = What.FastMonster
            console.gotoxy(level.Fx[loop], level.Fy[loop])
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        if randrange(6) == 1:
            Player_Move(game, playfield, player, level, console) # player gets a chance to move after each monster?

def Move_MBlock():
    pass

def Run(console: Crt):
    game = Game()
    level = Level()
    playfield = Playfield(64, 23)
    player = PlayerState()
    Screen(game, console)
    NewGame(game, playfield, player, level, console)

def NewGame(game: Game, playfield: Playfield, player: PlayerState, level: Level, console: Crt):
    console.reset_colors()
    Title(game, level, console)
    Border(level, console)
    Init_Screen(game, player, playfield, level, console)
    Update_Info(player, console)
    player.level = 1
    Next_Level(player, playfield, level)
    Display_Playfield(playfield, level, console)
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
    for x in range(1, 800):
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        console.sound(x // 2) # sounds.NewGame()
    console.gotoxy(*player.position)
    console.write(VisibleTiles.Player, Colors.Yellow)
    console.clearkeys()
    console.alert(YTOP + 1, 'Press any key to begin this level.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    while not game.Restart:
        Player_Move(game, playfield, player, level, console)
        if console.keypressed():
            level.SkipTime = 801
        else:
            level.SkipTime += 1
        if level.SkipTime > 800:
            for x in range(1, TMAX):
                level.T[x] -= 1
            level.SkipTime = 0 # -150 for FastPC
            if level.T[7] < 1: # Freeze is not active
                if level.T[1] < 1:
                    Move_Slow(game, playfield, player, level, console)
                if level.T[2] < 1:
                    Move_Medium(game, playfield, player, level, console)
                if level.T[3] < 1:
                    Move_Fast(game, playfield, player, level, console)
    NewGame(game, playfield, player, level, console)
