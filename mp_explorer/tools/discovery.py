from typing import List, Dict, Any
from .base import MPBase

class Discovery(MPBase):
    """Tools for searching and finding material IDs."""
    
    def find_materials(self, elements: List[str] = None, chemsys: str = None, **kwargs) -> List[Dict[str, Any]]:
        """
        Search for material IDs and formulas based on chemical criteria.
        Returns a minimal list of material_id and formula.
        """
        self.record_call(f"Materials Search")
        docs = self.mpr.summary.search(
            elements=elements, 
            chemsys=chemsys, 
            fields=["material_id", "formula_pretty"], 
            **kwargs
        )
        return [{"material_id": str(d.material_id), "formula": d.formula_pretty} for d in docs]

