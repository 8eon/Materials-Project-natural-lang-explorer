from mp_api.client import MPRester

class MPBase:
    """Base class to share the Materials Project connection across tools."""
    def __init__(self, api_key: str):
        self.mpr = MPRester(api_key)

