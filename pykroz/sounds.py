from random import randint
from typing import Sequence, Tuple, Union

SampleSet = Sequence[Tuple[Union[None, int], int]]

def FootStep() -> SampleSet:
    parts: SampleSet = []
    for _ in range(5):
        freq = randint(0, 500) + 350
        parts.append((freq, 1))
    parts.append((None, 120))
    for _ in range(6):
        freq = randint(0, 50) + 150
        parts.append((freq, 4))
    return parts

def GrabSound() -> SampleSet:
    return [(randint(1, 1000) + 1000, 0.5) for _ in range(50)]

def BlockSound() -> SampleSet:
    return [(x, 30) for x in range(60, 30, -3)]

def NoneSound() -> SampleSet:
    parts = []
    for _ in range(5):
        parts.append((400, 10))
        parts.append((None, 10))
        parts.append((700, 10))
        parts.append((None, 10))
    return parts

def Static() -> SampleSet:
    parts = []
    for _ in range(33):
        if randint(0, 1) == 0:
            for _ in range(randint(0, 60) + 10):
                parts.append((randint(0, 4000) + 3000, 1))
        else:
            parts.append((None, randint(3, 30)))
    return parts

def Points_For_Gems(gem: int) -> SampleSet:
    return [(gem * 8 + 100, 20)]

def Points_For_Whips(whip: int) -> SampleSet:
    return [(whip * 10 + 200, 20)]

def Points_For_Teleports(teleport: int) -> SampleSet:
    return [(teleport * 12 + 300, 30)]

def Points_For_Keys(key: int) -> SampleSet:
    return [(key * 30 + 100, 50)]

def Step_On_Monster(monster: int) -> SampleSet:
    return [(200 + 200 * monster, 25)]

def Open_Chest() -> SampleSet:
    parts = []
    for x in range(3, 42):
        for y in range(3, 42):
            parts.append((x * y, 1))
    return parts

def Slow() -> SampleSet:
    return [(x * 50 + 300, x * 10 + 40) for x in range(7, 1, -1)]

def Invisible() -> SampleSet:
    parts = []
    for _ in range(1, 4):
        parts.append((600, 50))
        parts.append((None, 50))
    return parts

def Door_No_Keys() -> SampleSet:
    parts = []
    for _ in range(1, 15):
        parts.append((randint(0, 99) + 30, 15))
        parts.append((None, 15))
    return parts

def Open_Door() -> SampleSet:
    return [(x, 15) for x in range(10, 90)]

def River_Splash() -> SampleSet:
    return [(randint(0, x * 2 + 200) + x, 1) for x in range(1, 500)] # 2000 on FastPC

def Speed() -> SampleSet:
    return [(x * 50 + 300, x * 10 + 40) for x in range(1, 7)]

def Teleport_Trap() -> SampleSet:
    return [(x * y, 1) for x in range(550, 20, -1) for y in range(60, 1, -1)]

def Bomb_Windup() -> SampleSet:
    return [(i * 2, 3) for i in range(70, 600)]

def Lava() -> SampleSet:
    return [(randint(y * x + 100) + y * x, 0.3) for x in range(1400, 20, -1) for y in range(9, 2, -1)] # 2000 on FastPC

def Pit_Splat() -> SampleSet:
    return [(randint(0, i), 0.2) for i in range(8000, 20, -1)]

def Freeze() -> SampleSet:
    return [(randint(0, 1000) + x + 200, 0.3) for x in range(1, 5000)] # 8000 on FastPC

def Quake_Start() -> SampleSet:
    return [(randint(0, i), 0.3) for i in range(1, 2500)] # 5500 on FastPC

def Quake_Block_Drop() -> SampleSet:
    return [(randint(200), 0.3) for _ in range(1, 400)] # 700 on FastPC

def Quake_Finish() -> SampleSet:
    return [(randint(i), 0.3) for i in range(2500, 20, -1)]

def Load_Error() -> SampleSet:
    return [(300, 250)]

def Whip(duration_ms: float) -> SampleSet:
    # play this between whip side effects...
    return [70, duration_ms]

def Whip_Hit() -> SampleSet:
    return [(400, 20), (90, 1)]

def Whip_Breakable_Destroy() -> SampleSet:
    parts = []
    for s in range(3300, 20, -1):
        parts.append((randint(0, s), 0.2))
        parts.append((90, 1))
    return parts

def Whip_Breakable_Hit() -> SampleSet:
    return [(130, 25), (90, 1)]

