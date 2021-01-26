from abc import ABCMeta, abstractmethod
from typing import Tuple
from enum import Enum

from pygame.locals import Color

from ascii import ASCII
from crt import Crt
from levels import Game, Level

class VisibleTiles(Enum):
    Null       = ASCII.Char[0]
    Breakable_Wall      = ASCII.Char[178]
    Whip       = ASCII.Char[244]
    Stairs     = ASCII.Char[240]
    Chest      = ASCII.Char[67]
    SlowTime   = ASCII.Char[232]
    Gem        = ASCII.Char[4]
    Invisible  = ASCII.Char[173]
    Teleport   = ASCII.Char[24]
    Key        = ASCII.Char[140]
    Door       = ASCII.Char[236]
    Wall       = ASCII.Char[219]
    SpeedTime  = ASCII.Char[233]
    Trap       = ASCII.Char[249]
    River      = ASCII.Char[247]
    Power      = ASCII.Char[9]
    Forest     = ASCII.Char[219]
    Tree       = ASCII.Char[5]
    Bomb       = ASCII.Char[157]
    Lava       = ASCII.Char[178]
    Pit        = ASCII.Char[176]
    Tome       = ASCII.Char[245]
    Tunnel     = ASCII.Char[239]
    Freeze     = ASCII.Char[159]
    Nugget     = ASCII.Char[15]
    Quake      = ASCII.Char[0]
    IBlock     = ASCII.Char[30]
    IWall      = ASCII.Char[0]
    IDoor      = ASCII.Char[0]
    Stop       = ASCII.Char[0]
    Trap2      = ASCII.Char[0]
    Zap        = ASCII.Char[30]
    Create     = ASCII.Char[31]
    Generator  = ASCII.Char[6]
    Trap3      = ASCII.Char[0]
    MBlock     = ASCII.Char[178]
    Trap4      = ASCII.Char[0]
    Player     = ASCII.Char[2]
    SMonster_1 = ASCII.Char[142]
    SMonster_2 = ASCII.Char[65]
    MMonster_1 = ASCII.Char[153]
    MMonster_2 = ASCII.Char[148]
    FMonster_1 = ASCII.Char[234]
    Tile       = ASCII.Char[0]
    ShowGems   = ASCII.Char[0]
    ZBlock     = ASCII.Char[178]
    BlockSpell = ASCII.Char[0]
    Chance     = ASCII.Char[63]
    Statue     = ASCII.Char[1]
    WallVanish = ASCII.Char[0]
    OWall1     = ASCII.Char[219]
    OWall2     = ASCII.Char[219]
    OWall3     = ASCII.Char[219]
    CWall1     = ASCII.Char[0]
    Cwall2     = ASCII.Char[0]
    CWall3     = ASCII.Char[0]
    OSpell1    = ASCII.Char[127]
    OSpell2    = ASCII.Char[127]
    OSpell3    = ASCII.Char[127]
    CSpell1    = ASCII.Char[0]
    CSpell2    = ASCII.Char[0]
    CSpell3    = ASCII.Char[0]
    GBlock     = ASCII.Char[178]
    Rock       = ASCII.Char[79]
    EWall      = ASCII.Char[88]
    Trap5      = ASCII.Char[0]
    TBlock     = ASCII.Char[0]
    TRock      = ASCII.Char[0]
    TGem       = ASCII.Char[0]
    TBlind     = ASCII.Char[0]
    TWhip      = ASCII.Char[0]
    TGold      = ASCII.Char[0]
    TTree      = ASCII.Char[0]
    Rope       = ASCII.Char[179]
    DropRope   = ASCII.Char[25]
    Amulet     = ASCII.Char[12]
    ShootRight = ASCII.Char[26]
    ShootLeft  = ASCII.Char[27]
    Trap6      = ASCII.Char[0]
    Trap7      = ASCII.Char[0]
    Trap8      = ASCII.Char[0]
    Trap9      = ASCII.Char[0]
    Trap10     = ASCII.Char[0]
    Trap11     = ASCII.Char[0]
    Trap12     = ASCII.Char[0]
    Trap13     = ASCII.Char[0]
    Message    = ASCII.Char[5]

class What(Enum):
    Nothing = 0
    SlowMonster = 1
    MediumMonster = 2
    FastMonster = 3
    Breakable_Wall = 4
    Whip = 5
    Stairs = 6
    Chest = 7
    SlowTime = 8
    Gem = 9
    Invisibility = 10
    TeleportScroll = 11
    Key = 12
    Door = 13
    Wall = 14
    SpeedTime = 15
    TeleportTrap = 16
    River = 17
    WhipPower = 18
    Forest = 19
    Tree = 20
    Bomb = 21
    Lava = 22
    Pit = 23
    Tome = 24
    Tunnel = 25
    Freeze = 26
    Nugget = 27
    Quake = 28
    Invisible_Breakable_Wall = 29
    Invisible_Wall = 30
    Invisible_Door = 31
    Stop = 32
    Trap_2 = 33
    W_ThirtyFour = 34
    Create = 35
    Generator = 36
    W_ThirtySeven = 37
    MBlock = 38
    W_ThirtyNine = 39
    Player = 40
    W_FourtyOne = 41
    W_FourtyTwo = 42
    Breakable_Wall_2 = 43

    W_FourtyFive = 45


    W_FourtyEight = 48
    W_FourtyNine = 49
    W_Fifty = 50
    W_FiftyOne = 51



    W_FiftyFive = 55
    W_FiftySix = 56
    W_FiftySeven = 57






    Breakable_Wall_3 = 64

    W_SixtySix = 66
    W_SixtySeven = 67
    W_SixtyEight = 68
    W_SixtyNine = 69
    W_Seventy = 70
    W_SeventyOne = 71
    W_SeventyTwo = 72
    W_SeventyThree = 73
    W_SeventyFour = 74
    Rope = 75
    # . . . 
    ExclamationPoint = 222

    
    W_TwoTwentyFour = 224
    W_TwoTwentyFive = 225
    W_TwoTwentySix = 226
    W_TwoTwentySeven = 227
    W_TwoTwentyEight = 228
    W_TwoTwentyNine = 229
    W_TwoThirty = 230
    W_TwoThirtyOne = 231
    Writing = 300

