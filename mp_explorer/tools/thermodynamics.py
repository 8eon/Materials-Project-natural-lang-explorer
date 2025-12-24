from typing import Dict, Any
from .base import MPBase

class Thermodynamics(MPBase):
    """Tools for retrieving energy and stability data."""
    
    def get_thermo_data(self, material_id: str) -> Dict[str, Any]:
        """Fetch raw thermodynamics data (stability, energy) for a specific ID."""
        self.record_call(f"Fetching Thermo: {material_id}")
        data = self.mpr.thermo.get_data_by_id(material_id)
        return data.dict() if data else {"error": "No thermo data found"}

