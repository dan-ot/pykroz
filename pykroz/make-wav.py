from functools import reduce
from typing import List, Tuple, cast
from numpy import linspace, pi as nppi, sin as npsin, recarray, array, int8
from pathlib import Path
import wave


BITRATE = 88200 # per ms, not per second

def sine(frequency = 440.0, duration = 1.0) -> bytes:
    points = int(BITRATE * duration)
    times = cast(recarray, linspace(0, duration, points, endpoint=False))
    x = times * frequency * 2 * nppi
    s = npsin(x) + 1.0
    m = s * 127.5
    a = array(m, dtype = int8)
    data = cast(recarray, a)
    return data.tobytes()

def wav(filename: str, instructions: List[Tuple[float, float]]):
    frames = bytes(reduce(
        lambda soFar, current: [*soFar, *sine(*current)],
        instructions,
        []
    ))
    Path(filename).touch()
    with open(filename, 'wb') as f:
        with wave.open(f) as file:
            wfile = cast(wave.Wave_write, file)
            wfile.setframerate(BITRATE)
            wfile.setnchannels(1)
            wfile.setsampwidth(1)
            wfile.writeframes(frames)

wav('pykroz/sound/title-prompt.wav', [(200, 0.1)])
wav('pykroz/sound/resume-game.wav', [(500, 0.1), *[(f, 1/30) for f in range(200, 100, -1)], (100, 0.1)])