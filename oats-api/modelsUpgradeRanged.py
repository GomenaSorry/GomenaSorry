from cgitb import reset
from difflib import restore
from typing import Optional
from pydantic import BaseModel

class Cost(BaseModel):
    quality: str
    cost: int

class weaponUpgradeRanged(BaseModel):
    weaponComponentName: str
    weaponComponentId: str
    compatibility: list
    location: Optional[list]  = None
    cost: list[Cost]
    time: str
    weight: Optional[float] = None
    license: Optional[str] = None

class UpdateWeaponUpgradeRanged(BaseModel):
    compatibility: list
    location: Optional[list]  = None
    cost: list[Cost]
    time: str
    weight: Optional[float] = None
    license: Optional[str] = None