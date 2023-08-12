#!/usr/bin/env python3
from prompt_toolkit import PromptSession
import utilities


class FidLength:
    title = "Fid Length"
    rope_type = 0  # General

    rope_diameter_message = "Enter rope diameter: "

    def __init__(
        self, session_or_style: utilities.SessionOrStyle, full_screen: bool = False
    ):
        """Class for calculating the length of a fid for a particualar rope diameter.

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

    def text_only(self):
        """Collects parameters and runs calculations in a basic text format"""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Calculations ===
        length = rope_diameter * 21

        print(f"Results\n================\nFid length: {length: .4f}")

    def console_gui(self):
        """Collects parameters and runs calculations with a console GUI"""
        # Not yet implemented, just call text_only() so things don't break
        # If we are running in full screen mode, this doesn't get defined on initialization
        self.session = PromptSession()
        self.text_only()

    def calculate(self):
        """Collect parameters and calculate length of a fid,
        selecting the correct method for current mode automatically.
        """
        if self.full_screen:
            self.console_gui()
        else:
            self.text_only()
