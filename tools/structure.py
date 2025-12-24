from typing import Dict, Any
from .base import MPBase

class Structure(MPBase):
    """Tools for retrieving crystal structure data (lattice, sites, symmetry)."""
    
    def get_structure_data(self, material_id: str) -> Dict[str, Any]:
        """Fetch raw crystal structure data for a specific material ID."""
        data = self.mpr.structures.get_data_by_id(material_id)
        return data.dict() if data else {"error": "No structure data found"}