def Monster_Steps(monsters: int) -> SampleSet:
    parts = []
    for _ in range(1, monsters):
        parts.append((20, 0.3))
        parts.append((None, 0.3))
    return parts

def Monster_Self_Destruction() -> SampleSet:
    return [(800, 18), (400, 20)]

def Monster1_On_Player() -> SampleSet:
    return [(400, 25)]

def Monster2_On_Player() -> SampleSet:
    return [(600, 25)]

def Monster3_On_Player() -> SampleSet:
    return [(800, 25)]

def Color_Prompt() -> SampleSet:
    return [(500, 30)]

def Speed_Prompt() -> SampleSet:
    return [(300, 30)]

def Difficulty_Key() -> SampleSet:
    return [(300, 100)]

def Difficulty_Prompt() -> SampleSet:
    return [(700, 100)]

def Begin_Game() -> SampleSet:
    return [(x * y * y, y / 2) for x in range(100, 20, -1) for y in range(10, 1, -1)]

def Bad_Key() -> SampleSet:
    return [
        (540, 40),
        (100, 15),
        (None, 15)
        (100, 15),
        (None, 15)
        (100, 15),
        (None, 15)
        (100, 15),
        (None, 15)
    ]

def Generate_Stairs() -> SampleSet:
    return [(2000, 40)]

def Pause() -> SampleSet:
    parts = [(500, 100)]
    for x in range(200, 100, -1):
        parts.append((x, 2))
    return parts

def Quit() -> SampleSet:
    return [
        (600, 100),
        (450, 100),
        (300, 100),
        (99, 99)
    ]

def Teleport() -> SampleSet:
    parts = []
    x = 0
    while x < 90:
        x += 2
        y = 0
        while y < 220:
            y += 1
            parts.append((x * y, 0.3))
    return parts

# Integrated with behavior/animation...
def Death() -> SampleSet:
    parts = []
    for x in range(150, 5, -1):
        parts.append((x * x, 0.5))
    return parts

def Victory_MacGuffin() -> SampleSet:
    parts = []
    for x in range(1, 24):
        for y in range(5, 1, -1):
            parts.append((x * 45 + y * 10, y * 3))
            parts.append((None, 40))
    return parts

def Victory_MacGuffin_2(b: int, x: int, y: int) -> SampleSet:
    # Played inside three loops, but only conditionally...
    return [(x * y* (b + 1), 0.3)]

def Victory_Strange() -> SampleSet:
    parts = []
    for x in range(1, 250):
        parts.append((randint(0, 3000) + x, 0.5))
    for y in range(2200, 20, -1):
        parts.append((randint(0, y), 0.5))
    return parts

def Victory_ScramblePlayer() -> SampleSet:
    return [(x * 3, 2) for x in range(1, 650)]

def Victory_Epilogue() -> SampleSet:
    return [(x * 45, 3) for x in range(1, 30)]

def Level_Wipe() -> SampleSet:
    return [(x * 45, 3) for x in range(1, 30)]

def Enter_Level() -> SampleSet:
    return [(x // 2, 1) for x in range(1, 600)]

def Whip_Power() -> SampleSet:
    parts = []
    for x in range(3, 35):
        for y in range(45, 52):
            parts.append((x * y, 7))
            parts.append((None, 15))
    return parts

def Bomb_Detonate() -> SampleSet:
    parts = []
    for i in range(5000, 20, -1): # 8230 for FastPC
        parts.append((randint(0, i), 0.3))
        parts.append((30, 8))
    return parts

def Pit_Falling() -> SampleSet:
    parts = []
    x = 3000
    for i in range(1, 16):
        for _ in range(2, 24):
            x = x - 8
            parts.append((x, 53 - 3 * i))
    return parts

def Tunnelling(duration_ms: float) -> SampleSet:
    sample_ms = 0.2
    return [(randint(0, 3000) + 100, sample_ms) for _ in range(0, duration_ms // sample_ms)]

def Tunnel_Exit() -> SampleSet:
    return [(randint(0, 1000), 0.2) for _ in range(1, 400)] # 2100 on FastPC

def Load() -> SampleSet:
    return [(x // 2, 0.3) for x in range(1, 600)]

def Teleport_Windup(windup_ms: float) -> SampleSet:
    return [(20, windup_ms)]

def NewGame() -> SampleSet:
    return [(x // 2, 0.3) for x in range(1, 800)]