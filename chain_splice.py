#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from math import pi
import utilities


class ChainSplice:
    title = "Chain Splice"
    rope_type = 1  # Twisted

    rope_diameter_message = "Enter rope diameter: "
    chain_diameter_message = "Enter chain diameter: "

    def __init__(
        self, session_or_style: utilities.SessionOrStyle, full_screen: bool = False
    ):
        """Class for calculating the length of rope required for an eye splice in twisted rope

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
        rope_diameter = float(self.session.prompt(self.chain_diameter_message))
        chain_radius = float(self.session.prompt(self.chain_diameter_message)) / 2
        bury_count = int(self.session.prompt(self.bury_count_message))

        # === Calculate values ===
        # Length required to go through the chain
        loop_length = 2 * pi * (chain_radius + (rope_diameter / 2))
        # Length required for the bury
        bury_length = rope_diameter * (3 * bury_count)
        total_length = loop_length + bury_length

        # === Display results ===
        print(
            f"Results\n================\nTotal length: {total_length}\nBury length: {bury_length}\nLoop length: {loop_length}"
        )

    def console_gui(self):
        """Collects parameters and runs calculations with a console GUI"""
        # Not yet implemented, just call text_only() so things don't break
        # If we are running in full screen mode, this doesn't get defined on initialization
        self.session = PromptSession()
        self.text_only()

    def calculate(self):
        """Collect parameters and calculate length required for the chain splice,
        selecting the correct method for current mode automatically.
        """
        if self.full_screen:
            self.console_gui()
        else:
            self.text_only

    def __str__(self):
        return self.title
