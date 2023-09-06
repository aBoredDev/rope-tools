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
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog, yes_no_dialog
from prompt_toolkit.formatted_text import FormattedText
import eye_splice, back_splice, chain_splice, grog_sling, general
import translate as tr
import utilities
from docopt import docopt

arguments = docopt(__doc__, version="aBoredDev's Rope Tools 1.0")
session = PromptSession()
style = Style.from_dict({})
full_screen = arguments["--dialog"]
lang = "en"

# Check that the language is one that we have translations for to avoid a TON of KeyErrors
if lang not in tr.language_options:
    if full_screen:
        message_dialog(
            title="Alert",
            text=f"Specified language is unavailable. Available options are {', '.join(tr.language_options)}.\nDefaulting to english.",
            style=style
        )
    else:
        print(f"Specified language is unavailable. Available options are {', '.join(tr.language_options)}.\nDefaulting to english.")
    lang = "en"

# === Ropes and splices ===
rope_types = list(utilities.RopeType)
calculations = [
    [  # General calculations
        general.FidLengthCalculate(session, style),
        general.FidLengthTable(session, style)
    ],
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

# Check that all the calculations have been categorized correctly in case the user has
# added more.
cat_errors = []
for rt in rope_types:
    for c in calculations[rt.value]:
        if not c.rope_type == rt:
            cat_errors.append(tr.cat_error_listing[lang].format(
                c_title=c.title,
                c_rope_type=tr.rope_types[lang][c.rope_type],
                rt=tr.rope_types[lang][rt]
            ))
            calculations[rt.value].remove(c)

# If mis-categorized calculations have been found, notify the user of this, and remove
# the offending calculation from the list.
if len(cat_errors):
    if not full_screen:
        print(f"{tr.cat_error_message[lang]}\n")
        print(*cat_errors, sep="\n  ===\n")
    if full_screen:
        m = f"{tr.cat_error_message[lang]}\n"
        m += "\n  ===\n".join(cat_errors)
        message_dialog(
            title=tr.error[lang],
            text=m,
            style=style
        ).run()

running = True
# Print the disclaimer
if full_screen:
    running = yes_no_dialog(
        title=tr.disclaimer_title[lang],
        text=f"{tr.disclaimer_body[lang]}\n\n{tr.disclaimer_acknowledge_dialog[lang]}",
        style=Style.from_dict({
            "frame.label": "#ff0000",
            "dialog": "bg:#ff0000"
        })
    ).run()
else:
    print_formatted_text(FormattedText([
        ("#ff0000", f"{tr.disclaimer_title[lang]}\n\n")
    ]))
    print(f"{tr.disclaimer_body[lang]}\n\n")
    response = session.prompt(FormattedText([
        ("#ff0000", tr.disclaimer_acknowledge_text_message[lang])
    ]))
    if not response.lower() == tr.disclaimer_acknowledge_text_answer[lang]:
        running = False

while running and not full_screen:
    # Ask what rope type we are working with
    rope_type = utilities.select_from_list(
        session,
        tr.select_rope_type_text[lang],
        [tr.rope_types[lang][rt] for rt in rope_types],
        tr.quit[lang]
    )

    if rope_type == len(rope_types):
        break
    
    # Ask what calculation the user wants to perform
    calculation = utilities.select_from_list(
        session,
        tr.select_calculation_text[lang],
        calculations[rope_type],
        tr.back[lang],
    )

    if calculation == len(calculations[rope_type]):
        continue

    # Run the calculation
    calculations[rope_type][calculation].text()

    # See if the user wants to run another calculation
    run_again = session.prompt(tr.end_message[lang])
    if run_again.lower() not in tr.end_message_answer[lang]:
        break

while running and full_screen:
    rope_type = radiolist_dialog(
        title=tr.rope_type[lang],
        text=tr.select_rope_type_dialog[lang],
        values=[[rt.value, tr.rope_types[lang][rt]] for rt in rope_types],
        cancel_text=tr.quit[lang],
    ).run()

    if rope_type is None:
        break

    calculation = radiolist_dialog(
        title=tr.calculation[lang],
        text=tr.select_calculation_dialog[lang],
        values=[
            [i, calculations[rope_type][i].title]
            for i in range(len(calculations[rope_type]))
        ],
        cancel_text=tr.back[lang]
    ).run()

    if calculation is None:
        continue

    calculations[rope_type][calculation].dialog()
