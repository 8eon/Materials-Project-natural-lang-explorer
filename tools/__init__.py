from .discovery import Discovery
from .thermodynamics import Thermodynamics
from .electronic import Electronic
from .structure import Structure
from .magnetic import Magnetic

class MPClient(Discovery, Thermodynamics, Electronic, Structure, Magnetic):
    """
    Combined Materials Project Client.
    Inherits from granular feature modules for a clean, modular structure.
    """
    def __init__(self, api_key: str):
        super().__init__(api_key)

