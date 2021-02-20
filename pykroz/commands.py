from enum import Enum
from typing import Optional, Tuple

import pygame.constants

class Command(Enum):
    UTILITY1 = 1
    UTILITY2 = 2
    SPECIAL1 = 3
    SPECIAL2 = 4
    SELECT = 80
    MENU = 81
    BACK = 82
    ACTIVATE = 83
    DEFEND = 84
    ATTACK = 87
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
        return Command.UTILITY2
    if key == pygame.constants.K_MINUS or key == pygame.constants.K_KP_MINUS:
        return Command.UTILITY1
    if key == pygame.constants.K_9:
        return Command.SPECIAL1
    if key == pygame.constants.K_0:
        return Command.SPECIAL2
    if key == pygame.constants.K_PAUSE or key == pygame.constants.K_p:
        return Command.SELECT
    if key == pygame.constants.K_ESCAPE or key == pygame.constants.K_q:
        return Command.MENU
    if key == pygame.constants.K_r:
        return Command.BACK
    if key == pygame.constants.K_s:
        return Command.ACTIVATE
    if key == pygame.constants.K_t:
        return Command.DEFEND
    if key == pygame.constants.K_w:
        return Command.ATTACK
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
        return Command.ACTIVATE
    if button == pygame.constants.CONTROLLER_BUTTON_B:
        return Command.BACK
    if button == pygame.constants.CONTROLLER_BUTTON_X:
        return Command.ATTACK
    if button == pygame.constants.CONTROLLER_BUTTON_Y:
        return Command.DEFEND
    if button == pygame.constants.CONTROLLER_BUTTON_BACK:
        return Command.MENU
    if button == pygame.constants.CONTROLLER_BUTTON_START:
        return Command.SELECT

    if button == pygame.constants.CONTROLLER_BUTTON_LEFTSHOULDER:
        return Command.UTILITY2
    if button == pygame.constants.CONTROLLER_BUTTON_RIGHTSHOULDER:
        return Command.UTILITY1

    if button == pygame.constants.CONTROLLER_BUTTON_LEFTSTICK:
        return Command.SPECIAL1
    if button == pygame.constants.CONTROLLER_BUTTON_RIGHTSTICK:
        return Command.SPECIAL2

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
