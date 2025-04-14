class Conf:
    """
    Common configuration
    
    Problems to solve:
    
    - debug, stdout shall be fine grained at module level (at least)
    - functions has special config as well
    - maybe move print and stdout to a lib as well, e.g. commons
    """
    def __init__(self, stdout = False, debug = False):
        self.stdout = stdout
        self.debug = debug
    
    def __str__(self):
        return f"conf: (stdout: {self.stdout}, debug: {self.debug})"