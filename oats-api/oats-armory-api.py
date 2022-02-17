from fastapi import FastAPI, Path, Query, HTTPException
import json
from modelsWeapon import Weapon, UpdateWeapon
from modelsArmor import Armor, UpdateArmor
from modelsExplosive import Explosive, UpdateExplosive
from modelsUpgradeRanged import weaponUpgradeRanged, UpdateWeaponUpgradeRanged
from modelsUpgradeArmor import armorUpgrade, UpdateArmorUpgrade
from equipmentList import weaponClassList, armorClassList, explosiveClassList

f = open("data.json", "r")
itemDb = json.load(f)

description = """
**Ops And Tactics (OATS) Armory API** helps you search for items from the **Ops and Tactics RPG 6th edition** ruleset 🔫

**Ops & Tactics** written and designed by **Sweet Soul Bro !!H5XdMKmBv5G** 

<a href="http://opsandtactics.blogspot.com">http://opsandtactics.blogspot.com/</a>


**You can use the API to do the following:**

* View the whole list of items per equipment category
* Search for items by index per equipment category
* Search for items by name per equipment category
* Search for items by class per equipment category
"""

tags_metadata = [
    {
        "name": "all",
        "description": "View items from the database."
    },
    {
        "name": "weapon",
        "description": "View and weapon items from the database."
    },
    {
        "name": "armor",
        "description": "View and manage armor items from the database."
    },
    {
        "name": "explosive",
        "description": "View and manage explosive items from the database."
    },    
    {
        "name": "weapon upgrade",
        "description": "View and manage weapon upgrade items from the database."
    },
    {
        "name": "armor upgrade",
        "description": "View and manage armor upgrade items from the database."
    }

]

app = FastAPI(
    title="OATS Armory API", 
    openapi_tags=tags_metadata, 
    description=description, 
    version="0.0.1",
    contact={
        "name": "GomenaSorry",
        "url": "https://github.com/GomenaSorry/oats-api",
        "email": "sitdownpowerbomb@gmail.com"
        }
    )

@app.get("/get-all/", tags=["all"])
def get_all():
    return itemDb

@app.get("/get-item/{index}", tags=["all"])
def get_item(index: int = Path(None, description="The index of the item you would like to view")):
    return itemDb[index]

# weapon

@app.get("/weapon/get-name/{weaponName}", tags=["weapon"])
def get_by_name(weaponName: str = Query(None, title="Name", description="Name of the item")):
    for weapon in itemDb:
        if weapon.get('weaponName') == weaponName:
            return weapon
        raise HTTPException(status_code=404, detail="Item name not found")

@app.get("/weapon/get-id/{weaponId}", tags=["weapon"])
def get_by_id(weaponId: str = Query(None, title="Name", description="ID of the item")):
    for weapon in itemDb:
        if weapon.get('weaponId') == weaponId:
            return weapon
    raise HTTPException(status_code=404, detail="Item ID not found")

@app.get("/weapon/get-class/{weaponClass}", tags=["weapon"])
def get_by_class(weaponClass: str = Query(None, title="Name", description="Class of the items")):
    if weaponClass not in weaponClassList:
        raise HTTPException(status_code=404, detail="Item class not found")
    weaponsByClass = list()
    for weapon in itemDb:    
        if weapon.get('weaponClass') == weaponClass:
            weaponsByClass.append(weapon.get('weaponName'))
    return weaponsByClass
  
@app.post("/weapon/create-item/", tags=["weapon"])
def create_item(newWeapon: Weapon):
    for weapon in itemDb:
        if weapon.get('weaponId') == newWeapon.weaponId:
            raise HTTPException(status_code=400, detail="Item already exists")
    itemDb.append(dict(newWeapon))
    return newWeapon

@app.put("/weapon/update-item/{weaponId}", tags=["weapon"])
def update_item(updWeapon: UpdateWeapon, weaponId: str = Query(None, title="Name", description="ID of the item")):
    for weapon in itemDb:
        if weaponId == weapon.get('weaponId'):
            weapon.update(updWeapon)
            return weapon
    raise HTTPException(status_code=404, detail="Item ID not found")

# armor

@app.get("/armor/get-name/{armorName}", tags=["armor"])
def get_by_name(armorName: str = Query(None, title="Name", description="Name of the item")):
    for armor in itemDb:
        if armor.get('armorName') == armorName:
            return armor
        raise HTTPException(status_code=404, detail="Item name not found")

@app.get("/armor/get-id/{armorId}", tags=["armor"])
def get_by_id(armorId: str = Query(None, title="Name", description="ID of the item")):
    for armor in itemDb:
        if armor.get('armorId') == armorId:
            return armor
    raise HTTPException(status_code=404, detail="Item ID not found")

@app.get("/armor/get-class/{armorClass}", tags=["armor"])
def get_by_class(armorClass: str = Query(None, title="Name", description="Class of the items")):
    if armorClass not in armorClassList:
        raise HTTPException(status_code=404, detail="Item class not found")
    armorByClass = list()
    for armor in itemDb:    
        if armor.get('armorClass') == armorClass:
            armorByClass.append(armor.get('armorName'))
    return armorByClass
  
@app.post("/armor/create-item/", tags=["armor"])
def create_item(newArmor: Armor):
    for armor in itemDb:
        if armor.get('armorId') == newArmor.armorId:
            raise HTTPException(status_code=400, detail="Item already exists")
    itemDb.append(dict(newArmor))
    return newArmor

