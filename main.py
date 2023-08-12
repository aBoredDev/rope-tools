#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import eye_splice, back_splice, general
import re
import utilities


session = PromptSession()

# === Ropes and splices ===
rope_types = ["General", "Twisted", "Hollow braid"]
calculations = [
    [general.FidLength(session)],  # General calculations
    [  # Splices in twisted rope
        eye_splice.TwistedEyeSplice(session),
        back_splice.TwistedBackSplice(session),
    ],
    [eye_splice.HollowBraidLockedEyeSplice(session)],  # Splices in hollow braid rope
]

for i in range(len(calculations)):
    for c in calculations[i]:
        if not c.rope_type == i:
            print(
                f"The following calculation has not been categorized correctly and will be omitted:\n  Name: {c.title}\n  Rope type: {rope_types[c.rope_type]}"
            )
            calculations[i].remove(c)

rope_message = "Enter a number from the list to select a type of rope:"
end_message = "Run again? [y/N]: "

for r in rope_types:
    rope_message += f"\n  {rope_types.index(r)}) {r}"

rope_message += f"\n  {len(rope_types)}) Quit\n\n> "

running = True
while running:
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
    calculations[rope_type][calculation].calculate()

    # See if the user wants to run another calculation
    run_again = session.prompt(end_message)
    if run_again.lower() not in ["y", "yes"]:
        running = False
