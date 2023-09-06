#!/usr/bin/env python3
"""Module for providing translations of user-facing messages in the other modules.
At the moment this only provides english (I'm Canadian, so some words might be spelt)
translations because it's the one language that I speak fluently enough to provide
accurate translations for.

In the process of doing all this, I've realized that it does make the code a huge pain
in the ass to maintain, but ¯\_(ツ)_/¯. I'm doing it mostly because it's something I've
never done before.
"""
import utilities


language_options = {"en"}

# +--------------------------------------------------------+
# |                                                        |
# |            Dialog buttons and exit options             |
# |                                                        |
# +--------------------------------------------------------+
yes = {
    "en": "Yes"
}

no = {
    "en": "No"
}

ok = {
    "en": "OK"
}

continue_btn = {
    "en": "Continue"
}

cancel = {
    "en": "Cancel"
}

back = {
    "en": "Back"
}

quit = {
    "en": "Quit"
}


# +--------------------------------------------------------+
# |                                                        |
# |           Calculation questions and results            |
# |                                                        |
# +--------------------------------------------------------+
rope_diameter_message = {
    "en": "Enter the diameter of the rope you are using: "
}

# Used with utilities.radius_or_diameter helper functions
radius_or_diameter_message = {
    "radius": {
        "en": "Enter the desired {name} radius, or d to use diameter: "
    },
    "diameter": {
        "en": "Enter the desired {name} diameter: "
    }
}

chain_diameter_message = {
    "en": "Enter chain link diameter: "
}

tuck_count_message = {
    "en": "Enter the desired number of tucks (5 is typical): "
}

# Single word entries
eye = {
    "en": "eye"
}

sling = {
    "en": "sling"
}

source = {
    "en": "Source"
}

# Results entries
results = {
    "en": "Results"
}

length = {
    "en": "Length"
}

total_length = {
    "en": "Total length"
}

eye_length = {
    "en": "Eye length"
}

loop_length = {
    "en": "Loop length"
}

tuck_length = {
    "en": "Tuck length"
}

lost_length = {
    "en": "Est. length lost"
}

bury_length = {
    "en": "Bury length"
}

tail_length = {
    "en": "Tail length"
}

sling_circumference = {
    "en": "Sling circumference"
}

short_fid = {
    "en": "Short fid"
}

half_fid = {
    "en": "Half fid"
}

long_fid = {
    "en": "Long fid"
}

full_fid = {
    "en": "Full fid"
}


# +--------------------------------------------------------+
# |                                                        |
# |         Script control questions and responses         |
# |                                                        |
# +--------------------------------------------------------+
# Some of these prompts differ between text and dialog modes, so I have split them up
# into two dicts.
select_rope_type_text = {
    "en": "Enter a number from the list to select a type of rope: "
}

select_rope_type_dialog = {
    "en": "What type of rope are you working with?"
}

select_calculation_text = {
    "en": "Enter a number from the list to select a calculation: "
}

select_calculation_dialog = {
    "en": "What calculation do you want to do?"
}

# For the 'utilities.select_from_list' function
select_from_list_error = {
    "en": "'{answer}' is not a valid option. Please try again or select the '{oops_option}' option.\n"
}

# If you are not familiar with command line prompts, yes/no question are often asked in
# this format, ending with [y/n]. Typically Y or N are capitalized, indicating the
# default answer.
end_message = {
    "en": "Run again? [y/N]: "
}

# Because of how I handle this in the script, this translation should be the AFFIMATIVE
# answer to the above question.
end_message_answer = {
    "en": ["y", "yes"]
}

# Categorization error messages
cat_error_message = {
    "en": "The following calculations have been categorized incorrectly and will be omitted:"
}

# The values inside the curly braces within the string MUST remain the same in all
# languages, otherwise they will not be replace correctly.
cat_error_listing = {
    "en": "  Name: {c_title} ({c_rope_type})\n  As rope type: {rt}"
}

# Single word entries
rope_type = {
    "en": "Rope type"
}

calculation = {
    "en": "Calculation"
}

error = {
    "en": "Error"
}


# +--------------------------------------------------------+
# |                                                        |
# |            Rope types and calculation names            |
# |                                                        |
# +--------------------------------------------------------+
rope_types: dict[str, dict[utilities.RopeType, str]] = {
    "en": {
        utilities.RopeType.GENERAL:         "General",
        utilities.RopeType.TWISTED:         "Twisted",
        utilities.RopeType.HOLLOW_BRAID:    "Hollow braid"
    }
}

back_splice = {
    "en": "Back splice"
}

chain_splice = {
    "en": "Chain splice"
}

eye_splice = {
    "en": "Eye splice"
}

locked_eye_splice = {
    "en": "Locked Brummel eye splice"
}

grog_sling = {
    "en": "Grog sling"
}

fid_length_table = {
    "en": "Fid Length Table"
}

fid_length_calculate = {
    "en": "Fid Length Calculator"
}

fid_table_headers: dict[str, tuple[str]] = {
    "en": ("Rope dia. (in)", "Short fid (in)", "Long fid (in)", "Full fid (in)")
}


# +--------------------------------------------------------+
# |                                                        |
# |                       Disclaimer                       |
# |                                                        |
# +--------------------------------------------------------+
# If you need the full text of the disclaimer in a nice, line-wrapped format, see
# README.md
disclaimer_title = {
    "en": "!!! DISCLAIMER - READ FULLY BEFORE CONTINUING !!!"
}

disclaimer_body = {
    "en": "The numbers given by this tool are intended as a guide only. If you plan on using any of the splices described here for lifting or life support appliations, it is your responsibility to make sure you are tying everything correctly and following all relevant laws where you live. There are a lot of variables with splices, and making a mistake with the wrong ones can seriously impact the strength of the final splice. If you doubt yuor skills at all, you should not be trusting your, or other people's, lives to your splices."
}

disclaimer_acknowledge_text_message = {
    "en": "Type 'yes' if you have read and agree to the disclaimer: "
}

# This should be correct answer to the above prompt. Eg. 'yes' for english
disclaimer_acknowledge_text_answer = {
    "en": "yes"
}

disclaimer_acknowledge_dialog = {
    "en": "By selecting 'yes', you are saying that you have read and agree to the disclaimer."
}
