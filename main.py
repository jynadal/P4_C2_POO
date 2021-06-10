""" Défini des clases d'outils."""


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self):
        """Ajoute un outil."""
        pass

    def remove_tool(self):
        """Enleve un outil."""
        pass


class Screwdriver:
    """Tournevis"""

    def __init__(self, size):
        """Initialise la taille."""
        self.size = size
    
    def tighten(self):
        """Serre une vis."""
        print("tighten the Tournevis!")
    
    def loosen(self):
        """Desserre une vis."""
        print("loosen the Tournevis!")


class Hammer:
    """Marteau"""

    def __init__(self, color):
        """Initialise la couleur."""
        self.color = color

    def paint(self, new_color):
        """Paint le marteau"""
        print("Change the hammer's color to {}" . format(new_color))
    
    def hammer_in(self, nail):
        """Enfonce un clou"""
        print("Hammer in")

    def remove(self, nail):
        """Enlevee un clou"""
        print("remove something with the hammer")

marteau1 = Hammer("red")
print(marteau1.color)
marteau1.paint("blue")