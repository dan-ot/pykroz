from typing import Protocol
from pygame import Surface
from commands import Command

class TickableState(Protocol):
    def tick(self, deltaTime: float) -> 'TickableState':
        ...

    def render(self, surface: Surface) -> None:
        ...

class CommandableState(TickableState, Protocol):
    def tick(self, deltaTime: float) -> 'CommandableState':
        ...

    def command(self, command: Command) -> None:
        ...
