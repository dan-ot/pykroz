from typing import Callable, MutableMapping, Optional
from pygame import Rect, Surface

from states.protocols import CommandableState
from commands import Command
from engine.ascii import ASCII

class Page():
    def __init__(self, content: Surface, report_selection: Callable[[Command], None]):
        self.content = content
        self.report_selection = report_selection

class PageSet():
    def __init__(self, pages: list[Page], parent: Optional['PageSet'] = None, data: MutableMapping[str, Command] = {}, current_page: int = 0):
        self.parent = parent
        self.data = data
        self.pages = pages
        self.current_page = current_page

class MenuState():
    def __init__(self, initialState, font: ASCII, size: Rect):
        self.state = initialState


    def tick(self, deltaTime: float) -> CommandableState:
        return self #.state.tick(deltaTime)

    def render(self, surface: Surface) -> None:
        pass
        #self.state.render(surface)

    def command(self, command: Command):
        pass
