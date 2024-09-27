from .colors import white
def prompt(message, color=white):
    return input(f"{color} > {message}")