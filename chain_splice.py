#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
from math import pi
import utilities


class TwistedChainSplice:
    title = "Chain Splice"
    rope_type = utilities.RopeType.TWISTED

    rope_diameter_message = "Enter rope diameter: "
    chain_diameter_message = "Enter chain diameter: "
    tuck_count_message = "Enter desired number of 'tucks' (5 is typical): "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of rope required for a chain splice in twisted rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session

    def text(self):
        """Collects parameters and prints results in a basic text format"""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))
        chain_radius = float(self.session.prompt(self.chain_diameter_message)) / 2
        tuck_count = int(self.session.prompt(self.tuck_count_message))

        total_length, tuck_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter, tuck_count)

        # === Display results ===
        print(
            f"Results\n================\nTotal length: {utilities.as_mixed_number(total_length)}\ntuck length: {utilities.as_mixed_number(tuck_length)}\nLoop length: {utilities.as_mixed_number(loop_length)}\nLost length: {utilities.as_mixed_number(lost_length)}"
        )

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI"""
        # === Collect parameters ===
        try:
            rope_diameter = float(input_dialog(title=self.title, text=self.rope_diameter_message, style=self.style).run())
            chain_radius = float(input_dialog(title=self.title, text=self.chain_diameter_message, style=self.style).run())
            tuck_count = int(input_dialog(title=self.title, text=self.tuck_count_message, style=self.style).run())
        except TypeError:
            return
        
        # === Run calculations ===
        total_length, tuck_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter, tuck_count)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"Total length: {utilities.as_mixed_number(total_length)}\ntuck length: {utilities.as_mixed_number(tuck_length)}\nLoop length: {utilities.as_mixed_number(loop_length)}\nLost length: {utilities.as_mixed_number(lost_length)}",
            style=self.style
        ).run()

    def calculate(self, chain_radius: float, rope_diameter: float, tuck_count: int) -> tuple[float]:
        """Calculate length required for the chain splice."""
        # Length required to go through the chain
        loop_length = 2 * pi * (chain_radius + (rope_diameter / 2))
        # Length required for the tucks
        tuck_length = rope_diameter * (3 * tuck_count)
        total_length = loop_length + tuck_length
        lost_length = total_length - chain_radius * 4

        return total_length, tuck_length, loop_length, lost_length

    def __str__(self):
        return self.title

class HollowBraidChainSplice:
    title = "Chain Splice"
    rope_type = utilities.RopeType.HOLLOW_BRAID

    rope_diameter_message = "Enter rope diameter: "
    chain_diameter_message = "Enter chain diameter: "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of rope required for a chain splice in hollow braid rope
        (Essentially just a locked brummel with the correct size eye)

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session
    
    def calculate(self, chain_radius: float, rope_diameter: float) -> tuple[float]:
        """Calculate length required for the chain splice."""
        # Length required to go through the chain
        loop_length = 2 * pi * (chain_radius + (rope_diameter / 2)) + (rope_diameter * 3)
        # Length required for the bury
        bury_length = rope_diameter * 72
        total_length = loop_length + bury_length
        lost_length = total_length - chain_radius * 4

        return total_length, bury_length, loop_length, lost_length

    def text(self):
        """Collects parameters and prints results in a basic text format"""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))
        chain_radius = float(self.session.prompt(self.chain_diameter_message)) / 2

        total_length, bury_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter)

        # === Display results ===
        print(
            f"Results\n================\nTotal length: {utilities.as_mixed_number(total_length)}\nBury length: {utilities.as_mixed_number(bury_length)}\nLoop length: {utilities.as_mixed_number(loop_length)}\nLost length: {utilities.as_mixed_number(lost_length)}"
        )

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI"""
        # === Collect parameters ===
        try:
            rope_diameter = float(input_dialog(title=self.title, text=self.rope_diameter_message, style=self.style).run())
            chain_radius = float(input_dialog(title=self.title, text=self.chain_diameter_message, style=self.style).run())
        except TypeError:
            return
        
        # === Run calculations ===
        total_length, bury_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"Total length: {utilities.as_mixed_number(total_length)}\nBury length: {utilities.as_mixed_number(bury_length)}\nLoop length: {utilities.as_mixed_number(loop_length)}\nLost length: {utilities.as_mixed_number(lost_length)}",
            style=self.style
        ).run()

    def __str__(self):
        return self.title
