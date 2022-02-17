from pydantic import BaseModel

class armorUpgrade(BaseModel):
    armorComponentName: str
    armorComponentId: str
    cost: int

class UpdateArmorUpgrade(BaseModel):
    cost: int
