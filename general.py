#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import utilities


class FidLengthCalculate:
    title = "Fid Length Calculator"
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
        """Calculate length of a fid, accouting for rope diameter when calculating the
        short section length, based on the Sampson tubular fid specs.

        Args:
            rope_diameter (float): The diameter of the rope to calculate for.

        Returns:
            tuple[float]: (short_length, half_length, long_length, full_length) The
                various fid lengths.
        """
        if rope_diameter <= 0.5:
            short_percent = 0.375
        elif 0.5 < rope_diameter <= 0.75:
            short_percent = 0.3
        else:
            short_percent = 0.25
        
        full_length = rope_diameter * 21
        short_length = full_length * short_percent
        half_length = rope_diameter * 10.5
        long_length = rope_diameter * 14
        
        return short_length, half_length, long_length, full_length

    def text(self):
        """Collects parameters and prints results in a basic text format."""
        # === Collect parameters ===
        rope_diameter = float(self.session.prompt(self.rope_diameter_message))

        # === Calculations ===
        short_length, half_length, long_length, full_length = self.calculate(rope_diameter)

        print(f"Results\n================\n" +
              f"Short fid: {utilities.as_mixed_number(short_length)}\n" +
              f"Half fid: {utilities.as_mixed_number(half_length)}\n" +
              f"Long fid: {utilities.as_mixed_number(long_length)}\n" +
              f"Full fid: {utilities.as_mixed_number(full_length)}"
              )

    def dialog(self):
        """Collects parameters and prints results with a console GUI."""
        # === Collect parameters ===
        # try/except because when the user hits 'Cancel' on the dialog, it returns None
        # which causes float() to throw a TypeError
        try:
            rope_diameter = float(input_dialog(title=self.title, text=self.rope_diameter_message, style=self.style).run())
        except TypeError:
            return
        
        # === Run calculations ===
        short_length, half_length, long_length, full_length = self.calculate(rope_diameter)
        
        # === Display results ===
        message_dialog(
            title=self.title,
            text=f"Short fid: {utilities.as_mixed_number(short_length)}\n" +
                 f"Half fid: {utilities.as_mixed_number(half_length)}\n" +
                 f"Long fid: {utilities.as_mixed_number(long_length)}\n" +
                 f"Full fid: {utilities.as_mixed_number(full_length)}",
            style=self.style
        ).run()
    
    def __str__(self):
        return self.title

class FidLengthTable:
    title = "Fid Length Table"
    rope_type = utilities.RopeType.GENERAL
    
    fid_table_headers = ("Rope dia. (in)", "Short fid (in)", "Long fid (in)",
                         "Full fid (in)")
    fid_table = (
        ("3/32", "3/4", "1-5/16", "2"),
        ("1/8", "1", "1-3/4", "2-5/8"),
        ("3/16", "1-1/2", "2-5/8", "4"),
        ("1/4", "2", "3-1/2", "5-1/4"),
        ("5/16", "2-1/2", "4-3/8", "6-9/16"),
        ("3/8", "3", "5-1/4", "7-7/8"),
        ("7/16", "3-1/2", "6-1/8", "9-3/16"),
        ("1/2", "4", "7", "10-1/2"),
        ("9-16", "4-1/4", "7-7/8", "12"),
        ("5/8", "4-1/2", "8-3/4", "13-1/8"),
        ("11/16", "4-13/16", "9-5/8", "14-7/16"),
        ("3/4", "4-3/4", "10-1/2", "15-3/4"),
        ("7/8", "4-1/2", "12-1/4", "18-3/8"),
        ("1", "5-1/4", "14", "21"),
        ("1-1/8", "6", "15-3/4", "23-5/8"),
        ("1-1/4", "6-1/2", "17-1/2", "26-1/4"),
        ("1-5/16", "7", "18-3/8", "27-9/16"),
        ("1-1/2", "8", "21", "31-1/2"),
        ("1-5/8", "8-1/2", "22-3/4", "34-1/8"),
        ("1-3/4", "9-1/4", "24-1/2", "36-3/4"),
        ("2", "10-1/2", "28", "42")
    )

    def __init__(self, session: PromptSession, style: Style):
        """Class which displays a table showing pre-calculated fid lengths. Table source:
        https://atlanticbraids.com/fid-lengths/

        Args:
            session (PromptSession): Ensures consistent formatting in text only mode.
            style (Style): Ensures consistent formatting in dialog mode.
        """
        self.style = style
        self.session = session
    
    def build_table(self, rows: int=len(fid_table)) -> list[str]:
        """Builds out the table that will be printed to the screen."""
        # calculate the widths for each column
        col_widths = [len(h) for h in self.fid_table_headers]
        
        # Build out the header
        header = "+" + "+".join(["-"*cw for cw in col_widths]) + "+\n"
        header += "|" + "|".join(self.fid_table_headers) + "|\n"
        header += "+" + "+".join(["="*cw for cw in col_widths]) + "+\n"
        
        # Build out the individual rows
        print(len(self.fid_table))
        row_sets: list[tuple[str]] = []
        for s in range(0, len(self.fid_table), rows):
            print(f"[{s}:{s+rows}]")
            row_sets.append(self.fid_table[s:s+rows])
        row_strings_sets: list[list[str]] = []
        for row_set in row_sets:
            row_strings: list[str] = []
            for row in row_set:
                row_string = "|"
                for i in range(len(row)):
                    row_string += f"{row[i]:{col_widths[i]}}|"
                row_strings.append(row_string + "\n")
            row_strings_sets.append(row_strings)
        
        # Build out the row separators
        row_divider_string = "+" + "+".join(["-"*cw for cw in col_widths]) + "+\n"
        
        # Create the table bodies
        table_bodies: list[str] = []
        for row_strings in row_strings_sets:
            # Join each individual row into the body
            table_body = row_divider_string.join(row_strings)
            
            # Add a bottom line
            table_body += "+" + "+".join(["-"*cw for cw in col_widths]) + "+\n"
            
            # Credit Atlantic Braids
            table_body += "Source: https://atlanticbraids.com/fid-lengths/"
            
            table_bodies.append(table_body)
        
        output_strings: list[str] = [header + tb for tb in table_bodies]
        
        return output_strings

    def text(self):
        """Print out the table in text only mode"""
        print(self.build_table()[0])
    
    def dialog(self):
        """Print out the table using console GUIs. Separates it into multiple shorter
        tables because prompt_toolkit provides no indication to the user that the text
        has been truncated."""
        tables: list[str] = self.build_table(int(len(self.fid_table)/3))
        [message_dialog(
            title=self.title,
            text=table,
            ok_text="Continue",
            style=self.style
        ).run() for table in tables]
    
    def __str__(self):
        return self.title
