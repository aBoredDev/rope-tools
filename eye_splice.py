#!/usr/bin/env python3
from math import sin, acos, pi
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities


class TwistedEyeSplice:
    title = "Eye Splice"
    rope_type = utilities.RopeType.TWISTED
    reference = "ABOK #2725"

    rope_diameter_message = "Enter rope diameter: "
    tuck_count_message = "Enter number of 'tucks' (5 is typical): "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of rope required for an eye splice in twisted rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session

    def calculate(self, eye_radius: float, rope_diameter: float, tuck_count: int) -> tuple[float]:
        """Run calculation with collected parameters"""
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
        """Collects parameters and runs calculations in a basic text format"""
        # === Collect parameters ===
        # Eye radius/diameter
        eye_radius = utilities.radius_or_diameter_text(self.session, "eye")

        # Rope diameter
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # No. of tucks
        tuck_count = int(self.session.prompt(self.tuck_count_message))

        # === Run calculations ===
        full_length, eye_length, tuck_length, lost_length = self.calculate(
            eye_radius, rope_diameter, tuck_count
        )

        # Print to screen
        print(
            f"Results\n================\nFull length: {utilities.as_mixed_number(full_length)}\nEye length: {utilities.as_mixed_number(eye_length)}\nTuck length: {utilities.as_mixed_number(tuck_length)}\nEst. length lost: {utilities.as_mixed_number(lost_length)}"
        )

    def dialog(self):
        """Collects parameters and runs calculations with a console GUI"""
        # === Collect parameters ===
        try:
            eye_radius = utilities.radius_or_diameter_dialog(self.style, self.title, "eye")

            rope_diameter = float(input_dialog(title=self.title, text=self.rope_diameter_message, style=self.style).run())

            tuck_count = int(input_dialog(title=self.title, text=self.tuck_count_message, style=self.style).run())
        except TypeError:
            return

        # === Run calculations ===
        full_length, eye_length, tuck_length, lost_length = self.calculate(
            eye_radius, rope_diameter, tuck_count
        )

        # === Show results ===
        message_dialog(
            title="Results",
            text=f"Full length: {utilities.as_mixed_number(full_length)}\nEye length: {utilities.as_mixed_number(eye_length)}\nTuck length: {utilities.as_mixed_number(tuck_length)}\nEst. length lost: {utilities.as_mixed_number(lost_length)}",
        ).run()

    def __str__(self):
        return self.title


class HollowBraidLockedEyeSplice:
    title = "Locked Brummel Eye Splice"
    rope_type = utilities.RopeType.HOLLOW_BRAID

    rope_diameter_message = "Enter rope diameter: "

    def __init__(
        self, session: PromptSession, style: Style
    ):
        """Class for calculating the length of rope required for an eye splice in hollow braid rope

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session

    def calculate(self, eye_radius: float, rope_diameter: float) -> tuple[float]:
        """Calculate length required for the eye splice."""
        # === Run calculations ===
        # Correction to accout for rope diameter
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
        """Collects parameters and prints results in text only mode"""
        # === Collect parameters ===
        # Eye radius/diameter
        eye_radius = utilities.radius_or_diameter_text(self.session, "eye")

        # Rope diameter
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Run calculations ===
        full_length, eye_length, bury_length, lost_length = self.calculate(
            eye_radius, rope_diameter
        )

        # Print to screen
        print(
            f"Results\n================\nFull length: {utilities.as_mixed_number(full_length)}\nEye length: {utilities.as_mixed_number(eye_length)}\nBury length: {utilities.as_mixed_number(bury_length)}\nEst. length lost: {utilities.as_mixed_number(lost_length)}"
        )

    def dialog(self):
        """Collects parameters and prints results in dialog mode"""
        try:
            eye_radius = utilities.radius_or_diameter_dialog(self.style, self.title, "eye")

            rope_diameter = float(
                input_dialog(
                    title="Rope diameter", text=self.rope_diameter_message
                ).run()
            )
        except TypeError:
            return

        # === Run calculations ===
        full_length, eye_length, bury_length, lost_length = self.calculate(
            eye_radius, rope_diameter
        )

        # === Show results ===
        message_dialog(
            title="Results",
            text=f"Full length: {utilities.as_mixed_number(full_length)}\nEye length: {utilities.as_mixed_number(eye_length)}\nBury length: {utilities.as_mixed_number(bury_length)}\nEst. length lost: {utilities.as_mixed_number(lost_length)}",
        ).run()

    def __str__(self):
        return self.title
