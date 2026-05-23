import webbrowser
from targets import OPEN_TARGETS


def open_target(target):

    if target in OPEN_TARGETS:

        url = OPEN_TARGETS[target]

        print(f"Opening {target}...")
        webbrowser.open(url)

    else:
        print("Unknown target.")


def process_command(cmd):

    action = cmd[0]

    target = cmd[1:]

    if action == "o":
        open_target(target)

    else:
        print("Unknown action.")
