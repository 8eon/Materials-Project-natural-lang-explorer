from typing import Dict, Any
from .base import MPBase

class Surfaces(MPBase):
    """Tools for retrieving surface properties and Wulff shapes."""
    
    def get_surface_data(self, material_id: str) -> Dict[str, Any]:
        """Fetch raw surface properties (Wulff shapes, surface energies) for a material."""
        self.record_call(f"Surface Data: {material_id}")
        try:
            data = self.mpr.surface_properties.get_data_by_id(material_id)
            return data.dict() if data else {"error": "No surface data found for this material"}
        except Exception as e:
            return {"error": f"Failed to retrieve surface data: {str(e)}"}

