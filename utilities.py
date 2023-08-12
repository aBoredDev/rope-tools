#!/usr/bin/env python3
from typing import TypeAlias, Union
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from enum import Enum


SessionOrStyle: TypeAlias = Union[PromptSession, Style]

class RopeType(Enum):
    GENERAL = 0
    TWISTED = 1
    HOLLOW_BRAID = 2

class LengthCalculator:
    def __init__(self, session_or_style: SessionOrStyle, full_screen: bool = False):
        """Class for calculating the length of rope required for something in a particular type of rope

        Args:
            session_or_style (SessionOrStyle): PromptSession or Style object, ensures consistent formatting.
            full_screen (bool, optional): Whether or not to use dialogs. Defaults to False.
        """
        self.full_screen = full_screen
        if full_screen:
            self.session = None
            self.style = session_or_style
        else:
            self.session = session_or_style
            self.style = None
    
    def calculate(self):
        """Collect parameters and calculate length required for the operation,
        selecting the correct method for current mode automatically.
        """
        if self.full_screen:
            self.console_gui()
        else:
            self.text_only()
