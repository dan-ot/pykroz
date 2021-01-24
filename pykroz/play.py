from commands import Command, command_from_key_code
from colors import Colors
from pathlib import Path
import json
from random import randrange
from typing import cast

import pygame.locals

from crt import Crt
from levels import Border, Dead, Define_Levels, Game, Level, PMOVE, Restore_Border, SaveType, Sign_Off, TMAX, Update_Info, VisibleTiles, XBOT, XSIZE, XTOP, YBOT, YSIZE, YTOP
from screens import Display_Playfield, Hit, Init_Screen, Screen
from movement import Move, Next_Level
from titles import Title
from layouts import Level1
import sounds

def Player_Move(game: Game, level: Level, console: Crt):
    # Handle internal messages
    command = command_from_key_code(console.readkey())
    if command is not None:
        console.reset_colors()
        if command == Command.DISCOVERY_CLEAR:
            game.FoundSet = []
            console.alert(YTOP + 1, 'Newly found object descriptions are reset.', Colors.Code[level.Bc], Colors.Code[level.Bb])
        elif command == Command.DISCOVERY_FULL:
            game.FoundSet = [x for x in range(255)]
            console.alert(YTOP + 1, 'References to new objects will not be displayed.', Colors.Code[level.Bc], Colors.Code[level.Bb])
        elif command == Command.CREATE_STAIRS:
            level.Pf[level.Px + 1, level.Py] = 6
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
                    level.Level = save_stuff.S_Level
                    level.Score = save_stuff.S_Score
                    level.Gems = save_stuff.S_Gems
                    level.Whips = save_stuff.S_Whips
                    level.Teleports = save_stuff.S_Teleports
                    level.Keys = save_stuff.S_Keys
                    level.WhipPower = save_stuff.S_WhipPower
                    game.Difficulty = save_stuff.S_Difficulty
                    level.Px = save_stuff.S_Px
                    level.Py = save_stuff.S_Py
                    game.FoundSet = save_stuff.S_FoundSet
                    game.MixUp = save_stuff.S_MixUp
                level.I_Score = level.Score
                level.I_Gems = level.Gems
                level.I_Whips = level.Whips
                level.I_Teleports = level.Teleports
                level.I_Keys = level.Keys
                level.I_WhipPower = level.WhipPower
                level.I_Difficulty = game.Difficulty
                level.I_Px = level.Px
                level.I_Py = level.Py
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
                level.Replacement = None

                Next_Level(game, level)

                console.window(2, 2, XSIZE + 1, YSIZE + 1)
                console.clrscr()
                console.window(1, 1, 80, 25)
                Border(level, console)
                Display_Playfield(level, console)
                for x in range (1, 600):
                    console.gotoxy(level.Px, level.Py)
                    console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
                    console.sound(x // 2, 0.3) # sounds.Load()
                console.gotoxy(level.Px, level.Py)
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
                level.Level,
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
            if level.Teleports < 1:
                console.sounds(sounds.NoneSound())
                return
            level.Teleports -= 1
            Update_Info(level, console)
            for x in range(1, 250):
                console.gotoxy(level.Px, level.Py)
                console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
            console.gotoxy(level.Px, level.Py)
            if level.Replacement == 75:
                console.write(VisibleTiles.Rope, Colors.LightGrey)
            else:
                console.write(' ')
            i = 0
            console.sound(20, 3) # sound.Teleport_Windup()
            while i <= 700:
                i += 1
                x = randrange(XSIZE) + XBOT
                y = randrange(YSIZE) + YBOT
                if level.Pf[x, y] in [0, 32, 33, 37, 39, 41, 44, 47, 55, 56, 57, 61, 62, 63, 67, 68, 69, 70, 71, 72, 73, 74, 224, 225, 226, 227, 228, 229, 230, 231]:
                    console.gotoxy(x, y)
                    console.write(1, Colors.Yellow)
                    console.delay(3)
                    console.gotoxy(x, y)
                    console.write(' ')
            # end Teleport_Windup()
            console.sounds(sounds.Teleport())
            level.Pf[level.Px, level.Py] = level.Replacement
            level.Px = 0
            while level.Px == 0:
                x = randrange(XSIZE) + XBOT
                y = randrange(YSIZE) + YBOT
                if level.Pf[x, y] == 0:
                    level.Px = 0
                    level.Py = 0
                    level.Pf[level.Px, level.Py] = 40
            level.Replacement = None
            console.clearkeys()
            for x in range(1, 500): # 3000 on FastPC
                console.gotoxy(level.Px, level.Py)
                console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
            if level.T[5] < 1:
                console.gotoxy(level.Px, level.Py)
                console.write(VisibleTiles.Player, Colors.Yellow)
            else:
                console.gotoxy(level.Px, level.Py)
                console.write(' ')
        
        elif command == Command.WHIP:
            if level.Whips < 1:
                console.sounds(sounds.NoneSound())
                return
            level.Whips -= 1
            console.sound(70, 0.3) # sounds.Whip()
            if level.Py > YBOT and level.Px > XBOT:
                Hit(level.Px - 1, level.Py - 1, '\\', level, console)
            if level.Px > XBOT:
                Hit(level.Px - 1, level.Py, '─', level, console)
            if level.Py < YTOP and level.Px > XBOT:
                Hit(level.Px - 1, level.Py + 1, '/')
            if level.Py < YTOP:
                Hit(level.Px, level.Py + 1, '│', level, console)
            if level.Py < YTOP and level.Px < XTOP:
                Hit(level.Px + 1, level.Py + 1, '\\')
            if level.Px < XTOP:
                Hit(level.Px + 1, level.Py, '─', level, console)
            if level.Py > YBOT and level.Px < XTOP:
                Hit(level.Px + 1, level.Py - 1, '/')
            if level.Py > YBOT:
                Hit(level.Px, level.Py - 1, '│', level, console)
            Update_Info(level, console)
            console.clearkeys()

        elif command == Command.MOVE_NORTH:
            Move(0, -1, PMOVE, game, level, console)
        elif command == Command.MOVE_SOUTH:
            Move(0, 1, PMOVE, game, level, console)
        elif command == Command.MOVE_EAST:
            Move(1, 0, PMOVE, game, level, console)
        elif command == Command.MOVE_WEST:
            Move(-1, 0, PMOVE, game, level, console)
        elif command == Command.MOVE_NORTHWEST:
            Move(-1, -1, PMOVE, game, level, console)
        elif command == Command.MOVE_NORTHEAST:
            Move(1, -1, PMOVE, game, level, console)
        elif command == Command.MOVE_SOUTHWEST:
            Move(-1, 1, PMOVE, game, level, console)
        elif command == Command.MOVE_SOUTHEAST:
            Move(1, 1, PMOVE, game, level, console)
    else: # command is None
        console.sounds(sounds.Bad_Key())

def Move_Slow(game: Game, level: Level, console: Crt):
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
                Player_Move(game, level, console)
                return
        if not level.Pf[level.Sx[loop], level.Sy[loop]] == 1: # There's no slow monster where there's supposed to be one?
            level.Sx[loop] = 0 # Set the current monster's X to 0?
            if randrange(8) == 1:
                Player_Move(game, level, console)
                return
        level.Pf[level.Sx[loop], level.Sy[loop]] = 0 # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Sx[loop], level.Sy[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        if level.Px < level.Sx[loop]:
            level.Sx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif level.Px > level.Sx[loop]:
            level.Sx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if level.Py < level.Sy[loop]:
                level.Sy[loop] -= 1
                y_dir = 1
            elif level.Py > level.Sy[loop]:
                level.Sy[loop] += 1
                y_dir = -1
        console.gotoxy(level.Sx[loop], level.Sy[loop]) # After the move!
        occupant = level.Pf[level.Sx[loop], level.Sy[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in [0, 68, 69, 70, 71, 72, 73, 74]:
            slow = 142 if randrange(2) == 0 else 65
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            level.Pf[level.Sx[loop], level.Sy[loop]] = 1 # Confirm the move
        # Things a monster can't move through
        elif occupant in [1, 2, 3, 6, 13, 14, 17, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 44, 45, 46, 47, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 75, 76, 77, 78, 79, 80, 224, 225, 226, 227, 228, 229, 230, 231]:
            level.Sx[loop] += x_dir
            level.Sy[loop] += y_dir
            level.Pf[level.Sx[loop], level.Sy[loop]] = 1 # Put the monster back
            console.gotoxy(level.Sx[loop], level.Sy[loop])
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
        # Things with mutual destruction
        elif occupant in [4, 38, 43, 64]:
            level.Pf[level.Sx[loop], level.Sy[loop]] = 0
            level.Sx[loop] = 0
            console.write(' ')
            level.Score += 1
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == 40: # The player!
            console.sounds(sounds.Monster1_On_Player())
            level.Sx[loop] = 0
            level.Gems -= 1
            if level.Gems < 0:
                Dead(True, game, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(level.Gems)) // 2, 8)
            if level.Gems > 9:
                console.write('{0}'.format(level.Gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(level.Gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in [5, 7, 8, 9, 10, 11, 12, 15, 16, 18, 26, 27, 48, 49, 50, 51, 82, 83]:
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
            level.Pf[level.Sx[loop], level.Sy[loop]] = 1
            console.sounds(sounds.GrabSound())
        else:
            level.Sx[loop] += x_dir
            level.Sy[loop] += y_dir
            level.Pf[level.Sx[loop], level.Sy[loop]] = 1
            console.gotoxy(level.Sx[loop], level.Sy[loop])
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
        if randrange(8) == 1:
            Player_Move(game, level, console) # player gets a chance to move after each monster?

def Move_Medium(game: Game, level: Level, console: Crt):
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
                Player_Move(game, level, console)
                return
        if not level.Pf[level.Mx[loop], level.My[loop]] == 1: # There's no slow monster where there's supposed to be one?
            level.Mx[loop] = 0 # Set the current monster's X to 0?
            if randrange(7) == 1:
                Player_Move(game, level, console)
                return
        level.Pf[level.Mx[loop], level.My[loop]] = 0 # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Mx[loop], level.My[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        if level.Px < level.Mx[loop]:
            level.Mx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif level.Px > level.Mx[loop]:
            level.Mx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if level.Py < level.My[loop]:
                level.My[loop] -= 1
                y_dir = 1
            elif level.Py > level.My[loop]:
                level.My[loop] += 1
                y_dir = -1
        console.gotoxy(level.Mx[loop], level.My[loop]) # After the move!
        occupant = level.Pf[level.Mx[loop], level.My[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in [0, 68, 69, 70, 71, 72, 73, 74]:
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            level.Pf[level.Mx[loop], level.My[loop]] = 1 # Confirm the move
        # Things a monster can't move through
        elif occupant in [1, 2, 3, 6, 13, 14, 17, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 44, 45, 46, 47, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 75, 76, 77, 78, 79, 80, 224, 225, 226, 227, 228, 229, 230, 231]:
            level.Mx[loop] += x_dir
            level.My[loop] += y_dir
            level.Pf[level.Mx[loop], level.My[loop]] = 1 # Put the monster back
            console.gotoxy(level.Mx[loop], level.My[loop])
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        # Things with mutual destruction
        elif occupant in [4, 38, 43, 64]:
            level.Pf[level.Mx[loop], level.My[loop]] = 0
            level.Mx[loop] = 0
            console.write(' ')
            level.Score += 2
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == 40: # The player!
            console.sound(sounds.Monster2_On_Player())
            level.Mx[loop] = 0
            level.Gems -= 2
            if level.Gems < 0:
                Dead(True, game, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(level.Gems)) // 2, 8)
            if level.Gems > 9:
                console.write('{0}'.format(level.Gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(level.Gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in [5, 7, 8, 9, 10, 11, 12, 15, 16, 18, 26, 27, 48, 49, 50, 51, 82, 83]:
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
            level.Pf[level.Mx[loop], level.My[loop]] = 1
            console.sounds(sounds.GrabSound())
        else:
            level.Mx[loop] += x_dir
            level.My[loop] += y_dir
            level.Pf[level.Mx[loop], level.My[loop]] = 1
            console.gotoxy(level.Mx[loop], level.My[loop])
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        if randrange(7) == 1:
            Player_Move(game, level, console) # player gets a chance to move after each monster?

def Move_Fast(game: Game, level: Level, console: Crt):
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
                Player_Move(game, level, console)
                return
        if not level.Pf[level.Fx[loop], level.Fy[loop]] == 1: # There's no slow monster where there's supposed to be one?
            level.Fx[loop] = 0 # Set the current monster's X to 0?
            if randrange(6) == 1:
                Player_Move(game, level, console)
                return
        level.Pf[level.Fx[loop], level.Fy[loop]] = 0 # remove the monster before we know whether it's move is valid...
        console.gotoxy(level.Fx[loop], level.Fy[loop])
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        if level.Px < level.Fx[loop]:
            level.Fx[loop] -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif level.Px > level.Fx[loop]:
            level.Fx[loop] += 1
            x_dir = -1
        if not level.Sideways:
            if level.Py < level.Fy[loop]:
                level.Fy[loop] -= 1
                y_dir = 1
            elif level.Py > level.Fy[loop]:
                level.Fy[loop] += 1
                y_dir = -1
        console.gotoxy(level.Fx[loop], level.Fy[loop]) # After the move!
        occupant = level.Pf[level.Fx[loop], level.Fy[loop]] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in [0, 68, 69, 70, 71, 72, 73, 74]:
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            level.Pf[level.Fx[loop], level.Fy[loop]] = 1 # Confirm the move
        # Things a monster can't move through
        elif occupant in [1, 2, 3, 6, 13, 14, 17, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 44, 45, 46, 47, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 75, 76, 77, 78, 79, 80, 224, 225, 226, 227, 228, 229, 230, 231]:
            level.Fx[loop] += x_dir
            level.Fy[loop] += y_dir
            level.Pf[level.Fx[loop], level.Fy[loop]] = 1 # Put the monster back
            console.gotoxy(level.Fx[loop], level.Fy[loop])
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        # Things with mutual destruction
        elif occupant in [4, 38, 43, 64]:
            level.Pf[level.Fx[loop], level.Fy[loop]] = 0
            level.Fx[loop] = 0
            console.write(' ')
            level.Score += 3
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == 40: # The player!
            console.sounds(sounds.Monster3_On_Player())
            level.Fx[loop] = 0
            level.Gems -= 3
            if level.Gems < 0:
                Dead(True, game, level, console)

            # Update Gems display?
            console.gotoxy(71, 8)
            console.write('      ')
            console.gotoxy(73 - len(str(level.Gems)) // 2, 8)
            if level.Gems > 9:
                console.write('{0}'.format(level.Gems), Colors.Red, Colors.LightGrey)
            else:
                console.write('{0}'.format(level.Gems), Colors.LightRed, Colors.DarkGrey) # Flashing when possible
        # Things a monster eats
        elif occupant in [5, 7, 8, 9, 10, 11, 12, 15, 16, 18, 26, 27, 48, 49, 50, 51, 82, 83]:
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
            level.Pf[level.Fx[loop], level.Fy[loop]] = 1
            console.sounds(sounds.GrabSound())
        else:
            level.Fx[loop] += x_dir
            level.Fy[loop] += y_dir
            level.Pf[level.Fx[loop], level.Fy[loop]] = 1
            console.gotoxy(level.Fx[loop], level.Fy[loop])
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        if randrange(6) == 1:
            Player_Move(game, level, console) # player gets a chance to move after each monster?

def Move_MBlock():
    pass

def Run(console: Crt):
    game = Game()
    level = Level()
    Screen(game, console)
    NewGame(game, level, console)
    
def NewGame(game: Game, level: Level, console: Crt):
    console.reset_colors()
    Title(game, level, console)
    Border(level, console)
    Init_Screen(game, level, console)
    Update_Info(level, console)
    Define_Levels(game)
    Level1(level)
    Display_Playfield(level, console)
    level.I_Score = level.Score
    level.I_Gems = level.Gems
    level.I_Whips = level.Whips
    level.I_Teleports = level.Teleports
    level.I_Keys = level.Keys
    level.I_WhipPower = level.WhipPower
    level.I_Difficulty = game.Difficulty
    level.I_Px = level.Px
    level.I_Py = level.Py
    level.I_FoundSet = game.FoundSet
    for x in range(1, 800):
        console.gotoxy(level.Px, level.Py)
        console.write(VisibleTiles.Player, Colors.Code[Colors.Random()], Colors.Code[Colors.RandomDark()])
        console.sound(x // 2) # sounds.NewGame()
    console.gotoxy(level.Px, level.Py)
    console.write(VisibleTiles.Player, Colors.Yellow)
    console.clearkeys()
    console.alert(YTOP + 1, 'Press any key to begin this level.', Colors.Code[level.Bc], Colors.Code[level.Bb])
    while not game.Restart:
        Player_Move(game, level, console)
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
                    Move_Slow(game, level, console)
                if level.T[2] < 1:
                    Move_Medium(game, level, console)
                if level.T[3] < 1:
                    Move_Fast(game, level, console)
    NewGame(game, level, console)