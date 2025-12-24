from typing import Dict, Any
from .base import MPBase

class Electronic(MPBase):
    """Tools for retrieving electronic structure data (bandgaps, DOS)."""
    
    def get_electronic_data(self, material_id: str) -> Dict[str, Any]:
        """Fetch raw electronic structure data for a specific material ID."""
        data = self.mpr.electronic_structure.get_data_by_id(material_id)
        return data.dict() if data else {"error": "No electronic data found"}

