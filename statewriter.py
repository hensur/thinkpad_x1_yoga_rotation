"""
writes yoga370d status variables to a config file
"""

from pathlib import Path
from fileinput import FileInput

state = str(Path.home().joinpath(".config/yogad/state.sh"))

def write_state(state_var, state_value):
    """
    finds occurrence of state var and replaces value with updated one
    """
    with FileInput(files=[state], inplace=True) as f:
        state_found = False
        for l in f:
            if l.startswith(state_var.upper() + "="):
                l = state_var.upper() + "=\"" + state_value + "\""
                state_found = True
            print(l, end="")

    if not state_found:
        with open(state, "a") as f:
            f.write(state_var.upper() + "=\"" + state_value + "\"")
