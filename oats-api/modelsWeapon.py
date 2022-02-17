from typing import Optional
from pydantic import BaseModel

class Tactical(BaseModel):
    availTactical: bool
    slotTactical: int

class Caliber(BaseModel):
    caliberName: str
    damage: str
    recoil: int

class Magazine(BaseModel):
    magType: str
    magSize: int
    magCost: int
    magError: int

class Upgrade(BaseModel):
    frame: bool
    barrel: bool
    optics: bool
    tactical: list[Tactical]

class Weapon(BaseModel):
    weaponName: str
    weaponId: str
    weaponClass: str
    caliber: list[Caliber]
    rateOfFire: list
    upgrade: list[Upgrade]
    range: int
    error: float
    magazine: list[Magazine]
    size: str
    weight: float
    cost: int
    license: str

class UpdateWeapon(BaseModel):
    rateOfFire: Optional[list]
    upgrade: Optional[list[Upgrade]]
    range: Optional[int]
    error: Optional[float]
    magazine: Optional[list[Magazine]]
    size: Optional[str]
    weight: Optional[float]
    cost: Optional[int]
    license: Optional[str]