class WhatSets():
    cleared_by_stairs = {
        What.Nothing,
        What.SlowTime,
        What.SpeedTime,
        What.River,
        What.Forest,
        What.Tree,
        What.Bomb,
        What.Lava,
        What.Freeze,
        What.Quake,
        What.Generator,
        What.W_SixtySix
    }

    destroyed_by_bomb = {
        What.Nothing,
        What.SlowMonster,
        What.MediumMonster,
        What.FastMonster,
        What.Breakable_Wall,
        What.Door,
        What.TeleportTrap,
        What.Forest,
        What.Quake,
        What.Invisible_Breakable_Wall,
        What.Invisible_Wall,
        What.Invisible_Door,
        What.Stop,
        What.Create,
        What.Generator,
        What.W_ThirtySeven,
        What.MBlock,
        What.W_ThirtyNine,
        What.Breakable_Wall_2,
        What.W_FourtyFive,
        What.W_FourtyEight,
        What.W_FourtyNine,
        What.W_Fifty,
        What.W_FiftyOne,
        What.Breakable_Wall_3,
        What.W_SixtySeven,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour,
        What.W_TwoTwentyFour,
        What.W_TwoTwentyFive,
        What.W_TwoTwentySix,
        What.W_TwoTwentySeven,
        What.W_TwoTwentyEight,
        What.W_TwoTwentyNine,
        What.W_TwoThirty,
        What.W_TwoThirtyOne
    }

    doesnt_block_tunnel_exit = {
        What.Nothing,
        What.Stop,
        What.Trap_2,
        What.W_ThirtySeven,
        What.W_ThirtyNine,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven,
        What.W_SixtySeven,
        What.W_TwoTwentyFour,
        What.W_TwoTwentyFive,
        What.W_TwoTwentySix,
        What.W_TwoTwentySeven,
        What.W_TwoTwentyEight,
        What.W_TwoTwentyNine,
        What.W_TwoThirty,
        What.W_TwoThirtyOne
    }

    becomes_replacement_with_tunnelling = {
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven
    }

    crushed_in_an_earthquake = {
        What.Nothing,
        What.SlowMonster,
        What.MediumMonster,
        What.FastMonster,
        What.Whip,
        What.Chest,
        What.SlowTime,
        What.Gem,
        What.Invisibility,
        What.TeleportScroll,
        What.SpeedTime,
        What.TeleportTrap,
        What.Freeze,
        What.Stop,
        What.Trap_2,
        What.W_ThirtySeven,
        What.W_ThirtyNine,
        What.W_SixtySeven,
        What.W_TwoTwentyFour,
        What.W_TwoTwentyFive,
        What.W_TwoTwentySix,
        What.W_TwoTwentySeven,
        What.W_TwoTwentyEight,
        What.W_TwoTwentyNine,
        What.W_TwoThirty,
        What.W_TwoThirtyOne
    }

def parse(chr: str) -> What:
    if   chr == ' ':
        return What.Nothing
    elif chr == '1':
        return What.SlowMonster
    elif chr == '2':
        return What.MediumMonster
    elif chr == '3':
        return What.FastMonster
    elif chr == 'X':
        return What.Breakable_Wall
    elif chr == 'W':
        return What.Whip
    elif chr == 'L':
        return What.Stairs
    elif chr == 'C':
        return What.Chest
    elif chr == 'S':
        return What.SlowTime
    elif chr == '+':
        return What.Gem
    elif chr == 'I':
        return What.Invisibility
    elif chr == 'T':
        return What.TeleportScroll
    elif chr == 'K':
        return What.Key
    elif chr == 'D':
        return What.Door
    elif chr == '#':
        return What.Wall
    elif chr == 'F':
        return What.SpeedTime
    elif chr == '.':
        return What.TeleportTrap
    elif chr == 'R':
        return What.River
    elif chr == 'Q':
        return What.WhipPower
    elif chr == '/':
        return What.Forest
    elif chr == '\\':
        return What.Tree
    elif chr == 'B':
        return What.Bomb
    elif chr == 'V':
        return What.Lava
    elif chr == '=':
        return What.Pit
    elif chr == 'A':
        return What.Tome
    elif chr == 'U':
        return What.Tunnel
    elif chr == 'Z':
        return What.Freeze
    elif chr == '*':
        return What.Nugget
    elif chr == 'E':
        return What.Quake
    elif chr == ';':
        return What.Invisible_Breakable_Wall
    elif chr == ':':
        return What.Invisible_Wall
    elif chr == '`':
        return What.Invisible_Door
    elif chr == '-':
        return What.Stop
    elif chr == '@':
        return What.Trap_2
    elif chr == '%':
        return What.W_ThirtyFour
    elif chr == ']':
        return What.Create
    elif chr == 'G':
        return What.Generator
    elif chr == '(':
        return What.W_ThirtySeven
    elif chr == 'P':
        return What.Player
    elif chr == '!':
        return What.ExclamationPoint
    else:
        print("Unknown What: [{0}]".format(chr))
        return What.Writing
    