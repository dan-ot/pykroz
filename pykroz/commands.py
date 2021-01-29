from enum import Enum
from typing import Optional

import pygame.locals

class Command(Enum):
    DISCOVERY_FULL = 1
    DISCOVERY_CLEAR = 2
    CREATE_STAIRS = 3
    GRANT_STUFF = 4
    PAUSE = 80
    QUIT = 81
    RESTORE = 82
    SAVE = 83
    TELEPORT = 84
    WHIP = 87
    MOVE_NORTHWEST = 171
    MOVE_NORTH = 172
    MOVE_NORTHEAST = 173
    MOVE_WEST = 175
    MOVE_EAST = 177
    MOVE_SOUTHWEST = 179
    MOVE_SOUTH = 180
    MOVE_SOUTHEAST = 181

def command_from_key_code(key: Optional[int]) -> Optional[Command]:
    if key == pygame.locals.K_EQUALS or key == pygame.locals.K_KP_PLUS:
        return Command.DISCOVERY_CLEAR
    elif key == pygame.locals.K_MINUS or key == pygame.locals.K_KP_MINUS:
        return Command.DISCOVERY_FULL
    elif key == pygame.locals.K_9:
        return Command.CREATE_STAIRS
    elif key == pygame.locals.K_0:
        return Command.GRANT_STUFF
    elif key == pygame.locals.K_PAUSE or key == pygame.locals.K_p:
        return Command.PAUSE
    elif key == pygame.locals.K_ESCAPE or key == pygame.locals.K_q:
        return Command.QUIT
    elif key == pygame.locals.K_r:
        return Command.RESTORE
    elif key == pygame.locals.K_s:
        return Command.SAVE
    elif key == pygame.locals.K_t:
        return Command.TELEPORT
    elif key == pygame.locals.K_w:
        return Command.WHIP
    elif key == pygame.locals.K_u or key == pygame.locals.K_KP7:
        return Command.MOVE_NORTHWEST
    elif key == pygame.locals.K_UP or key == pygame.locals.K_i or key == pygame.locals.K_KP8:
        return Command.MOVE_NORTH
    elif key == pygame.locals.K_o or key == pygame.locals.K_KP9:
        return Command.MOVE_NORTHEAST
    elif key == pygame.locals.K_LEFT or key == pygame.locals.K_j or key == pygame.locals.K_KP4:
        return Command.MOVE_WEST
    elif key == pygame.locals.K_RIGHT or key == pygame.locals.K_k or key == pygame.locals.K_KP6:
        return Command.MOVE_EAST
    elif key == pygame.locals.K_n or key == pygame.locals.K_KP1:
        return Command.MOVE_SOUTHWEST
    elif key == pygame.locals.K_DOWN or key == pygame.locals.K_m or key == pygame.locals.K_KP2:
        return Command.MOVE_SOUTH
    elif key == pygame.locals.K_COMMA or key == pygame.locals.K_KP3:
        return Command.MOVE_SOUTHEAST
    else:
        return None
