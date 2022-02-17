from typing import Optional
from pydantic import BaseModel

class Explosive(BaseModel):
    explosiveName: str
    explosiveId: str
    explosiveType: str
    damage: str
    damageType: Optional[str]
    blastRadius: Optional[int]
    woundRadius: Optional[int]
    range: int
    size: str
    weight: float
    cost: int
    license: str

class UpdateExplosive(BaseModel):
    explosiveType: str
    damage: str
    damageType: Optional[str]
    blastRadius: Optional[int]
    woundRadius: Optional[int]
    range: int
    size: str
    weight: float
    cost: int
    license: str