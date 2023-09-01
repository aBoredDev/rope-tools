#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities


class TwistedBackSplice:
    title = "Back Splice"
    rope_type = utilities.RopeType.TWISTED
    reference = "ABOK #2813"

    rope_diameter_message = "Enter rope diameter: "
    bury_count_message = "Enter number of buries (5 is typical): "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of rope required for a back splice in twisted rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session

    def text(self):
        """Collects parameters and runs calculations in a basic text format"""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Run calculations ===
        length = self.calculate(rope_diameter)

        # === Display results ===
        print(f"Results\n================\nLength: {utilities.as_mixed_number(length)}")

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI"""
        try:
            rope_diameter = float(
                input_dialog(
                    title=self.title, text=self.rope_diameter_message, style=self.style
                ).run()
            )
        except TypeError:
            return

        # === Run calculations ===
        length = self.calculate(rope_diameter)

        # === Show results ===
        message_dialog(
            title="Results",
            text=f"Length: {utilities.as_mixed_number(length)}",
            style=self.style
        ).run()

    def calculate(self, rope_diameter: float) -> float:
        """Calculate length required for the back splice."""
        # === Run calculations ===
        return rope_diameter * 15

    def __str__(self):
        return self.title
