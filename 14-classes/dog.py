class Dog :
    """A simple attempt to model a dog."""

    # __init__ is run whenever an object is instanciated
    # 'self' is passed automatically
    def __init__(self, name, age) :
        """Initialize name and age"""
        self.name = name
        self.age = age

    def sit(self) :
        """simulate a dog sitting in response to the command"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self) :
        """simulate a dog rolling over in response to the command"""
        print(f"{self.name.title()} is rolling over.")

