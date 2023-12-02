import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "layout", help="colemak or querty layout", choices=["colemak", "querty"]
)
parser.add_argument(
    "filename", help="settings.json file", default="settings.json", type=str
)

filename = parser.parse_args().filename

# Open the JSON file and load the data into a dictionary
with open(filename, "r") as file:
    data = json.load(file)

# Change the setting
if parser.parse_args().layout == "colemak":
    data["vim.normalModeKeyBindingsNonRecursive"] = [
        {"before": ["<space>"], "commands": ["vspacecode.space"]},
        {
            "before": [","],
            "commands": [
                "vspacecode.space",
                {"command": "whichkey.triggerKey", "args": "m"},
            ],
        },
        {"before": ["m"], "after": ["h"]},
        {"before": ["n"], "after": ["j"]},
        {"before": ["e"], "after": ["k"]},
        {"before": ["i"], "after": ["l"]},
        {"before": ["k"], "after": ["n"]},
        {"before": ["K"], "after": ["N"]},
        {"before": ["l"], "after": ["i"]},
        {"before": ["L"], "after": ["I"]},
        {"before": ["f"], "after": ["e"]},
        {"before": ["F"], "after": ["E"]},
        {"before": ["h"], "after": ["m"]},
        {"before": ["<c-n>"], "commands": [":nohl"]},
    ]
    data["vim.visualModeKeyBindingsNonRecursive"] = [
        {"before": ["<space>"], "commands": ["vspacecode.space"]},
        {
            "before": [","],
            "commands": [
                "vspacecode.space",
                {"command": "whichkey.triggerKey", "args": "m"},
            ],
        },
        {"before": [">"], "commands": ["editor.action.indentLines"]},
        {"before": ["<"], "commands": ["editor.action.outdentLines"]},
        {"before": ["m"], "after": ["h"]},
        {"before": ["n"], "after": ["j"]},
        {"before": ["e"], "after": ["k"]},
        {"before": ["i"], "after": ["l"]},
        {"before": ["k"], "after": ["n"]},
        {"before": ["K"], "after": ["N"]},
        {"before": ["l"], "after": ["i"]},
        {"before": ["L"], "after": ["I"]},
        {"before": ["f"], "after": ["e"]},
        {"before": ["F"], "after": ["E"]},
        {"before": ["h"], "after": ["m"]},
    ]
    print(data["vim.normalModeKeyBindingsNonRecursive"])

else:
    data["vim.normalModeKeyBindingsNonRecursive"] = [
        {"before": ["<space>"], "commands": ["vspacecode.space"]},
        {
            "before": [","],
            "commands": [
                "vspacecode.space",
                {"command": "whichkey.triggerkey", "args": "m"},
            ],
        },
        {"before": ["<c-n>"], "commands": [":nohl"]}
    ]
    data["vim.visualModeKeyBindingsNonRecursive"] = [
        {"before": ["<space>"], "commands": ["vspacecode.space"]},
        {
            "before": [","],
            "commands": [
                "vspacecode.space",
                {"command": "whichkey.triggerKey", "args": "m"},
            ],
        },
        {"before": [">"], "commands": ["editor.action.indentLines"]},
        {"before": ["<"], "commands": ["editor.action.outdentLines"]},
    ]

# Write the updated dictionary back into the JSON file
with open(filename, "w") as file:
    json.dump(data, file, indent=2)
