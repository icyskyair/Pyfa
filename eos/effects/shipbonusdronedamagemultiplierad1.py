type = "passive"
def handler(fit, src, context):
    fit.drones.filteredItemBoost(lambda mod: mod.item.requiresSkill("Drones"), "damageMultiplier", src.getModifiedItemAttr("shipBonusAD1"), skill="Amarr Destroyer")
