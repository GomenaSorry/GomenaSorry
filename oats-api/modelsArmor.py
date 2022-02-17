from typing import Optional
from pydantic import BaseModel

class DamageType(BaseModel):
    type: list
    value: int

class Armor(BaseModel):
    armorName: str
    armorId: str
    armorType: str
    armorClass: Optional[str] = None
    equipmentBonus: Optional[int] = None
    maxAgiBonus: Optional[int] = None
    armorPenalty: Optional[int] = None
    combatPointLoss: Optional[int] = None
    armorPoints: int
    weight: float
    cost: int
    damageReduction: list[DamageType]

class UpdateArmor(BaseModel):
    armorType: str
    armorClass: Optional[str] = None
    equipmentBonus: Optional[int] = None
    maxAgiBonus: Optional[int] = None
    armorPenalty: Optional[int] = None
    combatPointLoss: Optional[int] = None
    armorPoints: int
    weight: float
    cost: int
    damageReduction: list[DamageType]
