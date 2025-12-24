from typing import Dict, Any
from .base import MPBase

class Magnetic(MPBase):
    """Tools for retrieving magnetic properties (moments, ordering)."""
    
    def get_magnetic_data(self, material_id: str) -> Dict[str, Any]:
        """Fetch raw magnetic data for a specific material ID."""
        data = self.mpr.magnetism.get_data_by_id(material_id)
        return data.dict() if data else {"error": "No magnetic data found"}

