

class Strings:
    """
    This Strings object was made to store data from strings separation and use it later
    when comparing fingertips position
    """
    def __init__(self, tuning):
        self.tuning = tuning
        self.separating_lines = {}

    def __str__(self):
        return str(self.separating_lines)

    def __copy__(self):
        new = Strings(self.tuning)
        new.separating_lines = self.separating_lines.copy()
        return new

    def __len__(self):
        return len(self.tuning)-1
