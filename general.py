#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities


class FidLength:
    title = "Fid Length"
    rope_type = utilities.RopeType.GENERAL

    rope_diameter_message = "Enter rope diameter: "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of a fid for a particular diameter of rope.

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session
    
    def calculate(self, rope_diameter: float) -> tuple[float]:
        """Collect parameters and calculate length of a fid,
        selecting the correct method for current mode automatically.
        """
        if rope_diameter <= 0.5:
            short_length = 0.375
        elif 0.5 < rope_diameter <= 0.75:
            short_length = 0.3
        else:
            short_length = 0.25
        
        full_length = rope_diameter * 21
        short_section = full_length * short_length
        
        return full_length, short_section

    def text(self):
        """Collects parameters and runs calculations in a basic text format"""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Calculations ===
        full_length, short_section = self.calculate(rope_diameter)

        print(f"Results\n================\nFid length: {utilities.as_mixed_number(full_length)}\nShort section: {utilities.as_mixed_number(short_section)}")

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI"""
        # === Collect parameters ===
        try:
            rope_diameter = float(input_dialog(title=self.title, text=self.rope_diameter_message, style=self.style).run())
        except TypeError:
            return
        
        # === Run calculations ===
        full_length, short_section = self.calculate(rope_diameter)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"Fid length: {utilities.as_mixed_number(full_length)}\nShort section: {utilities.as_mixed_number(short_section)}",
            style=self.style
        ).run()
    
    def __str__(self):
        return self.title
