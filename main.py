#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import eye_splice, back_splice, general
import re


session = PromptSession()

# === Ropes and splices ===
rope_types = ['General', 'Twisted', 'Hollow braid']
calculations = [
    [  # General calculations
        general.FidLength(session)
    ],
    [  # Splices in twisted rope
        eye_splice.TwistedEyeSplice(session),
        back_splice.TwistedBackSplice(session)
    ],
    [  # Splices in hollow braid rope
        eye_splice.HollowBraidLockedEyeSplice(session)
    ]
]

for i in range(len(calculations)):
    for c in calculations[i]:
        if not c.rope_type == i:
            print(f'The following calculation has not been categorized correctly and will be omitted:',
                  f'  Name: {c.title}\n  Rope type: {rope_types[c.rope_type]}')
            calculations[i].remove(c)

rope_message = 'Enter a number from the list to select a type of rope:'
end_message = 'Run again? [y/N]: '

for r in rope_types:
    rope_message += f'\n  {rope_types.index(r)}) {r}'

rope_message += f'\n  {len(rope_types)}) Quit\n\n> '

running = True
while running:
    # Ask the question and handle any errors that we can forsee
    while True:
        try:
            rope_type = int(session.prompt(rope_message))
            if rope_type > len(rope_types):
                print(f"'{rope_type}' is not a valid option. Please try again or select the 'Quit' option.\n")
                continue
            break
        except ValueError as e:
            value = re.search(r"'(.*)'$", str(e))
            print(f"'{value.group(1)}' is not a valid option. Please try again or select the 'Quit' option.\n")
    
    if rope_type == len(rope_types):
        break
    
    calc_message = 'Enter a number from the list to select a calculation:'
    
    for c in calculations[rope_type]:
        calc_message += f'\n  {calculations[rope_type].index(c)}) {c.title}'

    
    calc_message += f'\n  {len(calculations[rope_type])}) Back\n\n> '
    # Ask the question and handle any errors that we can forsee
    while True:
        try:
            calculation = int(session.prompt(calc_message))
            if calculation > len(calculations):
                print(f"'{calculation}' is not a valid option. Please try again or select the 'Back' option.\n")
                continue
            break
        except ValueError:
            value = re.search(r"'(.*)'$", str(e))
            print(f"'{value.group(1)}' is not a valid option. Please try again or select the 'Back' option.\n")
    if calculation == len(calculations[rope_type]):
        continue

    calculations[rope_type][int(calculation)].calculate()
    
    run_again = session.prompt(end_message)
    if run_again.lower() not in ['y', 'yes']:
        running = False
