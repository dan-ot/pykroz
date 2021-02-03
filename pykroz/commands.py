from enum import Enum
from typing import Optional, Tuple

import pygame.constants

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

def command_from_key_code(key: int) -> Optional[Command]:
    if key == pygame.constants.K_EQUALS or key == pygame.constants.K_KP_PLUS:
        return Command.DISCOVERY_CLEAR
    if key == pygame.constants.K_MINUS or key == pygame.constants.K_KP_MINUS:
        return Command.DISCOVERY_FULL
    if key == pygame.constants.K_9:
        return Command.CREATE_STAIRS
    if key == pygame.constants.K_0:
        return Command.GRANT_STUFF
    if key == pygame.constants.K_PAUSE or key == pygame.constants.K_p:
        return Command.PAUSE
    if key == pygame.constants.K_ESCAPE or key == pygame.constants.K_q:
        return Command.QUIT
    if key == pygame.constants.K_r:
        return Command.RESTORE
    if key == pygame.constants.K_s:
        return Command.SAVE
    if key == pygame.constants.K_t:
        return Command.TELEPORT
    if key == pygame.constants.K_w:
        return Command.WHIP
    if key == pygame.constants.K_u or key == pygame.constants.K_KP7:
        return Command.MOVE_NORTHWEST
    if key == pygame.constants.K_UP or key == pygame.constants.K_i or key == pygame.constants.K_KP8:
        return Command.MOVE_NORTH
    if key == pygame.constants.K_o or key == pygame.constants.K_KP9:
        return Command.MOVE_NORTHEAST
    if key == pygame.constants.K_LEFT or key == pygame.constants.K_j or key == pygame.constants.K_KP4:
        return Command.MOVE_WEST
    if key == pygame.constants.K_RIGHT or key == pygame.constants.K_k or key == pygame.constants.K_KP6:
        return Command.MOVE_EAST
    if key == pygame.constants.K_n or key == pygame.constants.K_KP1:
        return Command.MOVE_SOUTHWEST
    if key == pygame.constants.K_DOWN or key == pygame.constants.K_m or key == pygame.constants.K_KP2:
        return Command.MOVE_SOUTH
    if key == pygame.constants.K_COMMA or key == pygame.constants.K_KP3:
        return Command.MOVE_SOUTHEAST

    return None

def command_from_button(button: int) -> Optional[Command]:
    if button == pygame.constants.CONTROLLER_BUTTON_A:
        return Command.SAVE
    if button == pygame.constants.CONTROLLER_BUTTON_B:
        return Command.RESTORE
    if button == pygame.constants.CONTROLLER_BUTTON_X:
        return Command.WHIP
    if button == pygame.constants.CONTROLLER_BUTTON_Y:
        return Command.TELEPORT
    if button == pygame.constants.CONTROLLER_BUTTON_BACK:
        return Command.QUIT
    if button == pygame.constants.CONTROLLER_BUTTON_START:
        return Command.PAUSE

    if button == pygame.constants.CONTROLLER_BUTTON_LEFTSHOULDER:
        return Command.DISCOVERY_CLEAR
    if button == pygame.constants.CONTROLLER_BUTTON_RIGHTSHOULDER:
        return Command.DISCOVERY_FULL

    if button == pygame.constants.CONTROLLER_BUTTON_LEFTSTICK:
        return Command.CREATE_STAIRS
    if button == pygame.constants.CONTROLLER_BUTTON_RIGHTSTICK:
        return Command.GRANT_STUFF

    return None

def command_from_hat(value: Tuple[int, int]) -> Optional[Command]:
    if value == (-1, 1):
        return Command.MOVE_NORTHWEST
    if value == (0, 1):
        return Command.MOVE_NORTH
    if value == (1, 1):
        return Command.MOVE_NORTHEAST
    if value == (-1, 0):
        return Command.MOVE_WEST
    if value == (1, 0):
        return Command.MOVE_EAST
    if value == (-1, -1):
        return Command.MOVE_SOUTHWEST
    if value == (0, -1):
        return Command.MOVE_SOUTH
    if value == (1, -1):
        return Command.MOVE_SOUTHEAST

    return None
