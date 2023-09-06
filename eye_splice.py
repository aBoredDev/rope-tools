#!/usr/bin/env python3
from math import sin, acos, pi
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities
import translate as tr


class TwistedEyeSplice:
    # Default value only, will be overridden by constructor with translation value
    title = "Eye Splice"
    rope_type = utilities.RopeType.TWISTED
    reference = "ABOK #2725"

    def __init__(
        self, session: PromptSession, style: Style, lang: str = "en"
    ):
        """Class for calculating the length of rope required for an eye splice in
        twisted rope.

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
            lang (str, optional): Language specifer for translations. Defaults to "en".
        """
        self.style = style
        self.session = session
        self.lang = lang
        
        self.title = tr.eye_splice[lang]

    def calculate(self, eye_radius: float, rope_diameter: float, tuck_count: int) -> tuple[float]:
        """Calculates the length required to create the desired eye.

        Args:
            eye_radius (float): The desired eye radius.
            rope_diameter (float): The diameter of the rope being used.
            tuck_count (int): The desired number of 'tucks'.

        Returns:
            tuple[float]: (full_length, eye_length, tuck_length, lost_length) The
                various lengths needed to create the eye.
        """
        # Correction to account for rope size
        eye_radius += rope_diameter / 2
        # Angle between rope axis and the end of the tangent section (90°-alpha)
        beta = acos(eye_radius / (eye_radius * 3))
        # Angle between 180° and tangent section
        alpha = (pi / 2) - beta

        # Arc length of the eye
        A = ((alpha + pi) / (2 * pi)) * (2 * pi * eye_radius)
        # Length of the tangent section
        B = sin(beta) / (eye_radius * 3)

        # Total length of the eye
        eye_length = A + 2 * B
        # Length required for the tucks
        tuck_length = rope_diameter * (3 * tuck_count)
        # Full length required for the splice (eye + 1 tuck length)
        full_length = eye_length + tuck_length
        # Approximate length lost to the splice
        lost_length = full_length - eye_radius * 4

        return full_length, eye_length, tuck_length, lost_length

    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        # Eye radius/diameter
        eye_radius = utilities.radius_or_diameter_text(self.session, tr.eye[self.lang])

        # Rope diameter
        rope_diameter = float(self.session.prompt(tr.rope_diameter_message[self.lang]))

        # No. of tucks
        tuck_count = int(self.session.prompt(tr.tuck_count_message[self.lang]))

        # === Run calculations ===
        full_length, eye_length, tuck_length, lost_length = self.calculate(
            eye_radius, rope_diameter, tuck_count
        )

        # Print to screen
        print(
            f"{tr.results[self.lang]}\n================",
            f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(full_length)}",
            f"{tr.eye_length[self.lang]}: {utilities.as_mixed_number(eye_length)}",
            f"{tr.tuck_length[self.lang]}: {utilities.as_mixed_number(tuck_length)}",
            f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            sep="\n"
        )

    def dialog(self):
        """Collects parameters and prints results with a console GUI"""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() and int() to throw a TypeError
        try:
            eye_radius = utilities.radius_or_diameter_dialog(self.style, self.title, "eye")
            rope_diameter = float(input_dialog(
                title=self.title,
                text=tr.rope_diameter_message[self.lang],
                style=self.style
            ).run())
            tuck_count = int(input_dialog(
                title=self.title,
                text=tr.tuck_count_message[self.lang],
                style=self.style
            ).run())
        except TypeError:
            return

        # === Run calculations ===
        total_length, eye_length, tuck_length, lost_length = self.calculate(
            eye_radius, rope_diameter, tuck_count
        )

        # === Show results ===
        message_dialog(
            title=tr.results[self.lang],
            text=f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}\n" +
                 f"{tr.eye_length[self.lang]}: {utilities.as_mixed_number(eye_length)}\n" +
                 f"{tr.tuck_length[self.lang]}: {utilities.as_mixed_number(tuck_length)}\n" +
                 f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            ok_text=tr.ok[self.lang],
            style=self.style
        ).run()

    def __str__(self):
        return self.title


