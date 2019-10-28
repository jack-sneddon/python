from types import Literal

"""
New Types introduced
    Literal types
    Typed dictionaries
    Final objects
    Protocols
"""
# Literal Type
def accepts_only_four(x: Literal[4]) -> None:
    pass

accepts_only_four(4)   # OK
accepts_only_four(19)  # Rejected


