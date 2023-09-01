#!/usr/bin/env python3
from typing import TypeAlias, Union
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog
from enum import Enum
import re
import math


SessionOrStyle: TypeAlias = Union[PromptSession, Style]


def select_from_list(
    session: PromptSession, start_message: str, options: list, oops_option: str
) -> int:
    options_list = "".join(
        [f"\n  {i}) {options[i]}" for i in range(len(options))] + [f"\n  {len(options)}) {oops_option}"]
    )
    full_message = start_message + options_list + "\n\n> "
    while True:
        try:
            answer = int(session.prompt(full_message))
            if answer > len(options):
                print(
                    f"'{answer}' is not a valid option. Please try again or select the '{oops_option}' option.\n"
                )
                continue
            return answer
        except ValueError as e:
            value = re.search(r"'(.*)'$", str(e))
            print(
                f"'{value.group(1)}' is not a valid option. Please try again or select the '{oops_option}' option.\n"
            )


def radius_or_diameter_text(session: PromptSession, item_name: str) -> float:
    raw_radius: str = session.prompt(f"Enter {item_name} radius or d to use diameter: ")
    if raw_radius in ["d", "D"]:
        raw_diameter = session.prompt(f"Enter {item_name} diameter: ")
        return float(raw_diameter) / 2
    else:
        return float(raw_radius)


def radius_or_diameter_dialog(style: Style, title: str, item_name: str) -> float:
    raw_radius = input_dialog(
        title=title,
        text=f"Enter {item_name} radius or d to use diameter",
        style=style
    ).run()
    if raw_radius in ["d", "D"]:
        raw_diameter = input_dialog(
            title=title,
            text=f"Enter {item_name} diameter",
            style=style
        ).run()
        return float(raw_diameter) / 2
    else:
        return float(raw_radius)

def round_to_sixteenths(value: float) -> float:
    remainder = value % 0.0625
    return value - remainder

def as_mixed_number(value: float) -> str:
    rounded_value = round_to_sixteenths(value)
    
    fractional_part = (rounded_value % 1) * 16
    integral_part = int(rounded_value)
    
    halves = 1
    while fractional_part:
        if fractional_part % 2:
            break
        fractional_part /= 2
        halves *= 2
    
    if not fractional_part:
        return str(integral_part)
    else:
        return f"{integral_part}+{int(fractional_part)}/{int(16/halves)}"


class RopeType(Enum):
    GENERAL = 0
    TWISTED = 1
    HOLLOW_BRAID = 2

    def __str__(self):
        return self.name.capitalize().replace("_", " ")


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

    def __str__(self):
        return self.title