class HollowBraidLockedEyeSplice:
    # Default value only, will be overridden by constructor with translation value
    title = "Locked Brummel Eye Splice"
    rope_type = utilities.RopeType.HOLLOW_BRAID

    def __init__(
        self, session: PromptSession, style: Style, lang: str = "en"
    ):
        """Class for calculating the length of rope required for an eye splice in hollow braid rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
            lang (str, optional): Language specifer for translations. Defaults to "en".
        """
        self.style = style
        self.session = session
        self.lang = lang
        
        # Get the translated title
        self.title = tr.locked_eye_splice[self.lang]

    def calculate(self, eye_radius: float, rope_diameter: float) -> tuple[float]:
        """Calculate length required for the eye splice.

        Args:
            eye_radius (float): The desired radius of the eye.
            rope_diameter (float): The diameter of the rope.

        Returns:
            tuple[float]: (full_length, eye_length, bury_length, lost_length) The
                various lengths needed to create the eye splice. 
        """
        # === Run calculations ===
        # Correction to account for rope diameter
        eye_radius += rope_diameter / 2
        # Angle between rope axis and end of tangent section (90°-alpha)
        beta = acos(eye_radius / (eye_radius * 3))
        # Angle between 180° and tangent section
        alpha = (pi / 2) - beta
        # Arc length of eye
        A = ((alpha + pi) / (2 * pi)) * (2 * pi * eye_radius)
        # Length of the tangent section
        B = sin(beta) / (eye_radius * 3)

        # Total length of the eye
        eye_length = A + 2 * B + rope_diameter * 3
        # Length required for the bury
        bury_length = rope_diameter * 72
        # Full length required for the splice (eye + 1 bury length)
        full_length = eye_length + bury_length
        # Approximate length lost to the splice
        lost_length = full_length - eye_radius * 4

        return full_length, eye_length, bury_length, lost_length

    def text(self):
        """Collects parameters and prints results in text only mode."""
        # === Collect parameters ===
        # Eye radius/diameter
        eye_radius = utilities.radius_or_diameter_text(
            self.session,
            tr.eye[self.lang],
            self.lang
        )

        # Rope diameter
        rope_diameter = float(self.session.prompt(tr.rope_diameter_message[self.lang]))

        # === Run calculations ===
        total_length, eye_length, bury_length, lost_length = self.calculate(
            eye_radius, rope_diameter
        )

        # Print to screen
        print(
            f"{tr.results[self.lang]}\n================",
            f"{tr.full_length[self.lang]}: {utilities.as_mixed_number(total_length)}",
            f"{tr.eye_length[self.lang]}: {utilities.as_mixed_number(eye_length)}",
			f"{tr.bury_length[self.lang]}: {utilities.as_mixed_number(bury_length)}",
			f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            sep="\n"
        )

    def dialog(self):
        """Collects parameters and prints results in dialog mode."""
        # === Collect parameter ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() to throw a TypeError
        try:
            eye_radius = utilities.radius_or_diameter_dialog(
                self.style, 
                self.title,
                tr.eye[self.lang],
                self.lang
            )

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
        total_length, eye_length, bury_length, lost_length = self.calculate(
            eye_radius, rope_diameter
        )

        # === Show results ===
        message_dialog(
            title=tr.results[self.lang],
            text=f"{tr.total_length[self.lang]}: {utilities.as_mixed_number(total_length)}\n" +
                 f"{tr.eye_length[self.lang]}: {utilities.as_mixed_number(eye_length)}\n" +
                 f"{tr.bury_length[self.lang]}: {utilities.as_mixed_number(bury_length)}\n" +
                 f"{tr.lost_length[self.lang]}: {utilities.as_mixed_number(lost_length)}",
            ok_text=tr.ok[self.lang],
            style=self.style
        ).run()

    def __str__(self):
        return self.title
