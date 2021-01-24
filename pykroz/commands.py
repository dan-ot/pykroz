from enum import Enum
from typing import Optional
from pygame.event import Event

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

def command_from_key_event(event: Event) -> Optional[Command]:
    if event.key == pygame.locals.K_EQUALS or event.key == pygame.locals.K_KP_PLUS:
        return Command.DISCOVERY_CLEAR
    elif event.key == pygame.locals.K_MINUS or event.key == pygame.locals.K_KP_MINUS:
        return Command.DISCOVERY_FULL
    elif event.key == pygame.locals.K_9:
        return Command.CREATE_STAIRS
    elif event.key == pygame.locals.K_0:
        return Command.GRANT_STUFF
    elif event.key == pygame.locals.K_PAUSE or event.key == pygame.locals.K_p:
        return Command.PAUSE
    elif event.key == pygame.locals.K_ESCAPE or event.key == pygame.locals.K_q:
        return Command.QUIT
    elif event.key == pygame.locals.K_r:
        return Command.RESTORE
    elif event.key == pygame.locals.K_s:
        return Command.SAVE
    elif event.key == pygame.locals.K_t:
        return Command.TELEPORT
    elif event.key == pygame.locals.K_w:
        return Command.WHIP
    elif event.key == pygame.locals.K_u or event.key == pygame.locals.K_KP7:
        return Command.MOVE_NORTHWEST
    elif event.key == pygame.locals.K_UP or event.key == pygame.locals.K_i or event.key == pygame.locals.K_KP8:
        return Command.MOVE_NORTH
    elif event.key == pygame.locals.K_o or event.key == pygame.locals.K_KP9:
        return Command.MOVE_NORTHEAST
    elif event.key == pygame.locals.K_LEFT or event.key == pygame.locals.K_j or event.key == pygame.locals.K_KP4:
        return Command.MOVE_WEST
    elif event.key == pygame.locals.K_RIGHT or event.key == pygame.locals.K_k or event.key == pygame.locals.K_KP6:
        return Command.MOVE_EAST
    elif event.key == pygame.locals.K_n or event.key == pygame.locals.K_KP1:
        return Command.MOVE_SOUTHWEST
    elif event.key == pygame.locals.K_DOWN or event.key == pygame.locals.K_m or event.key == pygame.locals.K_KP2:
        return Command.MOVE_SOUTH
    elif event.key == pygame.locals.K_COMMA or event.key == pygame.locals.K_KP3:
        return Command.MOVE_SOUTHEAST
    
    