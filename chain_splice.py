#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
from math import pi
import utilities
import translate as tr


class TwistedChainSplice:
    title = "Chain Splice"
    rope_type = utilities.RopeType.TWISTED

    rope_diameter_message = "Enter rope diameter: "
    chain_diameter_message = "Enter chain diameter: "
    tuck_count_message = "Enter desired number of 'tucks' (5 is typical): "

    def __init__(
        self, session: PromptSession, style: Style, lang: str = "en"
    ):
        """Class for calculating the length of rope required for a chain splice in
        twisted rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
            lang (str, optional): Language specifer for translations. Defaults to "en".
        """
        self.style = style
        self.session = session
        self.lang = lang
        
        self.title = tr.chain_splice[lang]
    
    def calculate(self, chain_radius: float, rope_diameter: float, tuck_count: int) -> tuple[float]:
        """Calculate length required for the chain splice.

        Args:
            chain_radius (float): The radius of the chain link.
            rope_diameter (float): The diameter of the rope.
            tuck_count (int): The number of 'tucks' desired.

        Returns:
            tuple[float]: (total_length, tuck_length, loop_length, lost_length) The
                various lengths needed to create the splice.
        """
        # Length required to go through the chain
        loop_length = 2 * pi * (chain_radius + (rope_diameter / 2))
        # Length required for the tucks
        tuck_length = rope_diameter * (3 * tuck_count)
        total_length = loop_length + tuck_length
        lost_length = total_length - chain_radius * 4

        return total_length, tuck_length, loop_length, lost_length

    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(tr.rope_diameter_message[self.lang]))
        chain_radius = float(self.session.prompt(tr.chain_diameter_message[self.lang])) / 2
        tuck_count = int(self.session.prompt(tr.tuck_count_message[self.lang]))

        total_length, tuck_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter, tuck_count)

        # === Display results ===
        print(
            f"{tr.results[self.lang]}\n================",
            f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}",
            f"{tr.tuck_length[self.lang]}: {utilities.as_mixed_number(tuck_length)}",
            f"{tr.loop_length[self.lang]}: {utilities.as_mixed_number(loop_length)}",
            f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            sep="\n"
        )

    def dialog(self):
        """Collects parameters and prints results with a console GUI."""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() and int() to throw a TypeError
        try:
            rope_diameter = float(input_dialog(
                title=self.title,
                text=tr.rope_diameter_message[self.lang],
                ok_text=tr.ok[self.lang],
                cancel_text=tr.cancel[self.lang],
                style=self.style
            ).run())
            
            chain_radius = float(input_dialog(
                title=self.title,
                text=tr.chain_diameter_message[self.lang],
                ok_text=tr.ok[self.lang],
                cancel_text=tr.cancel[self.lang],
                style=self.style
            ).run())
            
            tuck_count = int(input_dialog(
                title=self.title,
                text=tr.tuck_count_message[self.lang],
                ok_text=tr.ok[self.lang],
                cancel_text=tr.cancel[self.lang],
                style=self.style
            ).run())
        except TypeError:
            return
        
        # === Run calculations ===
        total_length, tuck_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter, tuck_count)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}\n" +
                 f"{tr.tuck_length[self.lang]}: {utilities.as_mixed_number(tuck_length)}\n" +
                 f"{tr.loop_length[self.lang]}: {utilities.as_mixed_number(loop_length)}\n" +
                 f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            ok_text=tr.ok[self.lang],
            style=self.style
        ).run()

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
        """Class for calculating the length of rope required for a chain splice in
        hollow braid rope (Essentially just a locked brummel with the correct size eye)

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session
    
    def calculate(self, chain_radius: float, rope_diameter: float) -> tuple[float]:
        """Calculate length required for the chain splice.

        Args:
            chain_radius (float): The radius of the chain link
            rope_diameter (float): The diameter of the rope

        Returns:
            tuple[float]: (total_length, bury_length, loop_length, lost_length) The
                various lengths needed to create the chain splice.
        """
        # Length required to go through the chain
        loop_length = 2 * pi * (chain_radius + (rope_diameter / 2)) + (rope_diameter * 3)
        # Length required for the bury
        bury_length = rope_diameter * 72
        total_length = loop_length + bury_length
        lost_length = total_length - chain_radius * 4

        return total_length, bury_length, loop_length, lost_length

    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(tr.rope_diameter_message[self.lang]))
        chain_radius = float(self.session.prompt(tr.chain_diameter_message[self.lang])) / 2

        total_length, bury_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter)

        # === Display results ===
        print(
            f"{tr.results[self.lang]}\n================",
            f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}",
            f"{tr.bury_length[self.lang]}: {utilities.as_mixed_number(bury_length)}",
            f"{tr.loop_length[self.lang]}: {utilities.as_mixed_number(loop_length)}",
            f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            sep="\n"
        )

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI."""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() to throw a TypeError
        try:
            rope_diameter = float(input_dialog(
                title=self.title,
                text=tr.rope_diameter_message[self.lang],
                ok_text=tr.ok[self.lang],
                cancel_text=tr.cancel[self.lang],
                style=self.style
            ).run())
            
            chain_radius = float(input_dialog(
                title=self.title,
                text=tr.chain_diameter_message[self.lang],
                ok_text=tr.ok[self.lang],
                cancel_text=tr.cancel[self.lang],
                style=self.style
            ).run())
        except TypeError:
            return
        
        # === Run calculations ===
        total_length, bury_length, loop_length, lost_length = self.calculate(chain_radius, rope_diameter)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}\n" +
                 f"{tr.bury_length[self.lang]}: {utilities.as_mixed_number(bury_length)}\n" +
                 f"{tr.loop_length[self.lang]}: {utilities.as_mixed_number(loop_length)}\n" +
                 f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            ok_text=tr.ok[self.lang],
            style=self.style
        ).run()

    def __str__(self):
        return self.title
