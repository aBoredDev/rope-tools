#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities
import translate as tr


class TwistedBackSplice:
    # Default value only, will be overridden by constructor with translation value
    title = "Back Splice"
    rope_type = utilities.RopeType.TWISTED
    reference = "ABOK #2813"

    def __init__(
        self, session: PromptSession, style: Style, lang: str = "en"
    ):
        """Class for calculating the length of rope required for a back splice in twisted rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
            lang (str, optional): Language specifer for translations. Defaults to "en".
        """
        self.style = style
        self.session = session
        self.lang = lang
        
        self.title = tr.back_splice[lang]
    
    def calculate(self, rope_diameter: float) -> float:
            """Calculate length required for the back splice.

            Args:
                rope_diameter (float): The rope diameter to calculate for.

            Returns:
                float: The length needed to tie a back splice.
            """
            # === Run calculations ===
            return rope_diameter * 15
    
    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(tr.rope_diameter_message[self.lang]))

        # === Run calculations ===
        length = self.calculate(rope_diameter)

        # === Display results ===
        print(
            f"{tr.results[self.lang]}\n================",
            f"{tr.length[self.lang]}: {utilities.as_mixed_number(length)}",
            sep="\n"
        )

    def dialog(self):
        """Collects parameters and prints results with a console GUI."""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() to throw a TypeError
        try:
            rope_diameter = float(
                input_dialog(
                    title=self.title,
                    text=tr.rope_diameter_message[self.lang],
                    ok_text=tr.ok[self.lang],
                    cancel_text=tr.cancel[self.lang],
                    style=self.style
                ).run()
            )
        except TypeError:
            return

        # === Run calculations ===
        length = self.calculate(rope_diameter)

        # === Show results ===
        message_dialog(
            title=self.title,
            text=f"{tr.length[self.lang]}: {utilities.as_mixed_number(length)}",
            ok_text=tr.ok[self.lang],
            style=self.style
        ).run()

    def __str__(self):
        return self.title
