#!/usr/bin/env python3
from math import sin, acos, pi
from prompt_toolkit import PromptSession
import utilities


class TwistedEyeSplice:
    title = 'Eye Splice'
    rope_type = 1 # Twisted
    reference = 'ABOK #2725'
    
    eye_radius_message = 'Enter desired eye radius or d to use diameter: '
    eye_diameter_message = 'Enter desired eye diameter: '
    rope_diameter_message = 'Enter rope diameter: '
    bury_count_message = 'Enter number of buries (5 is typical): '
    
    def __init__(self, session_or_style: utilities.SessionOrStyle, full_screen: bool = False):
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
        """Collects parameters and runs calculations in a basic text format
        """
        # === Collect parameters ===
        # Eye radius/diameter
        raw_eye_radius: str = self.session.prompt(self.eye_radius_message)
        if raw_eye_radius.lower() == 'd':
            raw_eye_diameter = self.session.prompt(self.eye_diameter_message)
            eye_radius = float(raw_eye_diameter) / 2
        else:
            eye_radius = float(raw_eye_radius)
        
        # Rope diameter
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # No. of buries
        bury_count = int(self.session.prompt(self.bury_count_message))

        # === Run calculations ===
        beta = acos(eye_radius/(eye_radius*3))
        alpha = (pi/2) - beta

        A = ((alpha + pi)/(2*pi))*(2*pi * eye_radius)
        B = sin(beta)/(eye_radius*3)

        eye_length = A + 2*B  # Total length of the eye
        bury_length = rope_diameter*(3*bury_count)  # Length required for the bury
        full_length = eye_length + bury_length  # Full length required for the splice (eye + 1 bury length)
        lost_length = full_length - eye_radius*4  # Approximate length lost to the splice

        # Print to screen
        print(f'Results\n================\nFull length: {full_length: .4f}\nEye length: {eye_length: .4f}\nBury length: {bury_length: .4f}\nEst. length lost: {lost_length}')
    
    def console_gui(self):
        """Collects parameters and runs calculations with a console GUI
        """
        # Not yet implemented, just call text_only() so things don't break
        self.session = PromptSession() # If we are running in full screen mode, this doesn't get defined on initialization
        self.text_only()
        

    def calculate(self):
        """Collect parameters and calculate length required for the eye splice,
        selecting the correct method for current mode automatically.
        """
        if self.full_screen:
            self.console_gui()
        else:
            self.text_only()


class HollowBraidLockedEyeSplice:
    title = 'Locked Brummel Eye Splice'
    rope_type = 2 # Hollow
    
    eye_radius_message = 'Enter desired eye radius or d to use diameter: '
    eye_diameter_message = 'Enter desired eye diameter: '
    rope_diameter_message = 'Enter rope diameter: '
    
    def __init__(self, session_or_style: utilities.SessionOrStyle, full_screen: bool = False):
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
        """Collects parameters and runs calculations in a basic text format
        """
        # === Collect parameters ===
        # Eye radius/diameter
        raw_eye_radius: str = self.session.prompt(self.eye_radius_message)
        if raw_eye_radius.lower() == 'd':
            raw_eye_diameter = self.session.prompt(self.eye_diameter_message)
            eye_radius = float(raw_eye_diameter) / 2
        else:
            eye_radius = float(raw_eye_radius)
        
        # Rope diameter
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Run calculations ===
        beta = acos(eye_radius/(eye_radius*3))  # Angle between rope axis and end of tangent section (90°-alpha)
        alpha = (pi/2) - beta  # Angle between 180° and tangent section
        A = ((alpha + pi)/(2*pi))*(2*pi * eye_radius)  # Arc length of eye
        B = sin(beta)/(eye_radius*3)  # Length of the tangent section

        eye_length = A + 2*B + rope_diameter*3  # Total length of the eye
        bury_length = rope_diameter*72  # Length required for the bury
        full_length = eye_length + bury_length  # Full length required for the splice (eye + 1 bury length)
        lost_length = full_length - eye_radius*4  # Approximate length lost to the splice

        # Print to screen
        print(f'Results\n================\nFull length: {full_length: .4f}\nEye length: {eye_length: .4f}\nBury length: {bury_length: .4f}\nEst. length lost: {lost_length}')
    
    def console_gui(self):
        """Collects parameters and runs calculations with a console GUI
        """
        # Not yet implemented, just call text_only() so things don't break
        self.session = PromptSession() # If we are running in full screen mode, this doesn't get defined on initialization
        self.text_only()
        

    def calculate(self):
        """Collect parameters and calculate length required for the eye splice,
        selecting the correct method for current mode automatically.
        """
        if self.full_screen:
            self.console_gui()
        else:
            self.text_only()
