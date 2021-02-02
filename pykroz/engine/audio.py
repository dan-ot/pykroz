from collections import deque
from typing import Sequence, Tuple, Union, cast
import wave

import numpy
import pygame.sndarray
from pygame.mixer import Sound, find_channel

Sample = Tuple[Union[None, int], int]
SampleSet = Sequence[Tuple[Union[None, int], int]]

class Audio:
    def __init__(self, sample_rate: float, bit_depth: int):
        self.sample_rate = sample_rate
        if bit_depth > 0:
            self.type = 'uint{0}'.format(bit_depth)
        else:
            self.type = 'int{0}'.format(abs(bit_depth))
        self.channel = find_channel(False)
        self.queue: deque[Sound] = deque()
        self.volume = (2 ** (abs(bit_depth) - 1)) * 0.8

    def square_wave(self, sample: Sample) -> Sequence[int]:
        (freq, duration_in_ms) = sample
        duration_in_samples = int(self.sample_rate / 1000.0 * duration_in_ms)

        if freq is not None:
            # bits = [(2 * (2 * int(freq * t) - int(2 * freq * t)) + 1) * self.volume for t in range(0, duration_in_samples)]
            bits = [int(numpy.sign(numpy.sin(2 * numpy.pi * (t / self.sample_rate) * freq)) * self.volume) for t in range(duration_in_samples)]
            # bits = [-1 ** (int(2 * freq * (t / duration_in_ms))) * self.volume for t in range(duration_in_samples)]
        else:
            bits = [0 for _ in range(duration_in_samples)]
        return bits

    def sine_wave(self, sample: Sample) -> Sequence[int]:
        (freq, duration_in_ms) = sample
        duration_in_samples = int(self.sample_rate / 1000.0 * duration_in_ms)

        if freq is not None:
            bits = [int(numpy.sin(2.0 * numpy.pi * (t / self.sample_rate) * freq) * self.volume) for t in range(duration_in_samples)]
        else:
            bits = [0 for _ in range(duration_in_samples)]
        return bits

    def wave_to_sound(self, sample: Sequence[int], stereo: bool = True) -> Sound:
        in_stereo = list(map(lambda i: (i, i), sample)) if stereo else sample
        np = numpy.array(in_stereo, dtype=self.type)
        return pygame.sndarray.make_sound(np)

    def tone(self, freq: Union[int, None], duration_in_ms: float, wave_func) -> Sound:
        wav = wave_func((freq, duration_in_ms))
        return self.wave_to_sound(wav)

    def compose(self, commands: SampleSet, wave_func) -> Sound:
        blocks = map(wave_func, commands)
        single = []
        for block in blocks:
            single.extend(block)
        return self.wave_to_sound(single)

    def sound(self, sound: Sound):
        self.queue.append(sound)

    def sound_out(self, filename: str, sound: Sound):
        with wave.open(filename, 'wb') as f:
            file: wave.Wave_write = cast(wave.Wave_write, f)
            file.setframerate(self.sample_rate)
            file.setnchannels(1)
            file.setsampwidth(1 if self.type.endswith('8') else 2)
            file.writeframesraw(sound.get_raw())

    def tick(self):
        if not self.channel.get_busy():
            if len(self.queue) > 0:
                sound = cast(Sound, self.queue.popleft())
                print('Playing {0} seconds'.format(sound.get_length()))
                self.channel.play(sound)
                sound.play()
