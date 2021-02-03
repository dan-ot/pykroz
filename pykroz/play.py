from pathlib import Path
import json
from random import choice, randrange
from typing import cast

import pygame.constants

from display.game_display import GameDisplay
from playerstate import PlayerState
from pieces import What, WhatSets
from commands import Command, command_from_key_code
from engine.colors import Colors
from engine.crt import Crt
from levels import Dead, Game, Level, PMOVE, SaveType, Sign_Off, TMAX, VisibilityFlags, VisibleTiles, YTOP
from screens import Hit, Init_Screen, Screen
from movement import Move, Next_Level
from titles import Title
from playfield import Playfield
import sounds

def Player_Move(game: Game, playfield: Playfield, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    # Handle internal messages
    EXTRA_TIME = 8.0
    command = command_from_key_code(console.readkey())
    if command is not None:
        console.reset_colors()
        if command == Command.DISCOVERY_CLEAR:
            game.FoundSet = set()
            console.alert(YTOP + 1, 'Newly found object descriptions are reset.', level.Bc, level.Bb)
        elif command == Command.DISCOVERY_FULL:
            game.FoundSet = set(What)
            console.alert(YTOP + 1, 'References to new objects will not be displayed.', level.Bc, level.Bb)
        elif command == Command.CREATE_STAIRS:
            (px, py) = player.position
            playfield[px + 1, py] = What.Stairs
            console.sounds(sounds.Generate_Stairs())
        elif command == Command.PAUSE:
            console.sounds(sounds.Pause())
            console.clearkeys()
            console.alert(YTOP + 1, ' Press any key to resume game. ', level.Bc, level.Bb)
        elif command == Command.QUIT:
            console.sounds(sounds.Quit())
            console.clearkeys()
            console.alert(YTOP + 1, ' Are you sure you want to quit (Y/N)? ', level.Bc, level.Bb)
            ch = console.read()
            if ch == pygame.constants.K_y:
                Sign_Off(console)
        elif command == Command.RESTORE:
            console.alert(YTOP + 1, ' Are you sure you want to RESTORE (Y/N)? ', level.Bc, level.Bb)
            ch = console.read()
            if ch == pygame.constants.K_n:
                return
            console.clearkeys()
            # TODO: Writing in the border here...
            console.print(8, 25, ' Pick which letter to RESTORE from: A, B or C?  A  ')
            console.gotoxy(56, 25)
            ch = console.read()
            which_file = ''
            if ch == pygame.constants.K_ESCAPE:
                return
            elif ch == pygame.constants.K_b:
                which_file = 'B'
            elif ch == pygame.constants.K_c:
                which_file = 'C'
            else:
                which_file = 'A'
            console.print(20, 25, '  Restoring from file {0}...  '.format(which_file))
            file = Path('DUNGEON{0}.SAV'.format(which_file))
            if file.exists():
                with open(file, 'r') as f:
                    save_stuff = cast(SaveType, json.load(f))
                    player.level = save_stuff.level
                    player.score = save_stuff.score
                    player.gems = save_stuff.gems
                    player.whips = save_stuff.whips
                    player.teleports = save_stuff.teleports
                    player.keys = save_stuff.keys
                    player.whip_power = save_stuff.whip_power
                    game.Difficulty = save_stuff.difficulty
                    player.position = (save_stuff.px, save_stuff.py)
                    game.FoundSet = set(map(lambda t: What(t), save_stuff.found_set))
                    game.MixUp = save_stuff.mix_up
                level.initial.score = player.score
                level.initial.gems = player.gems
                level.initial.whips = player.whips
                level.initial.teleports = player.teleports
                level.initial.keys = player.keys
                level.initial.whip_power = player.whip_power
                level.initial.difficulty = game.Difficulty
                level.initial.px = player.position[0]
                level.initial.py = player.position[1]
                level.initial.found_set = list(game.FoundSet)
                display.mark_player_dirty()
                console.delay(1000)
                level.Sideways = False
                level.Evaporate = 0
                level.GenNum = 0
                level.visibility = VisibilityFlags.SHOW_ALL
                level.Bonus = 0
                level.GravOn = False
                level.GravCounter = 0
                level.TreeRate = -1
                level.slow_monster_timer = EXTRA_TIME - level.slow_monster_timer_base
                level.medium_monster_timer = EXTRA_TIME - level.medium_monster_timer_base
                level.fast_monster_timer = EXTRA_TIME - level.fast_monster_timer_base
                level.T[8] = 7
                level.T[4] = 0
                level.T[5] = 0
                level.T[6] = 0
                playfield.replacement = What.Nothing

                Next_Level(player, playfield, level)

                console.window(2, 2, playfield.bounds().width, playfield.bounds().height)
                console.clrscr()
                console.window(1, 1, 80, 25)
                display.new_level(playfield)
                for x in range (1, 600):
                    console.gotoxy(*player.position)
                    console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
                    console.sound(x // 2, 0.3) # sounds.Load()
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Yellow)
            else:
                console.sounds(sounds.Load_Error())
                console.alert(YTOP + 1, ' The SAVE file {0} was not found.'.format(which_file), level.Bc, level.Bb)

            console.alert(YTOP + 1, 'Press any key to begin this level.', level.Bc, level.Bb)

        elif command == Command.SAVE:
            console.alert(YTOP + 1, ' Are you sure you want to SAVE (Y/N)? ', level.Bc, level.Bb)
            ch = console.read()
            console.reset_colors()
            console.clearkeys()
            # TODO: Writing in the border here...
            console.print(11, 25, ' Pick which letter to SAVE to: A, B, or C?  A  ')
            console.gotoxy(54, 25)
            ch = console.read()
            which_file = ''
            if ch == pygame.constants.K_ESCAPE:
                return
            elif ch == pygame.constants.K_b:
                which_file = 'B'
            elif ch == pygame.constants.K_c:
                which_file = 'C'
            else:
                which_file = 'A'
            save_stuff = SaveType()
            save_stuff.level = player.level
            save_stuff.score = level.initial.score
            save_stuff.gems = level.initial.gems
            save_stuff.whips = level.initial.whips
            save_stuff.teleports = level.initial.teleports
            save_stuff.keys = level.initial.keys
            save_stuff.whip_power = level.initial.whip_power
            save_stuff.difficulty = level.initial.difficulty
            save_stuff.px = level.initial.px
            save_stuff.py = level.initial.py
            save_stuff.found_set = list(level.initial.found_set)
            save_stuff.mix_up = game.MixUp
            # TODO: Writing in the border here...
            console.print(22, 25, '  Saving to file {0}...  '.format(which_file))
            file = Path('DUNGEON{0}.SAV'.format(which_file))
            file.touch()
            with open(file, 'w') as f:
                json.dump(save_stuff, f)
            # TODO: Pause so the player can read what was written
            console.delay(1000)

        elif command == Command.TELEPORT:
            if player.teleports < 1:
                console.sounds(sounds.NoneSound())
                return
            player.teleports -= 1
            display.mark_player_dirty()
            for x in range(1, 250):
                console.gotoxy(*player.position)
                console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
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
                console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
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
            display.mark_player_dirty()
            console.clearkeys()

        elif command == Command.MOVE_NORTH:
            Move(0, -1, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_SOUTH:
            Move(0, 1, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_EAST:
            Move(1, 0, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_WEST:
            Move(-1, 0, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_NORTHWEST:
            Move(-1, -1, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_NORTHEAST:
            Move(1, -1, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_SOUTHWEST:
            Move(-1, 1, PMOVE, game, playfield, player, level, display, console)
        elif command == Command.MOVE_SOUTHEAST:
            Move(1, 1, PMOVE, game, playfield, player, level, display, console)
    else: # command is None
        console.sounds(sounds.Bad_Key())

def Move_Slow(game: Game, playfield: Playfield, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    # Remove monsters the playfield doesn't recognize
    level.slow_monsters = list(filter(lambda sm: playfield[sm] == What.SlowMonster, level.slow_monsters))

    # No-op if there are no monsters
    if len(level.slow_monsters) == 0:
        return
    if level.T[6] > 0: # FastTime is on
        level.slow_monster_timer = level.slow_monster_timer_base * 0.0
    else:
        if level.T[4] > 0: # SlowTime is on
            level.slow_monster_timer = level.slow_monster_timer_base * 5.0
        else:
            level.slow_monster_timer = level.slow_monster_timer_base
    for (i, monster_coord) in enumerate(level.slow_monsters):
        playfield[monster_coord] = What.Nothing # remove the monster before we know whether its move is valid...
        console.gotoxy(*monster_coord)
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        (mx, my) = monster_coord
        if px < mx:
            mx -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > mx:
            mx += 1
            x_dir = -1
        if not level.Sideways:
            if py < my:
                my -= 1
                y_dir = 1
            elif py > my:
                my += 1
                y_dir = -1
        console.gotoxy(mx, my) # After the move!
        occupant = playfield[mx, my] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[mx, my] = What.SlowMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.SlowMonster # Put the monster back
            console.gotoxy(mx, my)
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[mx, my] = What.Nothing # This will remove the monster next filter
            console.write(' ')
            player.score += 1
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sounds(sounds.Monster1_On_Player())
            player.gems -= 1
            if player.gems < 0:
                Dead(True, game, player, level, display, console)

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
            playfield[mx, my] = What.SlowMonster
            console.sounds(sounds.GrabSound())
        else:
            # Monster doesn't move
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.SlowMonster
            console.gotoxy(mx, my)
            console.write(VisibleTiles.SMonster_1 if randrange(2) == 0 else VisibleTiles.SMonster_2, Colors.LightRed)

        if randrange(8) == 1:
            Player_Move(game, playfield, player, level, display, console) # player gets a chance to move after each monster?
        level.slow_monsters[i] = (mx, my)

def Move_Medium(game: Game, playfield: Playfield, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    level.medium_monsters = list(filter(lambda sm: playfield[sm] == What.MediumMonster, level.medium_monsters))
    if len(level.medium_monsters) == 0:
        return
    if level.T[6] > 0: # FastTime is on
        level.medium_monster_timer = level.medium_monster_timer_base * 0.0
    else:
        if level.T[4] > 0: # SlowTime is on
            level.medium_monster_timer = level.medium_monster_timer_base * 5.0
        else:
            level.medium_monster_timer = level.medium_monster_timer_base

    for (i, monster_coord) in enumerate(level.medium_monsters):
        playfield[monster_coord] = What.Nothing # remove the monster before we know whether it's move is valid...
        console.gotoxy(*monster_coord)
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        (mx, my) = monster_coord
        if px < mx:
            mx -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > mx:
            mx += 1
            x_dir = -1
        if not level.Sideways:
            if py < my:
                my -= 1
                y_dir = 1
            elif py > my:
                my += 1
                y_dir = -1
        console.gotoxy(mx, my) # After the move!
        occupant = playfield[mx, my] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[mx, my] = What.MediumMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.MediumMonster # Put the monster back
            console.gotoxy(mx, my)
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[mx, my] = What.Nothing
            console.write(' ')
            player.score += 2
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sounds(sounds.Monster2_On_Player())
            player.gems -= 2
            if player.gems < 0:
                Dead(True, game, player, level, display, console)

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
            playfield[mx, my] = What.MediumMonster
            console.sounds(sounds.GrabSound())
        else:
            # Monster doesn't move
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.MediumMonster
            console.gotoxy(mx, my)
            console.write(VisibleTiles.MMonster_1 if randrange(2) == 0 else VisibleTiles.MMonster_2, Colors.LightGreen)
        if randrange(7) == 1:
            Player_Move(game, playfield, player, level, display, console) # player gets a chance to move after each monster?
        level.medium_monsters[i] = (mx, my)

def Move_Fast(game: Game, playfield: Playfield, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    level.fast_monsters = list(filter(lambda sm: playfield[sm] == What.FastMonster, level.fast_monsters))
    if len(level.fast_monsters) == 0:
        return
    if level.T[6] > 0: # FastTime is on
        level.fast_monster_timer = level.fast_monster_timer * 0.0 # 3 on FastPC
    else:
        if level.T[4] > 0: # SlowTime is on
            level.fast_monster_timer = level.fast_monster_timer_base * 5.0
        else:
            level.fast_monster_timer = level.fast_monster_timer_base
    for (i, monster_coord) in enumerate(level.fast_monsters):
        playfield[monster_coord] = What.Nothing # remove the monster before we know whether it's move is valid...
        console.gotoxy(*monster_coord)
        console.write(' ')
        # How far we've moved the monster before we realized it can't move?
        x_dir = 0
        y_dir = 0
        (px, py) = player.position
        (mx, my) = monster_coord
        if px < mx:
            mx -= 1 # change the monster's state before we know whether this move is valid...
            x_dir = 1
        elif px > mx:
            mx += 1
            x_dir = -1
        if not level.Sideways:
            if py < my:
                my -= 1
                y_dir = 1
            elif py > my:
                my += 1
                y_dir = -1
        console.gotoxy(mx, my) # After the move!
        occupant = playfield[mx, my] # What's in the space the monster may have moved to
        # Things that don't stop a monster
        if occupant in WhatSets.monster_empty_spaces:
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
            console.sound(20, 0.3) # sounds.Monster_Steps()
            playfield[mx, my] = What.FastMonster # Confirm the move
        # Things a monster can't move through
        elif occupant in WhatSets.monster_blocked:
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.FastMonster # Put the monster back
            console.gotoxy(mx, my)
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        # Things with mutual destruction
        elif occupant in WhatSets.monster_self_destruct:
            playfield[mx, my] = What.Nothing
            console.write(' ')
            player.score += 3
            console.sounds(sounds.Monster_Self_Destruction())
        elif occupant == What.Player: # The player!
            console.sounds(sounds.Monster3_On_Player())
            player.gems -= 3
            if player.gems < 0:
                Dead(True, game, player, level, display, console)

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
            playfield[mx, my] = What.FastMonster
            console.sounds(sounds.GrabSound())
        else:
            mx += x_dir
            my += y_dir
            playfield[mx, my] = What.FastMonster
            console.gotoxy(mx, my)
            console.write(VisibleTiles.FMonster_1, Colors.LightBlue)
        if randrange(6) == 1:
            Player_Move(game, playfield, player, level, display, console) # player gets a chance to move after each monster?
        level.fast_monsters[i] = (mx, my)

def Move_MBlock():
    pass

def Run(console: Crt):
    game = Game()
    level = Level()
    playfield = Playfield(64, 23)
    player = PlayerState()
    display = GameDisplay(playfield.bounds(), console)
    Screen(game, console)
    NewGame(game, playfield, player, level, display, console)

def NewGame(game: Game, playfield: Playfield, player: PlayerState, level: Level, display: GameDisplay, console: Crt):
    console.reset_colors()
    Title(game, level, console)
    Init_Screen(game, player, playfield, level, console)
    player.level = 1
    display.mark_player_dirty()
    Next_Level(player, playfield, level)

    display.new_level(playfield)
    level.initial.score = player.score
    level.initial.gems = player.gems
    level.initial.whips = player.whips
    level.initial.teleports = player.teleports
    level.initial.keys = player.keys
    level.initial.whip_power = player.whip_power
    level.initial.difficulty = game.Difficulty
    level.initial.px = player.position[0]
    level.initial.py = player.position[1]
    level.initial.found_set = list(game.FoundSet)
    for x in range(1, 800):
        console.gotoxy(*player.position)
        console.write(VisibleTiles.Player, Colors.Random(), Colors.RandomDark())
        console.sound(x // 2, 3) # sounds.NewGame()
    console.gotoxy(*player.position)
    console.write(VisibleTiles.Player, Colors.Yellow)
    console.clearkeys()
    display.alert('Press any key to begin this level.', bottom = True)
    while not game.Restart:
        Player_Move(game, playfield, player, level, display, console)
        if console.keypressed():
            level.SkipTime = 801
        else:
            level.SkipTime += 1
        if level.SkipTime > 800:
            for x in range(1, TMAX):
                level.T[x] -= 1
            level.SkipTime = 0 # -150 for FastPC
            if level.T[7] < 1: # Freeze is not active
                if level.slow_monster_timer <= 0:
                    Move_Slow(game, playfield, player, level, display, console)
                if level.medium_monster_timer <= 0:
                    Move_Medium(game, playfield, player, level, display, console)
                if level.fast_monster_timer <= 0:
                    Move_Fast(game, playfield, player, level, display, console)
    NewGame(game, playfield, player, level, display, console)
