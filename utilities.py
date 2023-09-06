#!/usr/bin/env python3
from typing import TypeAlias, Union
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog
from enum import Enum
import translate as tr
import re


# NOTE: DEPRECATED - Changed classes to accept both the session and style separately, instead
# of taking one or the other.
SessionOrStyle: TypeAlias = Union[PromptSession, Style]


def select_from_list(
    session: PromptSession, start_message: str, options: list[str], oops_option: str, lang: str = "en"
) -> int:
    """Utility function that prompts the user to select an item from a list and returns
    the index of the item they selected. Essentially a text-only companion to
    'radiolist_dialog'.

    Args:
        session (PromptSession): The current PromptSession.
        start_message (str): The inital message that usually contains the question.
        options (list[str]): The list of options.
        oops_option (str): The last option that will be added to the list, typically
            'Back', 'Cancel', or 'Quit'.
        lang (str, optional): The translation language. Defaults to "en".

    Returns:
        int: The index of the item selected. May be in the range of
            [0, length of options list].
    """
    options_list = "".join(
        [f"\n  {i}) {options[i]}" for i in range(len(options))] + [f"\n  {len(options)}) {oops_option}"]
    )
    full_message = start_message + options_list + "\n\n> "
    while True:
        try:
            answer = int(session.prompt(full_message))
            if answer > len(options):
                print(
                    tr.select_from_list_error[lang].format(answer=answer, oops_option=oops_option)
                )
                continue
            return answer
        except ValueError as e:
            value = re.search(r"'(.*)'$", str(e))
            print(
                tr.select_from_list_error[lang].format(answer=value.group(1), oops_option=oops_option)
            )


def radius_or_diameter_text(session: PromptSession, item_name: str, lang: str = "en") -> float:
    """Utility function for getting the radius or diameter of an item, using text only.

    Args:
        session (PromptSession): The current PromptSession.
        item_name (str): The name of the item
        lang (str, optional): The translation language. Defaults to "en".

    Returns:
        float: The radius of the item, because that's usually what we actually want.
    """
    raw_radius: str = session.prompt(tr.radius_or_diameter_message["radius"][lang].format(name=item_name))
    if raw_radius in ["d", "D"]:
        raw_diameter = session.prompt(tr.radius_or_diameter_message["diameter"][lang].format(name=item_name))
        return float(raw_diameter) / 2
    else:
        return float(raw_radius)


def radius_or_diameter_dialog(style: Style, title: str, item_name: str, lang: str = "en") -> float:
    """Utility function for getting the radius or diameter of an item, using console dialogs.

    Args:
        style (Style): The Style object being used, to keep the formatting consistent
        title (str): The title of the dialog
        item_name (str): The name of the item
        lang (str, optional): The translation language. Defaults to "en".

    Returns:
        float: The radius of the item, because that's usually what we actually want.
    """
    raw_radius = input_dialog(
        title=title,
        text=tr.radius_or_diameter_message["radius"][lang].format(name=item_name),
        ok_text=tr.ok[lang],
        cancel_text=tr.cancel[lang],
        style=style
    ).run()
    if raw_radius in ["d", "D"]:
        raw_diameter = input_dialog(
            title=title,
            text=tr.radius_or_diameter_message["diameter"][lang].format(name=item_name),
            ok_text=tr.ok[lang],
            cancel_text=tr.cancel[lang],
            style=style
        ).run()
        return float(raw_diameter) / 2
    else:
        return float(raw_radius)

def round_to_sixteenths(value: float) -> float:
    """Utility function to round a floating point value to the nearest 1/16th. Will
    always round down.

    Args:
        value (float): The floating point value to be rounded.

    Returns:
        float: The rounded value.
    """
    remainder = value % 0.0625
    return value - remainder

def as_mixed_number(value: float) -> str:
    """Utility function to convert a floating point value to a mixed number, rounded to
    the nearest 1/16th.

    Args:
        value (float): The floating point value to be converted

    Returns:
        str: The mixed number form, rounded to the nearest 1/16th.
    """
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
