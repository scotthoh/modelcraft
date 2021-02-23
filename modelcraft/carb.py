from typing import Dict, Optional


class Carb:
    def __init__(self, codes: Dict[str, int], copies: Optional[int] = None):
        self.codes = codes
        self.copies = copies

    def __eq__(self, other) -> bool:
        if isinstance(other, Carb):
            return self.codes == other.codes and self.length == other.length
        return NotImplemented

    @classmethod
    def from_json(cls, component: dict) -> "Carb":
        return cls(codes=component["codes"], copies=component.get("copies"))

    @classmethod
    def from_pdbe_molecule_dict(cls, mol: dict) -> "Carb":
        codes = mol["carb_codes"]
        length = sum(codes.values())
        copies = mol["number_of_copies"] // length
        return cls(codes=codes, copies=copies)

    def to_json(self) -> dict:
        return {"codes": self.codes, "copies": self.copies}
