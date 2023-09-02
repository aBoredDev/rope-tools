#!/usr/bin/env python3
from math import pi
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities


class GrogSling:
    title = "Grog sling"
    rope_type = utilities.RopeType.HOLLOW_BRAID
    
    rope_diameter_message = "Enter the diameter of rope you are using"
    
    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length required to create a grog sling of a given
        size in a particular diameter of rope.

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.session = session
        self.style = style
    
    def calculate(self, rope_diameter: float, sling_radius: float) -> tuple[float]:
        """Calculates the lengths required to create the grog sling. Uses a tail length
        of 30 rope diameters (+3 to account for the locking part).

        Args:
            rope_diameter (float): The diameter of rope being used.
            sling_radius (float): The desired radius of the finished sling.

        Returns:
            tuple[float]: (total_length, sling_circumference, tail_length) The various
                lengths needed to create the grog sling. 
        """
        sling_circumference = 2 * pi * sling_radius
        tail_length = rope_diameter * 30
        
        total_length = tail_length * 2 + sling_circumference
        
        return total_length, sling_circumference, tail_length

    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message).run())
        sling_radius = utilities.radius_or_diameter_text(self.session, "sling")
    
        # === Run calculations ===
        total_length, sling_circumference, tail_length = self.calculate(rope_diameter, sling_radius)
        
        # === Display results ===
        print(f"Results\n================\nTotal length: {utilities.as_mixed_number(total_length)}\nSling circumference: {utilities.as_mixed_number(sling_circumference)}\nTail length: {utilities.as_mixed_number(tail_length)}")
    
    def dialog(self):
        """Collects parameters and prints results with a console GUI."""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() and int() to throw a TypeError
        try:
            rope_diameter = float(input_dialog(
                title=self.title,
                text=self.rope_diameter_message,
                style=self.style
            ).run())
            sling_radius = utilities.radius_or_diameter_dialog(self.style, self.title, "sling")
        except TypeError:
            return
        
        # === Run calculations ===
        total_length, sling_circumference, tail_length = self.calculate(rope_diameter, sling_radius)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"Total length: {utilities.as_mixed_number(total_length)}\nSling circumference: {utilities.as_mixed_number(sling_circumference)}\nTail length: {utilities.as_mixed_number(tail_length)}"
        ).run()
    
    def __str__(self):
        return self.title