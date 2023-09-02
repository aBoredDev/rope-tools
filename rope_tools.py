"""
aBoredDev's Rope Tools
Tool for calculating the length required for various operations with ropes

Usage:
  rope_tools.py
  rope_tools.py --dialog
  rope_tools.py --help
  rope_tools.py --version

Options:
  -d --dialog   Run in dialog mode.
  -v --version  Show version.
  -h --help     Show this message.
"""
#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog
import eye_splice, back_splice, chain_splice, grog_sling, general
import utilities
from docopt import docopt

arguments = docopt(__doc__, version="aBoredDev's Rope Tools 1.0")
session = PromptSession()
style = Style.from_dict({})
full_screen = arguments["--dialog"]

# === Ropes and splices ===
rope_types = list(utilities.RopeType)
calculations = [
    [general.FidLength(session, style)],  # General calculations
    [  # Splices in twisted rope
        eye_splice.TwistedEyeSplice(session, style),
        back_splice.TwistedBackSplice(session, style),
        chain_splice.TwistedChainSplice(session, style)
    ],
    [  # Splices in hollow braid rope
        eye_splice.HollowBraidLockedEyeSplice(session, style),
        chain_splice.HollowBraidChainSplice(session, style),
        grog_sling.GrogSling(session, style)
    ]
]

cat_errors = []
for rt in rope_types:
    for c in calculations[rt.value]:
        if not c.rope_type == rt:
            cat_errors.append(f"  Name: {c.title} ({c.rope_type})\n  As rope type: {rt}")
            calculations[rt.value].remove(c)

if len(cat_errors):
    if not full_screen:
        print("The following calculations have been categorized incorrectly and will be omitted:\n")
        print("\n  ===\n".join(cat_errors))
    if full_screen:
        m = "The following calculations have been categorized incorrectly and will be omitted:\n"
        m += "\n  ===\n".join(cat_errors)
        message_dialog(
            title="Error",
            text=m,
            style=style
        ).run()

end_message = "Run again? [y/N] "

running = True
while running and not full_screen:
    # Ask what rope type we are working with
    rope_type = utilities.select_from_list(
        session,
        "Enter a number from the list to select a type of rope:",
        rope_types,
        "Quit",
    )

    if rope_type == len(rope_types):
        break
    
    # Ask what calculation the user wants to perform
    calculation = utilities.select_from_list(
        session,
        "Enter a number from the list to select a calculation:",
        calculations[rope_type],
        "Back",
    )

    if calculation == len(calculations[rope_type]):
        continue

    # Run the calculation
    calculations[rope_type][calculation].text()

    # See if the user wants to run another calculation
    run_again = session.prompt(end_message)
    if run_again.lower() not in ["y", "yes"]:
        running = False

while running and full_screen:
    rope_type = radiolist_dialog(
        title="Rope type",
        text="Which type of rope are you working with?",
        values=[[rt.value, str(rt)] for rt in rope_types],
        cancel_text="Quit",
    ).run()

    if rope_type is None:
        running = False
        break

    calculation = radiolist_dialog(
        title="Calculation",
        text="What calculation would you like to make?",
        values=[
            [i, calculations[rope_type][i].title]
            for i in range(len(calculations[rope_type]))
        ],
    ).run()

    if calculation is None:
        continue

    calculations[rope_type][calculation].dialog()
