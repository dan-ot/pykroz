from enum import Enum
from random import randrange
from typing import Optional

from pygame import Color

from levels import VisibilityFlags
from engine.ascii import ASCII
from engine.colors import Colors

class VisibleTiles():
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

class What(int, Enum):
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
    Zap = 34
    Create = 35
    Generator = 36
    Trap_3 = 37
    MBlock = 38
    Trap_4 = 39
    Player = 40
    ShowGems = 41
    W_FourtyTwo = 42
    ZBlock = 43
    BlockSpell = 44
    Chance = 45
    Statue = 46
    W_FourtySeven = 47
    W_FourtyEight = 48
    W_FourtyNine = 49
    W_Fifty = 50
    W_FiftyOne = 51
    Wall_2 = 52
    Wall_3 = 53
    Wall_Grey = 54
    W_FiftyFive = 55
    W_FiftySix = 56
    W_FiftySeven = 57
    OSpell1_1 = 58
    OSpell1_2 = 59
    OSpell1_3 = 60
    W_SixtyOne = 61
    W_SixtyTwo = 62
    W_SixtyThree = 63
    Breakable_Wall_Grey = 64
    W_SixtyFive = 65
    EWall = 66
    Trap_5 = 67
    W_SixtyEight = 68
    W_SixtyNine = 69
    W_Seventy = 70
    W_SeventyOne = 71
    W_SeventyTwo = 72
    W_SeventyThree = 73
    W_SeventyFour = 74
    Rope = 75
    DropRope_1 = 76
    DropRope_2 = 77
    DropRope_3 = 78
    DropRope_4 = 79
    DropRope_5 = 80
    Amulet = 81
    ShootRight = 82
    ShootLeft = 83
    # . . .
    ExclamationPoint = 222


    Trap_6 = 224
    Trap_7 = 225
    Trap_8 = 226
    Trap_9 = 227
    Trap_10 = 228
    Trap_11 = 229
    Trap_12 = 230
    Trap_13 = 231

    Tree_2 = 252
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
        What.EWall
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
        What.Trap_3,
        What.MBlock,
        What.Trap_4,
        What.ZBlock,
        What.Chance,
        What.W_FourtyEight,
        What.W_FourtyNine,
        What.W_Fifty,
        What.W_FiftyOne,
        What.Breakable_Wall_Grey,
        What.Trap_5,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    doesnt_block_tunnel_exit = {
        What.Nothing,
        What.Stop,
        What.Trap_2,
        What.Trap_3,
        What.Trap_4,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven,
        What.Trap_5,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    becomes_replacement_with_tunnelling = {
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven
    }

    becomes_replacement_with_go = {
        What.Rope,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven
    }

    becomes_replacement_with_sideways = {
        What.Rope,
        What.DropRope_1,
        What.DropRope_2,
        What.DropRope_3,
        What.DropRope_4,
        What.DropRope_5
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
        What.Trap_3,
        What.Trap_4,
        What.Trap_5,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    auto_discover_on_mixup = {
        What.Nothing,
        What.SlowMonster,
        What.MediumMonster,
        What.FastMonster,
        What.Breakable_Wall,
        What.Whip,
        What.Stairs,
        What.Chest,
        What.SlowTime,
        What.Gem,
        What.Invisibility,
        What.TeleportScroll,
        What.Key,
        What.Door,
        What.Wall,
        What.SpeedTime,
        What.TeleportTrap,
        What.River,
        What.WhipPower,
        What.Forest,
        What.Tree,
        What.Bomb,
        What.Lava,
        What.Pit,
        What.Tome,
        What.Tunnel,
        What.Freeze,
        What.Nugget,
        What.Quake,
        What.Invisible_Breakable_Wall,
        What.Invisible_Wall,
        What.Invisible_Door,
        What.Stop,
        What.Trap_2,
        What.Zap,
        What.Create,
        What.Generator,
        What.Trap_3,
        What.MBlock,
        What.Trap_4,
        What.Player,
        What.ShowGems,
        What.W_FourtyTwo,
        What.ZBlock,
        What.BlockSpell,
        What.Chance,
        What.Statue,
        What.W_FourtySeven,
        What.W_FourtyEight,
        What.W_FourtyNine,
        What.W_Fifty,
        What.W_FiftyOne,
        What.Wall_2,
        What.Wall_3,
        What.Wall_Grey,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven,
        What.OSpell1_1,
        What.OSpell1_2,
        What.OSpell1_3,
        What.W_SixtyOne,
        What.W_SixtyTwo,
        What.W_SixtyThree,
        What.Breakable_Wall_Grey,
        What.W_SixtyFive,
        What.EWall,
        What.Trap_5,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour,
        What.Rope,
        What.DropRope_1,
        What.DropRope_2,
        What.DropRope_3,
        What.DropRope_4,
        What.DropRope_5,
        What.Amulet,
        What.ShootRight,
        What.ShootLeft
    }

    invisible = {
        What.Invisible_Breakable_Wall,
        What.Invisible_Wall,
        What.Invisible_Door,
        What.Stop,
        What.Trap_2,
        What.Trap_3,
        What.Trap_4,
        What.ShowGems,
        What.W_FourtyTwo,
        What.BlockSpell,
        What.Trap_5,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13,
        What.Quake
    }

    monsters = {
        What.SlowMonster,
        What.MediumMonster,
        What.FastMonster
    }

    breakable_obstacles = {
        What.Breakable_Wall,
        What.Forest,
        What.Tree,
        What.Tree_2
    }

    breakable_things = {
        What.Invisibility,
        What.SpeedTime,
        What.TeleportTrap,
        What.WhipPower,
        What.Generator,
        What.W_FourtyEight,
        What.W_FourtyNine,
        What.W_Fifty,
        What.W_FiftyOne
    }

    wall_variants = {
        What.Wall,
        What.Wall_2,
        What.Wall_3
    }

    invisible_to_whip = {
        What.Quake,
        What.Invisible_Breakable_Wall,
        What.Invisible_Wall,
        What.Invisible_Door,
        What.Trap_2,
        What.Trap_3,
        What.Trap_4,
        What.ShowGems,
        What.BlockSpell,
        What.Trap_5,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    ospell_1s = {
        What.OSpell1_1,
        What.OSpell1_2,
        What.OSpell1_3
    }

    invisible_to_whip_2 = {
        What.W_FourtySeven,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven,
        What.W_SixtyOne,
        What.W_SixtyTwo,
        What.W_SixtyThree,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour
    }

    drop_ropes = {
        What.DropRope_1,
        What.DropRope_2,
        What.DropRope_3,
        What.DropRope_4,
        What.DropRope_5
    }

    blocks = {
        What.Breakable_Wall,
        What.ZBlock,
        What.Breakable_Wall_Grey
    }

    breakable_wall_variants = {
        What.MBlock,
        What.ZBlock,
        What.Breakable_Wall_Grey
    }

    teleport_animate_through = {
        What.Nothing,
        What.Stop,
        What.Trap_2,
        What.Trap_3,
        What.Trap_4,
        What.ShowGems,
        What.BlockSpell,
        What.W_FourtySeven,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.W_FiftySeven,
        What.W_SixtyOne,
        What.W_SixtyTwo,
        What.W_SixtyThree,
        What.Trap_5,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    monster_empty_spaces = {
        What.Nothing,
        What.W_SixtyEight,
        What.W_SixtyNine,
        What.W_Seventy,
        What.W_SeventyOne,
        What.W_SeventyTwo,
        What.W_SeventyThree,
        What.W_SeventyFour
    }

    monster_blocked = {
        What.SlowMonster,
        What.MediumMonster,
        What.FastMonster,
        What.Stairs,
        What.Door,
        What.Wall,
        What.River,
        What.Forest,
        What.Tree,
        What.Bomb,
        What.Lava,
        What.Pit,
        What.Tome,
        What.Tunnel,
        What.Quake,
        What.Invisible_Breakable_Wall,
        What.Invisible_Wall,
        What.Invisible_Door,
        What.Stop,
        What.Trap_2,
        What.Zap,
        What.Create,
        What.Generator,
        What.Trap_3,
        What.Trap_4,
        What.ShowGems,
        What.W_FourtyTwo,
        What.BlockSpell,
        What.Chance,
        What.Statue,
        What.W_FourtySeven,
        What.Wall_2,
        What.Wall_3,
        What.Wall_Grey,
        What.W_FiftyFive,
        What.W_FiftySix,
        What.OSpell1_1,
        What.OSpell1_2,
        What.OSpell1_3,
        What.W_SixtyOne,
        What.W_SixtyTwo,
        What.W_SixtyThree,
        What.W_SixtyFive,
        What.EWall,
        What.Trap_5,
        What.Rope,
        What.DropRope_1,
        What.DropRope_2,
        What.DropRope_3,
        What.DropRope_4,
        What.DropRope_5,
        What.Trap_6,
        What.Trap_7,
        What.Trap_8,
        What.Trap_9,
        What.Trap_10,
        What.Trap_11,
        What.Trap_12,
        What.Trap_13
    }

    monster_self_destruct = {
        What.Breakable_Wall,
        What.MBlock,
        What.ZBlock,
        What.Breakable_Wall_Grey
    }

    monster_eats = {
        What.Whip,
        What.Chest,
        What.SlowTime,
        What.Gem,
        What.Invisibility,
        What.TeleportScroll,
        What.Key,
        What.SpeedTime,
        What.TeleportTrap,
        What.WhipPower,
        What.Freeze,
        What.Nugget,
        What.W_FourtyEight,
        What.W_FourtyNine,
        What.W_Fifty,
        What.W_FiftyOne,
        What.ShootRight,
        What.ShootLeft
    }

def parse(character: str) -> What:
    if   character == ' ':
        return What.Nothing
    elif character == '1':
        return What.SlowMonster
    elif character == '2':
        return What.MediumMonster
    elif character == '3':
        return What.FastMonster
    elif character == 'X':
        return What.Breakable_Wall
    elif character == 'W':
        return What.Whip
    elif character == 'L':
        return What.Stairs
    elif character == 'C':
        return What.Chest
    elif character == 'S':
        return What.SlowTime
    elif character == '+':
        return What.Gem
    elif character == 'I':
        return What.Invisibility
    elif character == 'T':
        return What.TeleportScroll
    elif character == 'K':
        return What.Key
    elif character == 'D':
        return What.Door
    elif character == '#':
        return What.Wall
    elif character == 'F':
        return What.SpeedTime
    elif character == '.':
        return What.TeleportTrap
    elif character == 'R':
        return What.River
    elif character == 'Q':
        return What.WhipPower
    elif character == '/':
        return What.Forest
    elif character == '\\':
        return What.Tree
    elif character == 'B':
        return What.Bomb
    elif character == 'V':
        return What.Lava
    elif character == '=':
        return What.Pit
    elif character == 'A':
        return What.Tome
    elif character == 'U':
        return What.Tunnel
    elif character == 'Z':
        return What.Freeze
    elif character == '*':
        return What.Nugget
    elif character == 'E':
        return What.Quake
    elif character == ';':
        return What.Invisible_Breakable_Wall
    elif character == ':':
        return What.Invisible_Wall
    elif character == '`':
        return What.Invisible_Door
    elif character == '-':
        return What.Stop
    elif character == '@':
        return What.Trap_2
    elif character == '%':
        return What.Zap
    elif character == ']':
        return What.Create
    elif character == 'G':
        return What.Generator
    elif character == '(':
        return What.Trap_3
    elif character == 'P':
        return What.Player
    elif character == '!':
        return What.ExclamationPoint
    else:
        print("Unknown What: [{0}]".format(character))
        return What.Writing

class DrawResponse():
    def __init__(self, char: str, fg: Optional[Color] = None, bg: Optional[Color] = None, blinking: bool = False):
        self.char = char
        self.fg = fg
        self.bg = bg
        self.blinking = blinking

    @staticmethod
    def empty() -> "DrawResponse":
        return DrawResponse(' ')

def chance_of(what: What) -> Optional[int]:
    if what == What.Chest:
        return 20
    if what == What.SlowTime:
        return 35
    if what == What.Key:
        return 25
    if what == What.SpeedTime:
        return 10
    if what == What.WhipPower:
        return 15
    if what == What.Bomb:
        return 40
    if what == What.Quake:
        return 15
    return None

def draw(what: What, visibility: VisibilityFlags) -> DrawResponse:
    if what == What.Nothing:
        return DrawResponse(VisibleTiles.Tile)
    if what == What.SlowMonster:
        return DrawResponse(VisibleTiles.SMonster_1, Colors.LightRed)
    if what == What.MediumMonster:
        return DrawResponse(VisibleTiles.MMonster_1, Colors.LightGreen)
    if what == What.FastMonster:
        return DrawResponse(VisibleTiles.FMonster_1, Colors.LightBlue)
    if what == What.Breakable_Wall:
        return DrawResponse(VisibleTiles.Breakable_Wall, Colors.Brown)
    if what == What.Whip:
        return DrawResponse(VisibleTiles.Whip, Colors.White)
    if what == What.Stairs:
        if VisibilityFlags.HIDE_STAIRS in visibility:
            return DrawResponse.empty()
        else:
            return DrawResponse(VisibleTiles.Stairs, Colors.Black, Colors.LightGrey, blinking = True)
    if what == What.Chest:
        return DrawResponse(VisibleTiles.Chest, Colors.Yellow, Colors.Red)
    if what == What.SlowTime:
        return DrawResponse(VisibleTiles.SlowTime, Colors.LightCyan)
    if what == What.Gem:
        if VisibilityFlags.HIDE_GEMS in visibility:
            return DrawResponse.empty()
        else:
            return DrawResponse(VisibleTiles.Gem)
    if what == What.Invisibility:
        return DrawResponse(VisibleTiles.Invisible, Colors.Blue)
    if what == What.TeleportScroll:
        return DrawResponse(VisibleTiles.Teleport, Colors.LightMagenta)
    if what == What.Key:
        return DrawResponse(VisibleTiles.Key, Colors.LightRed)
    if what == What.Door:
        return DrawResponse(VisibleTiles.Door, Colors.Cyan, Colors.Magenta)
    if what == What.Wall:
        return DrawResponse(VisibleTiles.Wall, Colors.Brown)
    if what == What.SpeedTime:
        return DrawResponse(VisibleTiles.SpeedTime, Colors.LightCyan)
    if what == What.TeleportTrap:
        if VisibilityFlags.HIDE_TRAP in visibility:
            return DrawResponse.empty()
        else:
            return DrawResponse(VisibleTiles.Trap, Colors.LightGrey)
    if what == What.River:
        if randrange(15) == 0:
            return DrawResponse(VisibleTiles.Lava, Colors.White, Colors.Blue)
        else:
            return DrawResponse(VisibleTiles.River, Colors.LightBlue, Colors.Blue)
    if what == What.WhipPower:
        return DrawResponse(VisibleTiles.Power, Colors.White)
    if what == What.Forest:
        return DrawResponse(VisibleTiles.Forest, Colors.Green)
    if what in (What.Tree, What.Tree_2):
        return DrawResponse(VisibleTiles.Tree, Colors.Brown, Colors.Green)
    if what == What.Bomb:
        return DrawResponse(VisibleTiles.Bomb, Colors.White)
    if what == What.Lava:
        return DrawResponse(VisibleTiles.Lava, Colors.LightRed, Colors.Red)
    if what == What.Pit:
        return DrawResponse(VisibleTiles.Pit, Colors.LightGrey)
    if what == What.Tome:
        return DrawResponse(VisibleTiles.Tome, Colors.White, Colors.Magenta, blinking = True)
    if what == What.Tunnel:
        return DrawResponse(VisibleTiles.Tunnel, Colors.White)
    if what == What.Freeze:
        return DrawResponse(VisibleTiles.Freeze, Colors.LightGreen)
    if what == What.Nugget:
        return DrawResponse(VisibleTiles.Nugget, Colors.Yellow)
    if what == What.Zap:
        return DrawResponse(VisibleTiles.Zap, Colors.LightRed)
    if what == What.Create:
        if VisibilityFlags.HIDE_CREATE in visibility:
            return DrawResponse.empty()
        else:
            return DrawResponse(VisibleTiles.Chance, Colors.White)
    if what == What.Generator:
        return DrawResponse(VisibleTiles.Generator, Colors.Yellow, blinking = True)
    if what == What.MBlock:
        if VisibilityFlags.HIDE_M_BLOCK in visibility:
            return DrawResponse.empty()
        else:
            return DrawResponse(VisibleTiles.MBlock, Colors.Brown)
    if what == What.Player:
        return DrawResponse(VisibleTiles.Player, Colors.Yellow)
    if what == What.ZBlock:
        return DrawResponse(VisibleTiles.ZBlock, Colors.Brown)
    if what == What.Chance:
        return DrawResponse(VisibleTiles.Chance, Colors.White)
    if what == What.Statue:
        return DrawResponse(VisibleTiles.Statue, Colors.White, blinking = True)
    if what == What.ExclamationPoint:
        return DrawResponse('!', Colors.White, Colors.Brown)
    if what in WhatSets.invisible:
        return DrawResponse.empty()

    # TODO: Mark letters appropriately, not as int-able Whats
    return DrawResponse(ASCII.Char[int(what)].upper(), Colors.White, Colors.Brown)

def score_for(what: What, level: int) -> int:
    if what in WhatSets.monsters: # Monsters
        return int(What)
    if what in (What.Breakable_Wall, What.Wall): # Block
        return -2
    if what == What.Whip:
        return 1
    if what == What.Stairs:
        return level
    if what == What.Chest:
        return 5
    if what == What.Gem:
        return 1
    if what == What.Invisibility:
        return 10
    if what == What.TeleportScroll:
        return 1
    if what == What.SpeedTime:
        return 2
    if what == What.TeleportTrap:
        return -5
    if what == What.Lava:
        return 25
    if what == What.Tree:
        return -level // 2
    if what == What.Nugget:
        return 50
    if what == What.Create:
        return level * 2
    if what == What.Generator:
        return 50
    if what == What.MBlock:
        return 1

    return 0