@app.put("/armor/update-item/{armorId}", tags=["armor"])
def update_item(updArmor: UpdateArmor, armorId: str = Query(None, title="Name", description="ID of the item")):
    for armor in itemDb:
        if armorId == armor.get('armorId'):
            armor.update(updArmor)
            return armor
    raise HTTPException(status_code=404, detail="Item ID not found")

# explosive

@app.get("/explosive/get-name/{explosiveName}", tags=["explosive"])
def get_by_name(explosiveName: str = Query(None, title="Name", description="Name of the item")):
    for explosive in itemDb:
        if explosive.get('explosiveName') == explosiveName:
            return explosive
        raise HTTPException(status_code=404, detail="Item name not found")

@app.get("/explosive/get-id/{explosiveId}", tags=["explosive"])
def get_by_id(explosiveId: str = Query(None, title="Name", description="ID of the item")):
    for explosive in itemDb:
        if explosive.get('explosiveId') == explosiveId:
            return explosive
    raise HTTPException(status_code=404, detail="Item ID not found")

@app.get("/explosive/get-class/{explosiveClass}", tags=["explosive"])
def get_by_class(explosiveClass: str = Query(None, title="Name", description="Class of the items")):
    if explosiveClass not in explosiveClassList:
        raise HTTPException(status_code=404, detail="Item class not found")
    explosiveByClass = list()
    for explosive in itemDb:    
        if explosive.get('explosiveClass') == explosiveClass:
            explosiveByClass.append(explosive.get('explosiveName'))
    return explosiveByClass
  
@app.post("/explosive/create-item/", tags=["explosive"])
def create_item(newExplosive: Explosive):
    for explosive in itemDb:
        if explosive.get('explosiveId') == newExplosive.explosiveId:
            raise HTTPException(status_code=400, detail="Item already exists")
    itemDb.append(dict(newExplosive))
    return newExplosive

@app.put("/explosive/update-item/{explosiveId}", tags=["explosive"])
def update_item(updExplosive: UpdateExplosive, explosiveId: str = Query(None, title="Name", description="ID of the item")):
    for explosive in itemDb:
        if explosiveId == explosive.get('explosiveId'):
            explosive.update(updExplosive)
            return explosive
    raise HTTPException(status_code=404, detail="Item ID not found")

# weapon upgrade

@app.get("/weaponupgrade/get-name/{weaponComponentName}", tags=["weapon upgrade"])
def get_by_name(weaponComponentName: str = Query(None, title="Name", description="Name of the item")):
    for component in itemDb:
        if component.get('weaponComponentName') == weaponComponentName:
            return component
        raise HTTPException(status_code=404, detail="Item name not found")

@app.get("/weaponupgrade/get-id/{weaponComponentId}", tags=["weapon upgrade"])
def get_by_id(weaponComponentId: str = Query(None, title="Name", description="ID of the item")):
    for component in itemDb:
        if component.get('weaponComponentId') == weaponComponentId:
            return component
    raise HTTPException(status_code=404, detail="Item ID not found")

@app.post("/weaponupgrade/create-item/", tags=["weapon upgrade"])
def create_item(newWeaponComponent: weaponUpgradeRanged):
    for component in itemDb:
        if component.get('weaponComponentId') == newWeaponComponent.weaponComponentId:
            raise HTTPException(status_code=400, detail="Item already exists")
    itemDb.append(dict(newWeaponComponent))
    return newWeaponComponent

@app.put("/weaponupgrade/update-item/{weaponComponentId}", tags=["weapon upgrade"])
def update_item(updWeaponComponent: UpdateWeaponUpgradeRanged, weaponComponentId: str = Query(None, title="Name", description="ID of the item")):
    for component in itemDb:
        if weaponComponentId == component.get('weaponComponentId'):
            component.update(updWeaponComponent)
            return component
    raise HTTPException(status_code=404, detail="Item ID not found")

# armor upgrade

@app.get("/armorupgrade/get-name/{armorComponentName}", tags=["armor upgrade"])
def get_by_name(armorComponentName: str = Query(None, title="Name", description="Name of the item")):
    for component in itemDb:
        if component.get('armorComponentName') == armorComponentName:
            return component
        raise HTTPException(status_code=404, detail="Item name not found")

@app.get("/armorupgrade/get-id/{armorComponentId}", tags=["armor upgrade"])
def get_by_id(armorComponentId: str = Query(None, title="Name", description="ID of the item")):
    for component in itemDb:
        if component.get('armorComponentId') == armorComponentId:
            return component
    raise HTTPException(status_code=404, detail="Item ID not found")

@app.post("/armorupgrade/create-item/", tags=["armor upgrade"])
def create_item(newArmorComponent: armorUpgrade):
    for component in itemDb:
        if component.get('armorComponentId') == newArmorComponent.armorComponentId:
            raise HTTPException(status_code=400, detail="Item already exists")
    itemDb.append(dict(newArmorComponent))
    return newArmorComponent

@app.put("/armorupgrade/update-item/{weaponComponentId}", tags=["armor upgrade"])
def update_item(updArmorComponent: UpdateArmorUpgrade, armorComponentId: str = Query(None, title="Name", description="ID of the item")):
    for component in itemDb:
        if armorComponentId == component.get('armorComponentId'):
            component.update(updArmorComponent)
            return component
    raise HTTPException(status_code=404, detail="Item ID not found")